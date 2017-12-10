# coding = utf-8
import chardet
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# for i in range (1,100):
filename = '/Users/mac/Desktop/BosonNLP_sentiment_score.txt'
print filename
file = open(filename,'r')
while 1:
    line = file.readline()
    type = chardet.detect(line)
    text1 = line.decode(type["encoding"])
    print text1