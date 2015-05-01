What
----
A simple wav dubbing web api using `tornado <https://github.com/tornadoweb/tornado>`_ and `pydub <https://github.com/jiaaro/pydub>`_.
*(only for Samplerate 44100.0 Hz Bitdepth 16bits wav files)*

How
---
1. `Install docker <http://docs.docker.com/installation/debian/>`_ 
2. Pull the docker image from dockerhub::

	sudo docker pull showjackyang/dubsrv

3. Run the docker image::

	sudo docker run -d -p 8888:8888 showjackyang/dubsrv

4. Posting http request with two wav files to *localhost:8888/upload* will return a dubbed wav file.
