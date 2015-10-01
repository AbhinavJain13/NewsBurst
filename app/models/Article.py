from system.core.model import Model
import requests

class Article(Model):
	def __init__(self):
		super(Article, self).__init__()

	def import_articles(self):
		res = requests.get('http://api.nytimes.com/svc/news/v3/content/all/all?api-key=48bbb9068c763e07d418c6d8bb251c85:7:73103777')

		# res is a unicode dictionary
		print res.status_code
		print res.headers
		# res['results'] is list of articles
		res2 = res.json()
		print 'status: ', res2['status']
		print 'keys: ', res2.keys()
		print 'num_results:', res2['num_results']

		for i in range(10):
			print '*** article {}'.format(i)
			print res2['results'][i]['section']
			print res2['results'][i]['subsection']
			print res2['results'][i]['title']
			print res2['results'][i]['abstract']
			print res2['results'][i]['url']
			print
#			query = "INSERT INTO articles (section, subsection, title, abstract, url, created_at, updated_at, published_at) VALUES ('{}', '{}', '{}', '{}';".format(res2)
#			result = self.db.query_db(query)

		return redirect('/articles')