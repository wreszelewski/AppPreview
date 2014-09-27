from tornadorpc.json import JSONRPCHandler
from tornadorpc import start_server
import tornado.web
import tornado.ioloop

class Handler(JSONRPCHandler):

    def get_list(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        return [{'id' : 1, 'name' : 'jeden'},{'id' : 2, 'name' : 'dwa'}]

    def get_another(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        return [{'numer' : 3, 'nazwa' : 'trzy'},{'numer' : 4, 'nazwa' : 'cztery'}]

class DefaultHandler(tornado.web.RequestHandler):

    def options(self):
        self.set_header('Access-Control-Allow-Origin', 'localhost')
        self.set_header('Access-Control-Allow-Methods', 'GET,POST, OPTIONS')

    def get(self):
        self.set_header('Access-Control-Allow-Origin', 'localhost')
        self.set_header('Access-Control-Allow-Methods', 'GET,POST, OPTIONS')

application = tornado.web.Application([
    (r"/api/", Handler),
    (r"/(.*)", tornado.web.StaticFileHandler, {'path' : '.'}),
])

if __name__ == "__main__":
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
