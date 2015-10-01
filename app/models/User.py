from system.core.model import Model
from flask import Flask, flash, redirect, session
import re
from flask.ext.bcrypt import Bcrypt

class User(Model):
	def __init__(self):
		super(User, self).__init__()

	def get_user_by_email(self, email):
		return self.db.query_db("SELECT * FROM users WHERE email = '{}' LIMIT 1".format(email))

	def get_user_by_id(self, user_id):
		return self.db.query_db("SELECT * FROM users WHERE id = {} LIMIT 1".format(user_id))

	def create_user(self, newuser):
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')
		any_nonletter_regex = re.compile('[^a-z A-Z]')

		error = False
		fname = newuser['fname']
		lname = newuser['lname']
		email = newuser['email']
		password = newuser['password']
		password2 = newuser['password2']
		print '***** create_user'
		print fname
		print lname
		print email
		print password
		print password2

		if len(fname) < 1:
			error = True
			flash('First name cannot be blank', 'error')

		if len(lname) < 1:
			error = True
			flash('Last name cannot be blank', 'error')

		if len(email) < 1:
			error = True
			flash('Email cannot be blank', 'error')
		elif not EMAIL_REGEX.match(email):
			error = True
			flash('Invalid email address', 'error')

		#*****************************************
		# check if email is already registered
		#*****************************************
		results = self.db.query_db("SELECT * FROM users WHERE email = '{}' LIMIT 1".format(email))
		if results != []:
			error = True
			flash('Email is already registered', 'error')

		if len(password) < 4:
			error = True
			flash('Password must be at least 4 chars', 'error')

		if len(password2) < 4:
			error = True
			flash('Password confirmation must be at least 4 chars', 'error')

		if password != password2:
			error = True
			flash('Password and password confirmation must be the same', 'error')

		if not error:
			# encrypt password
			app = Flask(__name__)
			app.secret_key = 'KeepItSecretKeepItSafe'
			bcrypt = Bcrypt(app)
			pw_hash = bcrypt.generate_password_hash(password)

			query = "INSERT INTO users (fname, lname, email, pw_hash, created_at, updated_at) VALUES ('{}', '{}', '{}', '{}', NOW(), NOW() )".format(fname, lname, email, pw_hash)
			print query
			self.db.query_db(query)

			# registration was successful, so let's automatically
			# log in the user
			session['fname'] = fname
			session['lname'] = lname
			session['email'] = email

			# get user_id (since this is a new user it will be the largest id)
			query = "select * from users order by id desc limit 1"
			result = self.db.query_db(query)
			print '*** get session id'
			print result[0]['id']
			session['id'] = result[0]['id']
#			flash('Successful registration', 'success')
			return True
		else:
			return False
