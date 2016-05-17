import os.path
import json
import sys
import time
from slackAPI import channelAPI
import messageProcessor
from conf import PREV_CHANNELS_PATH, DATA_FOLDER

#read the status of the channels from last run
def getOldChannelStatus():
	try:
		f = open(PREV_CHANNELS_PATH, 'r');
		channels = json.load(f);

	# Couldn't find channels file
	except FileNotFoundError:

		response = input("Previous channel information file not found; will archive all messages.  Continue? [y/n]: ")
		while response.strip() != 'y' and response != 'n':
			response = input("Please type 'y' or 'n': ");

		if response == 'y':
			return {}
		else:
			sys.exit()

	except json.decoder.JSONDecodeError:

		print("Could not parse previous channel information file: " + PREV_CHANNELS_PATH)
		sys.exit()

	except:
		raise

	return channels

''' 
Compares old and current status of channels, returns a list of 
	channelID: {
		"lastUpdated": {"never", <timestamp>}
		"newStatus": {<timestamp>, "archived"}
	}

TODO: What if channels renamed?
'''
def getChannelsToUpdate(oldChannelStatus, channelStatus):
	updateTime = int(time.time())
	updates = {}

	for channel in channelStatus:

		lastUpdated = oldChannelStatus[channel["id"]] if (channel["id"] in oldChannelStatus) else "never";

		#Skipping archived channels, TODO not taking into account unarchiving
		if lastUpdated == "archived":
			continue;

		print(channel["id"])

		newStatus = "archived" if (channel["is_archived"] == True) else str(updateTime);

		updates[channel["id"]] = { "lastUpdated": lastUpdated, "newStatus": newStatus, "name": channel["name"] }

	return updates;


def updateChannels():
	oldChannelStatus = getOldChannelStatus();

	channelStatus = channelAPI.listChannels();

	updates = getChannelsToUpdate(oldChannelStatus, channelStatus)

	print (updates)


	for channelID, update in updates.items():
		updateChannel(channelID, update);


def getFileName(channelID, update):
	return ("{0}-#{1}-{2}-{3}.txt".format(channelID, update["name"], update["lastUpdated"], update["newStatus"]))

def updateChannel(channelID, update):

	print("Updating channel #{0}\n".format(update["name"]))

	messages = channelAPI.getChannelMessages(channelID, update["lastUpdated"])

	if len(messages) == 0:
		return

	ts = messages[0]["ts"];

	for message in messages:
		if ts > message["ts"]:
			print("messages retrieved in wrong order");
			sys.exit()

		ts = message["ts"];

	output = messageProcessor.process(messages);

	filename = DATA_FOLDER + "/" + getFileName(channelID, update)
	with open(filename, 'w') as f:
		f.write(output)







