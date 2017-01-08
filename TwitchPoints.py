#licensed under the MIT license. See LICENSE,md for more information.

import config
import pytwitcherapi
import threading

MainClient = pytwitcherapi.TwitchSession()

MainClient.client_id = config.client_id

def MainElapse():

    if(MainClient.get_stream(config.channelname).viewers > 0):
        MainClient.

timer = threading.Timer(60, MainElapse)
timer.start()