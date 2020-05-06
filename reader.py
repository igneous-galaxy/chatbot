from configparser import ConfigParser
import json

parser = ConfigParser()
parser.read('settings.ini')
TOKEN = parser['Bot']['token']

with open('default_text.json', 'r', encoding='utf-8') as text:
    TEXT = json.load(text)