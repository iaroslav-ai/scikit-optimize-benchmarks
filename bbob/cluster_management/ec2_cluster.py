"""
```
sudo pip install boto3
```

Create access keys at https://console.aws.amazon.com/iam , go to users -> create user, enable programmatic access

~/.aws/credentials:
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

To figure out IamFleetRole, go to IAM -> Roles and find fleet role.
Specify the key that you want to use to access created machines for
maintenance.

IAM images should be based on Ubuntu 16.04 image.

"""

import boto3
from pprint import pprint
import os
import time
from tqdm import tqdm
import joblib
import json
import argparse

target_capacity = 20
instance_type = 'c3.large'

config = json.load(open('config.json', 'r'))

recommended_worker_num = {
    'c3.large': 2,
    'c4.large': 2,
    'c3.xlarge': 4,
    'm3.medium': 1,
}

workers_per_instance = 1 #recommended_worker_num[instance_type]

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')


def start_cluster_instances():
    pprint("Starting the cluster instances ... ")

    # Print out bucket names
    cluster = client.request_spot_fleet(
        SpotFleetRequestConfig={
            'AllocationStrategy': 'lowestPrice',
            'IamFleetRole': config['iamfleetrole'],
            'LaunchSpecifications': [
                {
                    'SecurityGroups': [
                        {
                            'GroupId': config['security_group'],
                        }
                    ],
                    'InstanceType': instance_type,
                    'SpotPrice': '0.1',
                    'ImageId': config['ami_image_id'],
                    'KeyName': config['aws_key_name'],
                }
            ],
            'SpotPrice': '0.4',
            'TargetCapacity': target_capacity,
        }
    )

    return {
        'SpotFleetRequestId': cluster['SpotFleetRequestId']
    }


def execute_on(ip, cmd):
    cmd = "ssh -oStrictHostKeyChecking=no -i '" + config['aws_access_key'] + "' ubuntu@" + ip + " '" + cmd + "'"
    os.system(cmd)


def get_instance_ips(cluster):
    rid = cluster['SpotFleetRequestId']

    while True:
        response = client.describe_spot_fleet_instances(
            SpotFleetRequestId=rid
        )

        inst_ids = [inst['InstanceId'] for inst in response['ActiveInstances']]
        ips = [ec2.Instance(id=id).public_ip_address for id in inst_ids]

        if len(ips) >= target_capacity:
            break

        pprint("Current capcity: %s" % len(ips))
        time.sleep(3)

    return ips


def kill_screens(ips):
    # kill all screens in instances
    for instance_ip in tqdm(ips):
        execute_on(instance_ip, 'killall screen')


def execute_on_all(ips, cmd):
    # kill all screens in instances
    for instance_ip in tqdm(ips):
        execute_on(instance_ip, cmd)


def start_dask(ips):
    # start the scheduler on first instance
    primary_ip = ips[0]
    execute_on(primary_ip, 'screen -dmS scheduler bash -c \"dask-scheduler\"')
    scheduler_addr = primary_ip + ":8786"

    # start workers pointing on the scheduler
    for instance_ip in tqdm(ips[1:]):
        for i in range(workers_per_instance):
            execute_on(instance_ip, 'screen -dmS w'+str(i)+' bash -c \"dask-worker ' + scheduler_addr + '\"')

    return primary_ip


def terminate_cluster(cluster):
    client.cancel_spot_fleet_requests(
        SpotFleetRequestIds=[
            cluster['SpotFleetRequestId'],
        ],
        TerminateInstances=True
    )


def cl_make():
    cluster = start_cluster_instances()
    json.dump(cluster, open('cluster.json', 'w'))


def cl_reset():
    cluster = json.load(open('cluster.json'))
    pprint(cluster)

    pprint("Waiting for ips ... ")
    ips = get_instance_ips(cluster)
    pprint("Killing screens if any ... ")
    pprint(" ")
    kill_screens(ips)
    pprint("Starting workers ... ")
    primary_ip = start_dask(ips)
    pprint("")
    pprint("Starting mongos ... ")
    execute_on_all(ips, 'sudo service mongod start')
    pprint("Primary IP address:")
    pprint(primary_ip)


def cl_kill():
    cluster = json.load(open('cluster.json'))
    pprint(cluster)
    terminate_cluster(cluster)

# 'screen -dmS exec sudo bash -c "cd ~/shared && bash run_inf.sh"'
def cl_exec(cmd):

    cluster = json.load(open('cluster.json'))
    pprint(cluster)

    pprint("Waiting for ips ... ")
    ips = get_instance_ips(cluster)
    execute_on_all(ips, cmd)


def cl_mtfs():
    cluster = json.load(open('cluster.json'))
    pprint(cluster)

    ips = get_instance_ips(cluster)
    execute_on_all(ips, "sudo sshfs -o IdentityFile=~/acc.pm root@"+config['file_system_host']
                   +":/root/scikit-optimize-benchmarks ~/shared")


def cl_ip_main():
    cluster = json.load(open('cluster.json'))
    pprint(cluster)

    ips = get_instance_ips(cluster)
    print(ips[0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--kill', action='store_true', help="Destroy the current cluster.")
    parser.add_argument(
        '--make', action='store_true', help="Spawn a cluster.")
    parser.add_argument(
        '--reset', action='store_true', help="Reset the dask connections on cluster.")
    parser.add_argument(
        '--mtfs', action='store_true', help="Mount remote file system on cluster.")
    parser.add_argument(
        '--main', action='store_true', help="Show the IP of Dask scheduler for the cluster.")
    parser.add_argument(
        '--xec', nargs="?", default=None, type=str, help="Command to execute on every node of cluster.")

    args = parser.parse_args()

    if args.kill:
        cl_kill()

    if args.make:
        cl_make()

    if args.reset:
        cl_reset()

    if args.mtfs:
        cl_mtfs()

    if args.main:
        cl_mtfs()

    if args.xec:
        cl_exec(args.xec)
