# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

class Channel:
    def __init__(self, name, url):
        self.name = name
        self.url = url

CHANNELS = [
    Channel('NDTV 24×7', 'http://ndtvstream-lh.akamaihd.net/i/ndtv_24x7_1@300633/index_224_av-p.m3u8?sd=10&b=256,384&rebase=on&_fwobw=384000&_fwtbw=256000'),
    # Channel('NDTV Profit', ''),
    Channel('NDTV Prime', 'http://ndtvstream-lh.akamaihd.net/i/ndtv_profit_1@300635/master.m3u8?b=256,384'),
    # Channel('NDTV India', ''),
    # Channel('NDTV Goodtimes', 'http://ndtv.live.cdn.bitgravity.com/ndtv/live/ndtvgoodtimelive256')
]

def list_channels():
    for channel in CHANNELS:
        channel_item = xbmcgui.ListItem(label=channel.name)
        channel_item.setInfo('video', {'title': channel.name})
        xbmcplugin.addDirectoryItem(_handle, channel.url, channel_item, False)
    xbmcplugin.endOfDirectory(_handle)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    list_channels()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
