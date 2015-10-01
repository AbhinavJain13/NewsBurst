from system.core.model import Model
import requests

class Story(Model):
	def __init__(self):
		super(Story, self).__init__()

	def get_all(self):
		query = "SELECT * FROM stories ORDER BY id DESC LIMIT 10"
		return self.db.query_db(query)

	def get_story_by_id(self,id):
		query = "SELECT * FROM stories WHERE id = '{}'".format(id)
		return self.db.query_db(query)

	def add_story(self,story_id,user_id):
		query = "INSERT INTO adds (user_id, article_id, created_at, updated_at) VALUES ('{}','{}',NOW(),NOW())".format(user_id,story_id)
		self.db.query_db(query)
		return

	def get_saved_stories_by_user_id(self,id):
		query = "SELECT stories.title, stories.id,stories.url FROM stories JOIN adds ON adds.article_id = stories.id JOIN users on adds.user_id = users.id WHERE users.id = '{}'".format(id)
		return self.db.query_db(query)

	# def import_stories(self):
	# 	print 'ASKING NYT FOR STORIES'
	# 	res = requests.get('http://api.nytimes.com/svc/news/v3/content/all/all?api-key=48bbb9068c763e07d418c6d8bb251c85:7:73103777')
	# 	# print res

	# 	# # res is a unicode dictionary
	# 	# print res.status_code
	# 	# print res.headers

	# 	# res['results'] is list of articles
	# 	res2 = res.json()

	# 	# print 'status: ', res2['status']
	# 	# print 'keys: ', res2.keys()
	# 	# print 'num_results:', res2['num_results']


	# 	for i in range(10):
	# 		story_i = 
	# 		print '*** article {}'.format(i)
	# 		print res2['results'][i]['section']
	# 		print res2['results'][i]['subsection']
	# 		print res2['results'][i]['title']
	# 		print res2['results'][i]['abstract']
	# 		print res2['results'][i]['url']
	# 	return
# #			query = "INSERT INTO articles (section, subsection, title, abstract, url, created_at, updated_at, published_at) VALUES ('{}', '{}', '{}', '{}';".format(res2)
# #			result = self.db.query_db(query)

		# return redirect('/articles')

