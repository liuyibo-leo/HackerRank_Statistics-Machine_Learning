# Enter your code here. Read input from STDIN. Print output to STDOUT

def mean(dataList):
    Mean = sum(dataList)/len(dataList)
    return Mean

def variance(dataList):
    Mean = mean(dataList)
    Variance = sum([(i - Mean)**2 for i in dataList])
    return Variance

def cov(dataList_One, dataList_Two):
    Cov = sum([(dataList_One[i] - mean(dataList_One))*(dataList_Two[i] - mean(dataList_Two)) for i in range(len(dataList_One))])
    return Cov

physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

slop = cov(physics, history) / variance(physics)
bias = mean(history) - slop*mean(physics)

PredictedResult = slop*10 + bias
print(round(PredictedResult, 1))
