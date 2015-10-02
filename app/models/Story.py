from system.core.model import Model

from flask import Flask, flash, redirect, session

import requests

class Story(Model):
	def __init__(self):
		super(Story, self).__init__()


	def record_speed(self,speed):

		query = "SELECT id FROM speeds WHERE speed = '{}'".format(speed)
		result = self.db.query_db(query)
		if not result:
			query = "INSERT INTO speeds (speed) VALUES ('{}')".format(speed)
			self.db.query_db(query)
			query = "SELECT id FROM speeds ORDER BY id DESC LIMIT 1"
			result = self.db.query_db(query)
		return result

	def record_speedread(self,speed,user,story):

		query = "INSERT INTO speedreads (user_id,speed_id,story_id,created_at) VALUES ('{}','{}','{}',NOW())".format(user,speed,story)
		self.db.query_db(query)
		return True

	def get_speed_data(self,id):
		query = "SELECT avg(speeds.speed) as average_user_speed FROM speeds JOIN speedreads ON speedreads.speed_id = speeds.id JOIN users ON users.id = speedreads.user_id WHERE users.id = '{}'".format(id)
		average_user_speed = self.db.query_db(query)[0]['average_user_speed']
		query = "SELECT AVG(speeds.speed) as total_avg_speed FROM speeds JOIN speedreads ON speedreads.speed_id = speeds.id JOIN users ON users.id = speedreads.user_id WHERE users.id != '{}'".format(id)
		total_avg_speed = self.db.query_db(query)[0]['total_avg_speed']

		speed_data = [average_user_speed,total_avg_speed]
		
		return speed_data

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

	def get_popular_stories(self):
		query = "SELECT stories.title, stories.url, stories.id, count(users.id) as saves FROM stories JOIN adds ON adds.article_id = stories.id JOIN users ON adds.user_id = users.id GROUP BY stories.id ORDER BY saves desc"
		return self.db.query_db(query)

	def import_stories(self):
		res = requests.get('http://api.nytimes.com/svc/news/v3/content/all/world?api-key=48bbb9068c763e07d418c6d8bb251c85:7:73103777')

		# res is a unicode dictionary
		print res.status_code
		print res.headers
		# res['results'] is list of articles
		res2 = res.json()
		print 'status: ', res2['status']
		print 'keys: ', res2.keys()
		print 'num_results:', res2['num_results']

		for i in range( len(res2['results']) ):
			print '*** article {}'.format(i)
			section      = res2['results'][i]['section'].encode('utf-8', 'ignore')
			subsection   = res2['results'][i]['subsection'].encode('utf-8', 'ignore')
			url          = res2['results'][i]['url'].encode('utf-8', 'ignore')
			created_at   = res2['results'][i]['created_date'].encode('utf-8', 'ignore')
			updated_at   = res2['results'][i]['updated_date'].encode('utf-8', 'ignore')
			published_at = res2['results'][i]['published_date'].encode('utf-8', 'ignore')
			title        = res2['results'][i]['title'].encode('ascii', 'ignore')
			abstract     = res2['results'][i]['abstract'].encode('ascii', 'ignore')

			# convert Unicode chars to ascii with escape chars for SQL
#			title = title.replace(u'\u2010', "-")
#			title = title.replace(u'\u2018', "\\'")
#			title = title.replace(u'\u2019', "\\'")
#			title = title.replace(u'\u201c', "\\\"")
#			title = title.replace(u'\u201d', "\\\"")
#			abstract = abstract.replace(u'\u2010', "-")
#			abstract = abstract.replace(u'\u2018', "\\'")
#			abstract = abstract.replace(u'\u2019', "\\'")
#			abstract = abstract.replace(u'\u201c', "\\\"")
#			abstract = abstract.replace(u'\u201d', "\\\"")

			# do not insert story if it's already in DB
			query = "SELECT * FROM stories s where s.title='{}'".format(title)
			result = self.db.query_db(query)
			print '**** result'
			print result
			if not result:
				query = "INSERT INTO stories (section, subsection, title, abstract, url, created_at, updated_at, published_at) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(section, subsection, title, abstract, url, created_at, updated_at, published_at)
				print query
				result = self.db.query_db(query)
			else:
				print '**** skipped duplicate story'

		return redirect('/show_stories')
