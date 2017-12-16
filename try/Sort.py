#coding=utf-8
def Sort(list,k):
    dic = {}
    for i in list :
        if i == '':
            continue
        if i not in dic:
            dic[i] = 0
        dic[i] +=1
    newDic = {}
    key = ""
    for i in range(0,k+1):
        isFirst  = True
        for i in dic:
            if isFirst:
                key = i
                isFirst = False
                continue
            if dic[key] < dic[i]:
                key = i
        newDic[key] = dic[key]
        dic.pop(key)
    return newDic

def stopwordsDel(stopwords , list):
    resultL = []
    for w in list:
        if w.strip() in stopwords:
            continue
        resultL.append(w)
    return resultL

