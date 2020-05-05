f = open('movie_conversations.txt')
conversations = f.readlines()
f.close()
# словарь, в котором ключ - это первая фраза, а значение - следующая за ней (фразы в виде меток)
line_after_line = dict()
# сценарии диалогов с метками
for i in range(len(conversations)):
    conversations[i] = eval(conversations[i].split(' +++$+++ ')[-1][:-1])
    for j in range(len(conversations[i]) - 1):
        line_after_line[conversations[i][j]] = conversations[i][j + 1]

main_lines = line_after_line.keys()

f = open('movie_lines.txt')
movie_lines = f.readlines()
f.close()
# словарь с метками фраз и самими фразами и наборот
lines = dict()
for i in range(len(movie_lines)):
    smth = movie_lines[i].split(' +++$+++ ')
    lines[smth[0]] = smth[-1]
movie_lines = ''
inv_lines = {value: key for key, value in lines.items()}

# выводит диалог №1238
# for line in conversations[1238]:
#     print(lines[line])
text = ''
for i in main_lines:
    text += lines[i]
text = text.replace('\n', ' ')
