from bbob.evaluation import combine_results, calculate_metrics, get_average_ranking
from pprint import pprint
csv_name = '2017.08.csv'

#r = combine_results('d')
#m = calculate_metrics(r)
#m.to_csv('2017.08.csv')

ra = get_average_ranking(csv_name)

for k in sorted(ra):
    v = round(ra[k], 3)
    print(k + " | %s" % v)
