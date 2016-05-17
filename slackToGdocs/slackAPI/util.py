import requests

def getJSON(response, errorMsg):

	response = response.json();

	if "error" in response:
		raise RuntimeError(errorMsg + " " + response["error"]);
	elif "warning" in response:
		print(errorMsg + " Warning received: " + str(response["warning"]))

	return response;