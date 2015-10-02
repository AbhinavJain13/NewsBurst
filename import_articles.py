import requests
import json

def get_articles():
	#res = requests.get('http://api.nytimes.com/svc/news/v3/content/all/all/.xml?api-key=48bbb9068c763e07d418c6d8bb251c85:7:73103777')

	# all articles
	#res = requests.get('http://api.nytimes.com/svc/news/v3/content/all/all?api-key=48bbb9068c763e07d418c6d8bb251c85:7:73103777')

	# World and US articles
	res = requests.get('http://api.nytimes.com/svc/news/v3/content/all/all?api-key=48bbb9068c763e07d418c6d8bb251c85:7:73103777')

	# res is a unicode dictionary

	print res.status_code
#	print res.headers
	# res['results'] is list of articles
	#print res['results']

	res2 = res.json()
#	print 'status: ', res2['status']
#	print 'keys: ', res2.keys()
	print 'num_results:', res2['num_results']

	for i in range(20):
		section    = res2['results'][i]['section'])
		subsection = res2['results'][i]['subsection']
		title      = res2['results'][i]['title']
		abstract   = res2['results'][i]['abstract']
		url        = res2['results'][i]['url']

		# convert Unicode chars to ascii
		title = title.replace(u'\u2010', "-")
		title = title.replace(u'\u2018', "\'")
		title = title.replace(u'\u2019', "\'")
		title = title.replace(u'\u201c', "\"")
		title = title.replace(u'\u201d', "\"")
#		title = str(title)
		abstract = abstract.replace(u'\u2010', "-")
		abstract = abstract.replace(u'\u2018', "\'")
		abstract = abstract.replace(u'\u2019', "\'")
		abstract = abstract.replace(u'\u201c', "\"")
		abstract = abstract.replace(u'\u201d', "\"")
#		abstract = str(abstract)
#		print res2['results'][i]['section'].encode('utf-8')
#		print res2['results'][i]['subsection'].encode('utf-8')
#		print res2['results'][i]['title'].encode('utf-8')
#		print res2['results'][i]['abstract'].encode('utf-8')
#		print res2['results'][i]['url'].encode('utf-8')
		print 'section:    {}'.format(section)
		print 'subsection: {}'.format(subsection)
		print type(title)
		print abstract
		print url
		print

def get_section_names():
	# get all section names
	print '***** section names' 
	response = requests.get('http://api.nytimes.com/svc/news/v3/content/section-list?api-key=48bbb9068c763e07d418c6d8bb251c85:7:73103777')

	response2 = response.json()
	for item in response2['results']:
		print item['section']


#get_section_names()

get_articles()