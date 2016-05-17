
def process(messages):
	return extractText(messages)

def extractText(messages):

	output = ""
	for message in messages:
		output += message["text"]
		output += "\n"

	return output