import requests

_upload_url = 'http://localhost:8888/upload'
_wav = open('s1.wav', 'rb')
_wav2 = open('s2.wav', 'rb')
send_files = {'audioFile1': _wav, 'audioFile2': _wav2}
r = requests.post(_upload_url, files=send_files)

with open('dubbed.wav', 'wb') as file:
	file.write(r.content)