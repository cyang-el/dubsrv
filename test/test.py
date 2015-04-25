import requests

_upload_url = 'http://localhost:8888/upload'
_wav = open('t1.wav', 'rb')
_wav2 = open('t2.wav', 'rb')
send_files = {'audioFile1': _wav, 'audioFile2': _wav2}
r = requests.post(_upload_url, files=send_files)
print(r.status_code)
print(r.text)