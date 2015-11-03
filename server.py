import web
import optimizer

urls = (
   '/', 'index'
)

class index:
   def GET(self):
      output = ""
      players = optimizer.get_lineups()
      with open('optimal.csv', 'rb') as inFile:
         for row in inFile:
            output = output + row
      #raise web.seeother('/static/optimal.csv')
      return output

if __name__ == "__main__": 
   app = web.application(urls, globals())
   app.run()        
