from datetime import time


fileForRead = open('n_log1.txt', 'r')
fileForOut = open('out1.txt', 'w')
counter = 0
listTimestampOfLines = []
substring1 = 'A00000000002'
substring2 = 'ON_LINE-'

listLinesOfFileLog = fileForRead.readlines()

for line in listLinesOfFileLog:
    if line.find(substring1) + 1 and line.find(substring2) + 1:
        if line.find(substring1) < line.find(substring2):
            fileForOut.write(line)
            counter += 1
            listTimestampOfLines.append(line.split(' [')[0])

print('Количество строк в файле out1.txt: ' + str(counter))

for item in listTimestampOfLines:
    print(time(int(item.split(':')[0]), int(item.split(':')[1]), int(item[6:7]), int(item.split(',')[1] + '000')))






































# with open('out1.txt') as f:
#    count = sum(1 for _ in f)


