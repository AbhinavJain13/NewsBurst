"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes
routes['default_controller'] = 'Users'
routes['POST']['/users'] = 'Users#create'
routes['GET']['/users/<id>'] = 'Users#show'
routes['POST']['/login'] = 'Users#login'
routes['GET']['/logout'] = 'Users#logout'
routes['GET']['/show_stories'] = 'Stories#show'
routes['GET']['/load_story/<id>'] = 'Stories#load'
# routes['GET']['/load_story'] = 'Stories#load'
routes['POST']['/save_story'] = 'Stories#save'
routes['GET']['/story_refresh'] = 'Stories#refresh'
routes['GET']['/stories/import']  = 'Stories#import_stories'
routes['POST']['/record_speed'] = 'Stories#record'
routes['POST']['/remove'] = 'Stories#remove'