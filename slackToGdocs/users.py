import requests
from slackAPI import userAPI

def getUsernameIDMap():

	users = userAPI.listUsers()

	# Iterate through each user
	usernames = {};
	for member in users:
		member_id = member["id"];
		member_uname = member["name"]

		usernames[member_id] = member_uname;

	return usernames;