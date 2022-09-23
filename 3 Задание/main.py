import os

for _ in range(1000):
    answer = input("Введите название каталога: ")
    if os.path.exists(answer):
        tree = os.walk(answer)
        break

print('Список всех каталогов и файлов в этом и ниже стоящих каталогах: ')
if tree is not None:
    for i in tree:
        print(i)
        for j in list(i)[2]:
            if int(j.find('.txt')) + 1:
                os.remove(list(i)[0] + '/' + j)
            if int(j.find('.docx')) + 1:
                continue
            if int(j.find('.doc')) + 1:
                os.rename(list(i)[0] + '/' + j, list(i)[0] + '/' + j + 'x')


if answer is not None:
    if os.path.exists(answer):
        tree = os.walk(answer)

print('Повторный вывод: ')
for i in tree:
    print(i)
