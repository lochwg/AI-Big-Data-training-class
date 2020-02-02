import jieba

sentence = "工欲善其事，必先利其器，寫Python程式，\
第一步就要先建置編寫的環境 - 賴天應"
print("Input："), sentence
words = jieba.cut(sentence, cut_all = False)
print ("Output 精確模式 Full Mode：")

for word in words:
     print(word)