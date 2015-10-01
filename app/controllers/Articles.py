from system.core.controller import *
import requests

class Articles(Controller):
    def __init__(self, action):
        super(Articles, self).__init__(action)
        self.load_model('Article')

    def index(self):
        return self.load_view('/articles/index.html')

    def import_articles(self):
        print '*** import_articles'
        return self.models['Article'].import_articles()
