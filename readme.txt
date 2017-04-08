PiPyKoki - an implementation of libkoki and pykoki for the raspberry pi and pi camera module.

Dependencies/Instructions:
To install, clone to a pi.
Get dependencies:
	sudo apt-get install libopencv-dev libyaml-dev freeglut3-dev scons python-opencv
Go to libkoki directory then:
	sudo chmod 755 create-pkg-config
	sudo scons
Go to pykoki directory then:
	sudo python setup.py install
To test timing, from the robot directory run:
	python visiontest.py

General usage:
	from vision import *
Initialise camera with:
	self.cam = Vision()

Useful definition:
	def see((x,y) = (800,600), preview = False, preview_time = 1):
		return self.cam.vision_see((x,y), preview, preview_time)

(x,y) is camera resolution
preview = True displays what the camera sees on the pi screen
preview_time is the time in seconds the preview is shown before the capture


