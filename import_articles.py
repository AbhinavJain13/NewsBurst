import requests
import json

#res = requests.get('http://api.nytimes.com/svc/news/v3/content/all/all/.xml?api-key=48bbb9068c763e07d418c6d8bb251c85:7:73103777')

res = requests.get('http://api.nytimes.com/svc/news/v3/content/all/all?api-key=48bbb9068c763e07d418c6d8bb251c85:7:73103777')

# res is a unicode dictionary

print res.status_code
print res.headers
# res['results'] is list of articles
#print res['results']

res2 = res.json()
print 'status: ', res2['status']
print 'keys: ', res2.keys()
print 'num_results:', res2['num_results']

for i in range(10):
	print res2['results'][i]['section'].encode('utf-8')
	print res2['results'][i]['subsection'].encode('utf-8')
	print res2['results'][i]['title'].encode('utf-8')
	print res2['results'][i]['abstract'].encode('utf-8')
	print

# zzz.encode('utf-8')
# Colm Toibin: By the Book  abstract