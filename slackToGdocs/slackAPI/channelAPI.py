import requests
from slackAPI import util
from conf import TOKEN

def listChannels():
	params = {
		'token': TOKEN
	}

	r = requests.post('https://slack.com/api/channels.list', params);

	response = util.getJSON(r, "Error in getting user list")

	return response["channels"];

#returns the messages from #channelID newer than lastUpdated.
# if lastUpdated == "never" then this function will fetch all messages in the channel
def getChannelMessages(channelID, lastUpdated):
	
	# oldest param of 1 instead of 0 so that message chunks are fetched oldest to newest
	params = {
		'token': TOKEN,
		'channel': channelID,
		'oldest': 1 if lastUpdated == "never" else int(lastUpdated)
	}

	messages = [];

	# "Do while"
	while True:

		r = requests.post('https://slack.com/api/channels.history', params);
		response = util.getJSON(r, "Error in getting messages for channel " + channelID);

		# Empty channel, should only trigger in first iteration
		if (len(response["messages"]) == 0):
			break

		# Sort this chunk of messages ascending by timestamp.
		# Last message's timestamp will be next "oldest" param
		newMessages = response["messages"]
		sortedMessages = sorted(newMessages, key=lambda k: k['ts'])
		params["oldest"] = sortedMessages[-1]["ts"];

		messages.extend(sortedMessages)

		if response["has_more"] == False:
			break

	return messages

