from bbob.evaluation import combine_results, calculate_metrics, get_average_ranking
from pprint import pprint
r = combine_results('d')

m = calculate_metrics(r)
m.to_csv('data.csv')

ra = get_average_ranking('d.csv')

pprint(ra)