
with open('file_name', 'r') as inf:
    s1 = inf.readline()         # чтение первой строки в файле
    s2 = inf.readline()         # Чтение второй строки в файле
    s = inf.readline().strip()  # удаление служебных символов в троке

#import os
#    os.path.join('.', 'dirname', 'filename') # указание полного пути к файлу ./dirname/filename