from glob import glob
selector = "ldv-rest-pnslazy"
isTotal = False

rst_base = "/home/qianshan/Documents/实验结果/"
file = rst_base + "benchmark-noFinisedSet-459.csv"
file_content = []
file_content = open(file, "rb").readlines()
filter = "/home/qianshan/Exp/Milu/filter-strong-lclang3.8.txt"
filter_content = open(filter, "rb").readlines()
count = 0
contents = []
for line in file_content:
    ori = (bytes.decode(line)).split(',')
    if ori[0].__len__() == 0 or ori[1].__contains__("All") or ori[0].__contains__("Total"):
        contents.append(line)
        continue
    tar = str.encode(ori[0].split('/')[1])
    for name in filter_content:
        if name.__contains__(tar):
            # ori[0] = ''
            # contents.append(line)
            line = ''
            count = count + 1
            break
        # else:
            # contents.append(line)
        #     break
    if line.__len__() > 2:
        contents.append(line)
    sub_str = ''
    # for j in range(0, ori.__len__() - 1):
    #     sub_str += str(ori[j]) + '\t'
    # sub_str += str(ori[j + 1]) + '\t'
    # contents.append(str.encode(sub_str))

with open(rst_base + "rest225.txt", "wb") as rst_file:
    for row in contents:
        rst_file.write(row)

rst_file.close()
# rst_base = "/Users/yuqianshan/null/results-xml/z3/sum-diskperf/"
