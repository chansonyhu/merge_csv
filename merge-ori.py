from glob import glob
selector = "ldv-rest-ori"
isTotal = True

rst_base = "/home/qianshan/Documents/lazyExp-32_1/milu/" + selector + "/"
# rst_base = "/Users/yuqianshan/null/results-xml/z3/sum-diskperf/"
paths = glob(rst_base + selector + "_*")
sum_paths = []
for i in range(0, 5):
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
    sub = ['', 0, 0, 0, 0, 0, 0,
           '', 0, 0, 0, '', 0, 0]

    for file in sum_files:
        if not flag: #第一行特殊处理
            ori = (bytes.decode(file[i])).split('\t')
            # ori.insert(4, '-')
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
            sub[1] = int(ori[1])  # All Call
            sub[2] = int(ori[2])  # Heap Size (MB)
            # sub[3] = int(ori[3])  # LastVersion Hit

            sub[3] = int(ori[3])  # PathLens
            sub[4] = int(ori[4])  # SP
            sub[5] = float(ori[5])  # cputimes (s)
            sub[6] = int(ori[6])  # holes
            sub[7] = 'false'
            if ori[7].upper() == 'TRUE':  # lazy status
                sub[7] = 'true'
            sub[8] = int(ori[8])  # memUsage
            if ori[9] != '':
                sub[9] = float(ori[9])  # ref times (s)
            sub[10] = int(ori[10])  # refinements
            sub[11] = 0
            if ori[11].upper() == 'FALSE':  # status
                sub[11] += 1
            elif ori[11].upper().__contains__('ERROR'):
                sub[11] = -1
            sub[12] = float(ori[12])  # total (s)
            sub[13] = float(ori[13])  # walltimes (s)
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
            # if ori[3] != '':
            #    sub[3] += int(ori[3])  # LastVersion Hit
            if ori[3] != '':
                sub[3] += int(ori[3])  # PathLens
            if ori[4] != '':
                sub[4] += int(ori[4])  # SP
            sub[5] += float(ori[5])  # cputimes (s)
            if ori[6] != '':
                sub[6] += int(ori[6])  # holes
            if ori[7].upper() == 'TRUE':  # lazy status
                sub[7] = 'true'
            sub[8] += int(ori[8])  # memUsage
            if ori[9] != '':
                sub[9] += float(ori[9])  # ref times (s)
            if ori[10] != '':
                sub[10] += int(ori[10])  # refinements
            if ori[11].upper() == 'FALSE':  # status
                sub[11] += 1
            elif ori[11].upper().__contains__('ERROR'):
                sub[11] = -1
            if ori[12] != '':
                sub[12] += float(ori[12])  # total (s)
            sub[13] += float(ori[13])  # walltimes (s)
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

