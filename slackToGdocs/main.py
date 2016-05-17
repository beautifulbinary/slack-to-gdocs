import requests
import json
import pprint
import users
import channels
from conf import TOKEN, PREV_CHANNELS_PATH
from slackAPI import channelAPI


def main():

	# with open("conf.json") as f:
	# 	settings = json.load(f);

	# token = settings["token"];
	# dataFolder = settings["data-folder"]
	# prevChannels = settings["prev-channels"];

	# params = {
	# 	'token': TOKEN,
	# 	'channel': "C0BREV5CG",
	# 	'oldest': 1
	# }

	# channels.updateChannel("C0BREV5CG", { "lastUpdated": "never", "newStatus": "0", "name": "random" })

	# print(r.json())


	channels.updateChannels()

	# channels = channelAPI.listChannels();

	# cInfo = {}
	# for channel in channels:
	# 	cInfo[channel["id"]] = "archived"

	# out = json.dumps(cInfo, indent=4)

	# with open(PREV_CHANNELS_PATH, 'w') as f:
	# 	f.write(out)
