#coding=utf-8
import chardet
import DBUtils as dbu
import FileUtils as ft
import  jieba
import snownlp
import SnowNLP_Senti as snS
import File_simple_senti as fs

def classify_snowNLP():
    snS.selectAndCut()
def classify_simple():
    fs.selectAndCut()

if __name__ == "__main__":
    classify_simple()