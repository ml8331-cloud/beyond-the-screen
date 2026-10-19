"""Reproduce descriptive calculations. Python 3 standard library only."""
import csv, json, statistics
from pathlib import Path
from statistics import NormalDist

ROOT = Path(__file__).parent
trends = list(csv.DictReader((ROOT / 'data/trends_weekly.csv').open()))
videos = list(csv.DictReader((ROOT / 'data/youtube_observations.csv').open()))
assert len(trends) == 53
public = [v for v in videos if v['status'] == 'public']
assert len(public) == 5
for col in ('masked_singer', 'floor_fox'):
    vals = [int(r[col]) for r in trends]
    peak = max(vals)
    print(col, 'n=',len(vals), 'mean=',round(statistics.mean(vals),3),
          'peak=',peak, 'weeks=',[r['week_start'] for r in trends if int(r[col]) == peak])
for v in public:
    ratio = 1000 * float(v['likes']) / int(v['views'])
    print(v['id'], 'likes per 1,000 views=',round(ratio,3), v['like_precision'])
p1,p2,alpha,power = .01,.012,.025,.8
pbar = (p1+p2)/2
z = NormalDist()
n = ((z.inv_cdf(1-alpha/2)*(2*pbar*(1-pbar))**.5 +
      z.inv_cdf(power)*(p1*(1-p1)+p2*(1-p2))**.5)**2/(p2-p1)**2)
print('ASSUMED experiment, independent impressions per arm per show:',__import__('math').ceil(n))
print('No campaign lift, audience overlap or causal format preference is measured.')
