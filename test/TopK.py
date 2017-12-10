# coding=utf-8
from svm import *
from svmutil import *
#
# y, x = [1, -1], [{1: 1, 2: 1}, {1: -1, 2: -1}]
# prob = svm_problem(y, x)
# param = svm_parameter('-t 0 -c 4 -b 1')
# model = svm_train(prob, param)
# yt = [1]
# xt = [{1: 1, 2: 1}]
# p_label, p_acc, p_val = svm_predict(yt, xt, model)
# print(p_label)

import os
import sys

# os.chdir('E:\machine_learning\machine_learning\SVM\libsvm-3.18\python')
from svmutil import *

y, x = svm_read_problem("sources/lkagain")
m = svm_train(y[:275], x[:275], '-c 5')

y, x = svm_read_problem('../lk2.txt')
p_label, p_acc, p_val = svm_predict(y[0:], x[0:], m)
print p_label
print p_acc
print p_val