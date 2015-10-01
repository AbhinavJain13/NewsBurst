from system.core.controller import *
import requests

class Stories(Controller):
    def __init__(self, action):
        super(Stories, self).__init__(action)
        self.load_model('Story')

    def index(self):
        return self.load_view('/stories/index.html')

    def import_stories(self):
        print '*** import_stories'
        return self.models['Story'].import_stories()
