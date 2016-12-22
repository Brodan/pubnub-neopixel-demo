import atexit
import time
import os
from neopixel import *
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration

# LED grid configuration:
LED_COUNT = 64          # Number of LED pixels.
LED_PIN = 18            # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000    # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5             # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 200    # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False


class MySubscribeCallback(SubscribeCallback):
    """Handle incoming pubnub messages."""

    def message(self, pubnub, message):
        print('Message received: {}'.format(message.message))
        colorWipe(grid, Color(*message.message['color']))


def colorWipe(grid, color, wait_ms=50):
    """Wipe color across display a pixel at a time.

    src: github.com/jgarff/rpi_ws281x/blob/master/python/examples/strandtest.py
    """
    for i in range(grid.numPixels()):
        grid.setPixelColor(i, color)
        grid.show()


def exit_handler(grid):
    """Turn off all pixels on program exit."""
    for i in range(grid.numPixels()):
        grid.setPixelColor(i, 0)
        grid.show()


if __name__ == '__main__':
    # Initialize PubNub and add listener.
    pnconfig = PNConfiguration()
    pnconfig.subscribe_key = os.environ['PUBNUB_SUBSCRIBE_KEY']
    pnconfig.ssl = True
    pubnub = PubNub(pnconfig)
    pubnub.add_listener(MySubscribeCallback())

    # Create NeoPixel object with appropriate configuration.
    grid = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    # Intialize the library (must be called once before other functions).
    grid.begin()

    atexit.register(exit_handler, grid)

    try:
        pubnub.subscribe().channels('demo').execute()
        print ('Listening for messages. Press Ctrl-C to quit.')
        while(True):
            time.sleep(100)

    except KeyboardInterrupt:
        print('\nExiting...')
        pubnub.unsubscribe().channels('demo').execute()
        pubnub.stop()
