from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.dist import use_library
use_library('django', '1.2')
from google.appengine.ext.webapp import template
from mineddist import minEditDist, decide_vote
import os
import logging



class Exercise0Handler(webapp.RequestHandler):
    def get(self):        
        vals = {}
        #result = ""
        candidate = self.request.get("candidate")
        vals["candidate"] = candidate
        logging.info(minEditDist("Duggan", "Duggan"))
        logging.info(minEditDist("Dug", "Duggan"))
        #vals["candidate"] = candidate
        # logging.info("TESTING LOGGING")
        # logging.info(minEditDist(candidate, "Duggan"))
        # logging.info(minEditDist(candidate,"Dugeon"))
        # if minEditDist(candidate,"Duggan") > 3: #minEditDist(candidate, "Dugeon"):
        #   result = "Duggan"
        # elif minEditDist(candidate,"Dugeon") > #minEditDist(candidate,"Duggan"):
        #   result = "Dugeon"
        # else:
          # result = "Too Close to call"
        #candidate = self.request.get("candidate")
        logging.info("here is candidate")
        logging.info(candidate)
        result = decide_vote(candidate)
        logging.info(result)
        vals["result"] = result
        

        # add code to fill in vals dictionary here
        fname = os.path.join(os.path.dirname(__file__), 'templates/exercise2.tpl')
        page_contents = template.render(fname, vals)
        self.response.out.write(page_contents)

# class Exercise1Handler(webapp.RequestHandler):
# 	def get(self):
# 		vals = {}
# 		candidate = self.request.get("candidate")
# 		result = decide_vote(candidate)
#         vals["result"] = result

#         fname = os.path.join(os.path.dirname(__file__), 'templates/result.tpl')
#         page_contents = template.render(fname, vals)
#         self.response.out.write(page_contents)
    

def main():
    # in the start code we'd give the code for photoPageHandler (without any embellishments)
    application = webapp.WSGIApplication([
                                          ('/', Exercise0Handler)
                                          #('/result', Exercise1Handler),
                                          # ('/exercise2', Exercise2Handler),
                                          # ('/exercise3', Exercise3Handler)
                                          ])
    util.run_wsgi_app(application)
    

if __name__ == '__main__':
    main()
