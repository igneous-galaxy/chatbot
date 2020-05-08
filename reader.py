from configparser import ConfigParser
import json


def read_json(file):
    with open(file, 'r', encoding='utf-8') as text:
        return json.load(text)


parser = ConfigParser()
parser.read('settings.ini')
TOKEN = parser['Bot']['token']

TEXT = read_json('default_text.json')

COMMANDS = read_json('commands.json')