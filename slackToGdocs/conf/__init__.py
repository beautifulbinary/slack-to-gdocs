import json

with open("conf.json") as f:
		settings = json.load(f);

TOKEN = settings["token"];
DATA_FOLDER = settings["data-folder"]
PREV_CHANNELS_FILE = settings["prev-channels"];

PREV_CHANNELS_PATH = DATA_FOLDER + '/' + PREV_CHANNELS_FILE