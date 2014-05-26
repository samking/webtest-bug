import os

import webapp2


class Page(webapp2.RequestHandler):

    def get(self):
        path_info = os.environ.get('PATH_INFO', 'not set.')
        # path_info = self.request.path_info
        self.response.write('The path var is: ' + path_info)


APP = webapp2.WSGIApplication([(r'/', Page)], debug=True)
