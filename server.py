import web
import optimizer

urls = (
   '/', 'index'
)

class index:
   def GET(self):
      players = optimizer.get_lineups()
      return players

if __name__ == "__main__": 
   app = web.application(urls, globals())
   app.run()        
