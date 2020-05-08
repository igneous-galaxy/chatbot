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

LESSONS = {'many/much': 'many_much.jpg', 'предлоги': 'prepositions.jpg', 'Present Simple': 'Present Simple.jpg', 'can/could': 'can_could.jpg',
           'неправильные глаголы': 'irregular_verbs.jpg', 'prepositions': 'prepositions.jpg', 'irregular verbs': 'irregular_verbs.jpg'}