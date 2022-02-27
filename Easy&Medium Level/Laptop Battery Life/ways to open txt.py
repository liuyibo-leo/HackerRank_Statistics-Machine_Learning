data = open('Laptop Battery Life  Training Data.txt', 'r')
dataFile=data.readlines()
data.close()

X = []
y = []
for i in dataFile:
    line = i.strip() #remove before and after space
    line = line.split(',')
    X.append(float(line[0]))
    y.append(float(line[1]))
