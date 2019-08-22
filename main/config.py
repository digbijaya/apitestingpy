import json
import os
from main.djExept import applicatonEx

try:
    with open("../config.json") as file:

    # file = open("../config.json")
        config_data = json.load(file)
        print(config_data)

    # dirpath = os.getcwd()
    # print(dirpath)
except (FileNotFoundError, Exception) as exc:
    print(exc)
    raise applicatonEx("Please fix the config.json")

# config_data = json.load(open("../config.json"))
# print(config_data)