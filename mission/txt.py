number = [70,60,55,75,95,90,80,100]

f = open("D:\Github\-Babo\mission\미션.txt",'w')
for i in number:
    data = str(i)
    f.write(data+'\n')
f.close()

f = open("D:\Github\-Babo\mission\미션.txt",'r')
total = 0
for line in f:
    total +=int(line)
f.close

f = open("D:\Github\-Babo\mission\미션result.txt",'w')
f.write(str(total))
f.close()


