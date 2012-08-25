Aeroquad webbased Plotter
-------------------------

Why
---
The AQ Configurator needs a stable connection to be able to send back to telemetry. I needed something wherein the connection could suddenly be gone, and come back up again, using a more stable connection. And as a bonus, you can now get telemetry data on any device which can show html. Almost any smartphone, tablet etc.
The idea of the project is to have a portable solution which works on any platform.

Screenshot
----------
![Screenshot](https://img.skitch.com/20120825-mciasf39b3crj135cjrpk18m4r.preview.jpg "Showing the sensor output")

Run
---
The current setup is somewhat messy, but it's sure going to improve in the future. The first step is to install middleman:

	gem install middleman
	
And install foreman:

	gem install foreman
	
Then install pyserial:

	pip install pyserial
	
My arduino usually shows up on the same serial port, but you might want to check yours in 'listener.py', and change it to the correct one.
And your're all set, now just let middleman take care of the rest:

	middleman start

You can then open up the interface in your favorite browser:

	http://127.0.0.1:4567
	
Middleman actually listens on all your ips, so you can access that page from any pc in that network.

How does it work?
-----------------
Middleman will start 2 processes, one middleman process (which just generates the html pages for now), and a process which connects to your arduino and acts as a proxy for the serial commands and readouts. The html pages will fetch the data through the proxy via ajax calls (will be a websocket in the future), with longpolling.

Todo/Contribute
---------------
A lot, checkout the issue list if you want to help out, or post the issues you have.