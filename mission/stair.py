i = 0

for i in range (21):
    temp = ""
    for j in range (21 -i):
         temp = temp + " "
    for j in range (i):
        temp = temp + "*"
    print(temp)

