from configparser import ConfigParser
import json


def read_json(file):
    with open(file, 'r', encoding='utf-8') as text:
        return json.load(text)


parser = ConfigParser()
parser.read('settings_files/settings.ini')
TOKEN = parser['Bot']['token']
API_KEY = parser['Bot']['api_key']

TEXT = read_json('settings_files/default_text.json')

COMMANDS = read_json('settings_files/commands.json')

LESSONS = {'many/much': 'many_much.jpg', 'предлоги': 'prepositions.jpg', 'Present Simple': 'Present Simple.jpg', 'can/could': 'can_could.jpg',
           'неправильные глаголы': 'irregular_verbs.jpg', 'prepositions': 'prepositions.jpg', 'irregular verbs': 'irregular_verbs.jpg'}

TALKING = {'talk using movie phrases': 'movie',
           'Taylor Swift`s songs': 'taylor',
           'slime molds': 'slime',
           'London architecture': 'london'}