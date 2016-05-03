import requests
from util import util

def getUsers(token):
	r = requests.post('https://slack.com/api/users.list', data = {'token': token});

	response = util.getJSON(r, "Error in getting user list")

	# Iterate through each user
	usernames = {};
	for member in response["members"]:
		member_id = member["id"];
		member_uname = member["name"]

		usernames[member_id] = member_uname;

	return usernames;