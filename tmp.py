import os
import re
# milu_base = '/home/qianshan/Exp/Milu/benchmark_32_1/'
# files = os.popen('ls ' + milu_base).readlines()
# for file in files:
#     substr = file.split('.')
#     # os.system('cd ' + milu_base + '\n' +
#     #          'mv ' + file + '\ ' + substr[0] + '.c')
#     src = ''
#     src += substr[0] + '.'
#     src += substr[1] + '.'
#     src += substr[2] + '.'
#
#     src = milu_base + src + '* '
#     dest = milu_base + substr[0] + '.c'
#     print('mv ' + src + ' ' + dest)
#     os.system('mv ' +  + milu_base + substr[0] + '.c')
#
#
# status = os.system('ls ')
# print(status)

# error = 'error1.txt'
# file = '/tmp/test1.csv'
#
# file = open(file, "rb").readlines()
# out = []
# for line in file:
#     ori = (bytes.decode(line)).split('\t')
#     if line.__contains__(b'ERROR (parsing failed)') or ori[11].__contains__('ERROR (parsing failed)'):
#         out.append(ori[0].split('/')[1] + '\n')
#
# rst_base = '/tmp/'
# with open(rst_base + error, "wb") as rst_file:
#     for row in out:
#         rst_file.write(str.encode(row))
#
# rst_file.close()

base = '/home/qianshan/Documents/lazyExp-32_1/milu/ldv-rest-pnslazy/'

files = os.popen('ls ' + base).readlines()
# error_list = set()
# for name in files:
#     path = base + name.split('\n')[0]
#     file = open(path, "rb").readlines()
#     data = []
#     for line in file:
#         data = bytes.decode(line).split('\t')
#         if data[11].upper().__contains__('ERROR'):
#             error_list.add(data[0].split('/')[1])
#
# rst_base = '/tmp/'
# with open(rst_base + 'parsing.txt', "wb") as rst_file:
#     for item in error_list:
#         rst_file.write(str.encode(item + '\n'))
#
# rst_file.close()

error_list = []
list = open('/tmp/parsing.txt', "rb").readlines()
for i in list:
    error_list.append(bytes.decode(i).split('\n')[0])

# file = open(file, "rb").readlines()

for name in files:
    path = base + name.split('\n')[0]
    file = open(path, "rb").readlines()
    cache = []

    for line in file:
        Error = False
        for item in error_list:
            if bytes.decode(line).__contains__(item):
                Error = True
                break
        if not Error:
            cache.append(line)

    path_new = path + '.csv'
    with open(path_new, "wb") as rst_file:
        for item in cache:
            rst_file.write(item)