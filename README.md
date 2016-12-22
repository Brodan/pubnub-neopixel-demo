# PubNub-Neopixel-Demo
Demo app to power an LED matrix with RPi + Pubnub

![gif](http://i.imgur.com/Rehv667.gif)

# Requirements
- Raspberry Pi (I used [Model 1B](https://www.raspberrypi.org/products/model-b/), other models should work.)
- [Adafruit NeoPixel NeoMatrix](https://www.adafruit.com/product/1487) or any [NeoPixel](https://www.adafruit.com/categories/168) device.
- Python 3 + pip

# Instructions
Follow the instructions below to run this app locally.

## Raspberry Pi:
### Compile & Install rpi_ws281x Library
The rpi_ws281x library is the key that makes using NeoPixels with the Raspberry Pi possible. SSH into your Raspberry Pi and follow [these instructions](https://learn.adafruit.com/neopixels-on-raspberry-pi/software) to download and compile the library.

### Clone Source

```
$ git clone https://github.com/Brodan/PubNub-Neopixel-Demo.git
$ pip install -r requirements.txt
$ export PUBNUB_SUBSCRIBE_KEY='your_subscribe_key_here'
$ sudo python subscriber.py
```
Note: `sudo` is being used here to access the pinouts on the Raspberry Pi.

## On Your Local Machine

Retrive your Pubnub keys from https://admin.pubnub.com/
```
$ git clone https://github.com/Brodan/PubNub-Neopixel-Demo.git
$ pip install -r requirements.txt
$ export PUBNUB_SUBSCRIBE_KEY='your_subscribe_key_here'
$ export PUBNUB_PUBLISH_KEY='your_publish_key_here'
$ python publisher.py '#FFFFFF'
```
You can run this script any number of times with any valid hex color code.