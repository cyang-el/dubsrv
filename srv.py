import tornado
import tornado.ioloop
import tornado.web
from pydub import AudioSegment
import os 

__UPLOADS__ = "uploads/"
__DOWNLOADS__ = "downloads/"

def overdub(_files, _returnPath):
	print(_files[0], _files[1])
	s1, s2 = AudioSegment.from_wav(_files[0]), AudioSegment.from_wav(_files[1])
	_dubbed = s1.overlay(s2)
	_dubbed.export(_returnPath, format='wav')
	return True

 
class DSLinfo(tornado.web.RequestHandler):
    def get(self):
        self.render("static/index.html")
 

class Upload(tornado.web.RequestHandler):
	def post(self):
		_paths = []
		_returnPath = __DOWNLOADS__ + 'ret.wav'
		_httpfiles = self.request.files['audioFile1'][0], self.request.files['audioFile2'][0]
		for _httpfile in _httpfiles:
			_name = _httpfile['filename']
			fh = open(__UPLOADS__ + _name, 'wb')
			fh.write(_httpfile['body'])
			_paths.append(__UPLOADS__ + _name)
			print(_name)
		if overdub(_paths, _returnPath) == True:
			self.write(str(_returnPath))


application = tornado.web.Application([
        (r"/", DSLinfo),
        (r"/upload", Upload),
        ], debug=True)
 
 
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
