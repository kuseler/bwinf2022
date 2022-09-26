with open("fahrradwerkstatt0.txt") as f:
    a = f.readlines()


arr = []
for i in a:
    arr.append([int(i) for i in i.split()])
