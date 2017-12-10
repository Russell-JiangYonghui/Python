# coding= utf-8
from libsvm import *
from svmutil import *

y, x = svm_read_problem('/Users/mac/Desktop/svm/sh000001_1.txt')
# model = svm_train(y,x)
yt, xt = svm_read_problem('/Users/mac/Desktop/svm/sh000001_test_1.txt')
# model = svm_load_model('/Users/mac/Desktop/train.model')
model = svm_train(y, x ,'-s 4 -t 2 -c 0.8 -g 2.8 -p 0.02 -e 0.01')
# svm_save_model('/Users/mac/Desktop/train.model',model)
print('test:')
# p_label, p_acc, p_val = svm_predict(yt[200:202], xt[200:202], model)
p_label, p_acc, p_val = svm_predict(yt[:], xt[:], model)

print 'p_label:',p_label
print 'p_acc:',p_acc
print 'p_val:',p_val

cnt  = 0
sum = 0
for i,j,k in zip(p_label,yt,y):
    print i,j,k
    # continue
    sum+=1
    print sum
    if j == 0:
        print '原价为0'
        continue
    if (i - k) * (j - k) < 0:
        cnt += 1
    else:
        continue
    # print i,j,((i - j) / j) * 100,"%", i - j
    # cnt += 1
    # sum += ((i - j) / j)

print "错误率：",cnt / sum * 100