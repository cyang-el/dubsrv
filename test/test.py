import requests

_upload_url = 'http://ec2-52-24-32-8.us-west-2.compute.amazonaws.com:8888/upload'
_wav = open('t1.wav', 'rb')
_wav2 = open('t2.wav', 'rb')
send_files = {'audioFile1': _wav, 'audioFile2': _wav2}
r = requests.post(_upload_url, files=send_files)

with open('dubbed.wav', 'wb') as file:
	file.write(r.content)