What
----
a simple wav dubbing web api using `tornado <https://github.com/tornadoweb/tornado>`_ and `pydub <https://github.com/jiaaro/pydub>`_.

How
---
1. `install docker <http://docs.docker.com/installation/debian/>`_ 
2. Pull the images from dockerhub::

	docker pull showjackyang/dubsrv

3. Run the images::

	sudo docker run -d -p 8888:8888 showjackyang/dubsrv
