<p align="center">
  <img src="http://www.raspberryturk.com/assets/img/logo.svg" width="120px" />
</p>

# Raspberry Turk

The Raspberry Turk is a robot that can play chess—it's entirely open source, based on Raspberry Pi, and inspired by the 18th century chess playing machine, the Mechanical Turk. The project incorporates aspects of computer vision, data science, machine learning, robotics, 3D printing, and—of course—chess.

## Website

A website describing the robot and how it was made can be found [here](http://www.raspberryturk.com).

## The missing instruction

0. For Mac only, get Python 2 to work

	```shell
	# Uninstall python 2 first
	$brew uninstall python@2
	
	# Reinstall python 2 from a package. The simple brew install python@2 does not work anymore
	$brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/86a44a0a552c673a05f11018459c9f5faae3becc/Formula/python@2.rb
	```
1. Installation 
	```shell    
	$python setup.py install
	```
2. 


sudo dd if=/dev/zero of=/media/fasthdd/swapfile.img bs=1024 count=2M

## Creator

[Joey Meyer](http://www.raspberryturk.com/aboutme.html)

## License

Raspberry Turk is available under the MIT license. See the LICENSE file for more info.
