import requests
from slackAPI import util
from conf import TOKEN

def listUsers(token):
	r = requests.post('https://slack.com/api/users.list', data = {'token': TOKEN});

	response = util.getJSON(r, "Error in getting user list")

	return response["members"]