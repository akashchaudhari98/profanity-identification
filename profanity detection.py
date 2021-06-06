from typing import List
from nltk.tokenize import sent_tokenize
import re
import joblib
import time
from collections import Counter

class profanity:
    ''' cheaks for pronaity in the passes text'''
    def __init__(self):
        pass
        # self.vectorizer = joblib.load("model/vectorizer.joblib")
        # self.model = joblib.load("model/model.joblib")
        #self.sentences = self.book2sentece()
    
    # def book2sentence(self,data):
    #     with open(self.book) as file:
    #         data = file.read()
    #     sentences = sent_tokenize(data)
    #     return sentences
    
    # def cheak_value(self):
    #     profanity_count = 0
    #     profanity_sentences = []

    #     for line in self.sentences:
    #         line = re.sub(r'\W+', ' ', line)
    #         vectorized = self.vectorizer.transform([line])
    #         pred = self.model.predict(vectorized)
    #         if pred == 1:
    #             profanity_count = profanity_count + 1
    #             profanity_sentences.append(line)

    #     return profanity_count/len(self.sentences),profanity_sentences        
    
    def profanity_cheak(self,text):
        ''' returns dictionary of swear words and their counts'''
        word_list = "D:/projects/ZInc/Explicit language identification/swearwords.txt"
        
        count = 0
        start = time.time()
        with open(word_list) as words:
            words = words.readlines()
        words = [x.strip() for x in words]

        text = re.sub(r'\W+', ' ', text)
        list_ = []
        for word in text.split(" "):
            if word in words:
                list_.append(word)
        dict = Counter(list_)
        print("time required: ", time.time()- start)
        
        return dict
    


if __name__ == "__main__":
    book = "what the fuck is wrong with you david, why did you go back to that fucking bastard you bitch ?.what the fuck is wrong with you david, why did you go back to that fucking bastard you bitch ? "
    
        
    pro = profanity()
    x = pro.profanity_cheak(book)
    print(x)


