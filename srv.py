import tornado
import tornado.ioloop
import tornado.web
from pydub import AudioSegment
import os 

__UPLOADS__ = "tmp/"
__DOWNLOADS__ = "tmp/"

def overdub(_files, _returnPath):
	s1, s2 = AudioSegment.from_wav(_files[0]), AudioSegment.from_wav(_files[1])
	_dubbed = s1.overlay(s2)
	_dubbed.export(_returnPath, format='wav')
	os.remove(_files[0])
	os.remove(_files[1])
	return True


def filename_gen():
	import uuid
	return "{0}.wav".format(uuid.uuid4())
 
class DSLinfo(tornado.web.RequestHandler):
    def get(self):
        self.render("static/index.html")
 

class Upload(tornado.web.RequestHandler):
	def post(self):
		_paths = []
		filename = filename_gen()
		_returnPath = __DOWNLOADS__ + filename
		_httpfiles = self.request.files['audioFile1'][0], self.request.files['audioFile2'][0]
		for _httpfile in _httpfiles:
			_name = _httpfile['filename']
			fh = open(__UPLOADS__ + _name, 'wb')
			fh.write(_httpfile['body'])
			_paths.append(__UPLOADS__ + _name)
			print(_name)
		if overdub(_paths, _returnPath) == True:
			fr = open(_returnPath, 'rb')
			self.write(fr.read())
			#self.render("static/mixdown.html", mixfile = _returnPath)
		os.remove(_returnPath)


application = tornado.web.Application([
        (r"/", DSLinfo),
        (r"/upload", Upload),
        ], debug=False)
 
 
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
