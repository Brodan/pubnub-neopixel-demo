import re
import os
import argparse
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub


def hex_to_rgb(value):
    """Return (Red, Green, Blue) for the color given as #rrggbb.

    src: http://stackoverflow.com/a/214657/5045925
    """
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def pub(message):
    pubnub.publish().channel('demo').message(message).sync()


if __name__ == '__main__':
    # Configure and initialize Pubnub
    pnconfig = PNConfiguration()
    pnconfig.subscribe_key = os.environ['PUBNUB_SUBSCRIBE_KEY']
    pnconfig.publish_key = os.environ['PUBNUB_PUBLISH_KEY']
    pnconfig.enable_subscribe = False
    pubnub = PubNub(pnconfig)

    # Parse command line arguement.
    parser = argparse.ArgumentParser(
        description='Display a color on a Neopixel grid.')
    parser.add_argument('hexcolor', action="store")
    args = parser.parse_args()

    # Validate command line argument is proper hex code.
    # regex src: http://stackoverflow.com/a/1637260/5045925
    if re.match('^#(([0-9a-fA-F]{2}){3}|([0-9a-fA-F]){3})$',
                args.hexcolor) is not None:
        hexcolor = hex_to_rgb(args.hexcolor)
        data = {
            'color': hexcolor
        }
        pub(data)
    else:
        print('Please pass a valid color hex code. e.g. #FFF000 or #FFF')
