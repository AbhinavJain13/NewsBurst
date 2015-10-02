from system.core.controller import *
import requests

class Stories(Controller):
	def __init__(self, action):
		super(Stories, self).__init__(action)
		self.load_model('Story')

	def show(self):

		if not 'loaded_story' in session:
			session['loaded_story'] = {
			'headline' : None,
			'summary' : None
			}

		stories = self.models['Story'].get_all()

		id = session['id']
		
		saved_stories = self.models['Story'].get_saved_stories_by_user_id(id)
		
		popular_stories = self.models['Story'].get_popular_stories()

		speed_data = self.models['Story'].get_speed_data(id)

		if speed_data[0]:
			average_user_speed = int(speed_data[0])
		else:
			average_user_speed = '--'

		if speed_data[1]:
			total_avg_speed = int(speed_data[1])
		else:
			total_avg_speed = '--'

		print 'speed data/////////////////'
		print speed_data


		return self.load_view('stories/index.html', stories=stories, saved_stories=saved_stories, popular_stories=popular_stories, average_user_speed=average_user_speed, total_avg_speed=total_avg_speed)

	def load(self, id):
		print 'entering load'
		print id
		print '=================='
        # id variable is passed from url
        
        # Get story information from database
		story = self.models['Story'].get_story_by_id(id)[0]
		print story
		print story['id']
        # Set up session variable to load story

		session['loaded_story'] = {
			'id' : story['id'],
			'title' : story['title'],
			'abstract' : story['abstract'],
			'published_at' : story['published_at']
			}

		# return self.load_view('partials/load.html')
		# return jsonify(session['loaded_story'])
		# return session['loaded_story']
		return redirect('/show_stories')

	def save(self):

		print 'SAVING STORY --------------------'


		session.pop('loaded_story')
		story_id = request.form['story_id']

		print story_id
		user_id = session['id']

		self.models['Story'].add_story(story_id,user_id)

		return redirect('/show_stories')

	def record(self):
		speed = request.form

		for value in speed:
			speed = value
		
		speed_id = self.models['Story'].record_speed(speed)[0]['id']

		user_id = session['id']

		story_id = session['loaded_story']['id']

		self.models['Story'].record_speedread(speed_id,user_id,story_id)

		return redirect('/show_stories')

	def import_stories(self):
		print '*** import_stories'
		self.models['Story'].import_stories()

		stories = self.models['Story'].get_all()

		return self.load_view('partials/stories.html', stories=stories)

	def remove(self):
		story_id = request.form
		
		for id in story_id:
			story_id = story_id[id]

		
		user_id = session['id']

		self.models['Story'].remove(story_id,user_id)

		
		return redirect('/show_stories')

