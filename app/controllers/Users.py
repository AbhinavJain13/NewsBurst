from system.core.controller import *
from flask import Flask, flash, session
from flask.ext.bcrypt import Bcrypt

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('User')

	def index(self):
		return self.load_view('users/index.html')

	def create(self):
		print '***** create'
		newuser = request.form
		result = self.models['User'].create_user(newuser)
		if result is True:
			return redirect('/articles')
		else:
			return redirect('/')

	def show(self, id):
		print '*** show'
		userinfo = self.models['User'].get_user_by_id(user_id=id)
		playlistinfo = self.models['User'].get_playlistinfo(user_id=id)

		return self.load_view('users/playlist.html', userinfo=userinfo, playlistinfo=playlistinfo)


	def login(self):
		print '***** login'
		email    = request.form['email']
		password = request.form['password']

		results = self.models['User'].get_user_by_email(email)
		if results == []:
			flash('Bad password or email', 'error')
			return redirect('/')
        
		app = Flask(__name__)
		bcrypt = Bcrypt(app)
		if bcrypt.check_password_hash(results[0]['pw_hash'], password):
			session['id']    = results[0]['id']
			session['fname'] = results[0]['fname']
			session['lname'] = results[0]['lname']
			session['email'] = results[0]['email']
			print '*** session id: {}'.format(session['id'])
			return redirect('/articles')
		else:
			flash('Bad password or email', 'error')
			return redirect('/')

	def logout(self):
		session.clear()
		return redirect('/')