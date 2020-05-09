# до 32 строки идет обработка текстов с диалогами из фильмов
f = open('all_comands/texts/movie_conversations.txt')
conversations = f.readlines()
f.close()
# словарь, в котором ключ - это первая фраза, а значение - следующая за ней (фразы в виде меток)
line_after_line = dict()
# сценарии диалогов с метками
for i in range(len(conversations)):
    conversations[i] = eval(
        conversations[i].split(' +++$+++ ')[-1][:-1])  # сценарий диалога это список и вот его можно достать из файла
    for j in range(len(conversations[i]) - 1):
        line_after_line[conversations[i][j]] = conversations[i][j + 1]  # добавляем данные в словарь
main_lines = line_after_line.keys()  # id реплик, на которые можно ответить
f = open('all_comands/texts/movie_lines.txt')
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

movie_text = ''
for i in main_lines:
    movie_text += lines[i]

f = open('all_comands/texts/Architecture of London.txt')
arch_lines = f.readlines()
f.close()
f = open('all_comands/texts/slime molds.txt')
slime_lines = f.readlines()
f.close()
f = open('all_comands/texts/Look What You Made Me Do.txt')
tay_lines = f.readlines()
f.close()


def text(some_lines):
    txt = ''
    for line in some_lines:
        if line:
            txt += ' ' + line
    return txt


london_text = text(arch_lines)
slime_text = text(slime_lines)
tay_text = text(tay_lines)
