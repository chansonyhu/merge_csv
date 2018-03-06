from glob import glob
selector = "ldv-rest-pnslazy"
isTotal = True

rst_base = "/Users/yuqianshan/LabDrive/Seafile/My Library/LazyExpansion/lazyExp-32_1/milu/" \
           + selector + "/"
# rst_base = "/Users/yuqianshan/null/results-xml/z3/sum-diskperf/"
paths = glob(rst_base + selector + "_*")
sum_paths = []
for i in range(0, 6):
    pattern = selector + "_" + i.__str__()
    for tar in paths:
        if tar.__contains__(pattern):
            sum_paths.append(tar)
            break

sum_files = []
for path in sum_paths:
    if path == rst_base + selector + "_all.txt":
        continue
    sum_files.append(open(path, "rb").readlines())

rst = []

for i in range(0, 3):
    rst.append(sum_files[1][i])

flag = False
for i in range(3, len(sum_files[0])):
    flag = False
    sub = ['', 0, 0, 0, 0, 0, 0, 0,
           '', 0, 0, 0, 0, 0, 0]

    for file in sum_files:
        if not flag: #第一行特殊处理
            ori = (bytes.decode(file[i])).split('\t')
            ori.insert(3, '-')
            ori_str = ""
            # for sub in ori:
            #     ori_str += sub + '\t'
            for j in range(0, ori.__len__() - 1):
                ori_str += ori[j] + '\t'
            ori_str += ori[j + 1]
            if not isTotal:
                rst.append(str.encode(ori_str))
            flag = True
            # TODO 累加
            sub[0] = (ori[0].split('/'))[1]  # file name
            # sub[1] = int(ori[1])  # All Call
            # sub[2] = int(ori[2])  # Heap Size (MB)
            # sub[4] = int(ori[4])  # PathLens
            # sub[5] = int(ori[5])  # SP
            # sub[6] = float(ori[6])  # cputimes (s)
            # sub[7] = int(ori[7])  # holes
            # sub[8] = 'false'
            # if ori[8].upper().__contains__('TRUE'):  # lazy status
            #     sub[8] = 'true'
            # sub[9] = int(ori[9])  # memUsage
            # if ori[10] != '':
            #     sub[10] = float(ori[10])  # ref times (s)
            # sub[11] = int(ori[11])  # refinements
            # sub[12] = 0
            # if ori[12].upper().__contains__('FALSE'):  # status
            #     sub[12] += 1
            # elif ori[12].upper().__contains__('ERROR'):
            #     sub[12] = -1
            # sub[13] = float(ori[13])  # total (s)
            # sub[14] = float(ori[14])  # walltimes (s)
        else:
            ori = (bytes.decode(file[i])).split('\t')
            if not isTotal:
                rst.append(file[i])
            # TODO 累加
            # sub[0] = (ori[0].split('/'))[1]  # file name
            if ori[1] != '':
                sub[1] += int(ori[1])  # All Call
            if ori[2] != '':
                sub[2] += int(ori[2])  # Heap Size (MB)
            if ori.__len__() <= 14 and (ori[10].upper().__contains__('TRUE') or ori[10].upper().__contains__('FALSE')):
                ori.insert(3, '0')
            if ori[3] != '':
                sub[3] += int(ori[3])  # LastVersion Hit
            if ori[4] != '':
                sub[4] += int(ori[4])  # PathLens
            if ori[5] != '':
                sub[5] += int(ori[5])  # SP
            sub[6] += float(ori[6])  # cputimes (s)
            if ori[7] != '':
                sub[7] += int(ori[7])  # holes
            if ori[8].upper().__contains__('TRUE'):  # lazy status
                sub[8] = 'true'
            sub[9] += int(ori[9])  # memUsage

            if ori[11].upper().__contains__('TRUE') or ori[11].upper().__contains__('FALSE'):
                ori.insert(10, '0')
                sub[10] += float(ori[10])
            else:
                if ori[10] != '':
                    sub[10] += float(ori[10])  # ref times (s)

            if ori[11] != '':
                sub[11] += int(ori[11])  # refinements
            if ori[12].upper().__contains__('FALSE'):  # status
                sub[12] += 1
            elif ori[12].upper().__contains__('ERROR'):
                sub[12] = -1
            if ori[13] != '':
                sub[13] += float(ori[13])  # total (s)
            sub[14] += float(ori[14])  # walltimes (s)
    #TODO apppend累加行
    sub_str = ''
    for j in range(0, sub.__len__() - 1):
        sub_str += str(sub[j]) + '\t'
    sub_str += str(sub[j + 1]) + '\n'
    rst.append(str.encode(sub_str))

with open(rst_base + "rst_" + selector + "_all.txt", "wb") as rst_file:
    for row in rst:
        rst_file.write(row)

rst_file.close()

