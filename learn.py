# import pandas as pd
import re

dictionary = {}
file_name = "test.ft.txt" #text file after extracting the main file, make sure you have it in the same folder

class Word:
    """
    stores metrics related to a word
    positive : number of times the word resulted in a positive outcome so far.
    negative : number of times the word resulted in a negative outcome so far.
    total_occurances : number of times the word has been encountered so far.
    """
    def __init__(self,word = 0, positive = 0, negative = 0, neutral = 0, total_occurances = 0, positivity = 0, negativity = 0):
        self.word = word
        self.positive = positive
        self.negative = negative
        self.neutral =  neutral
        self.total_occurances =total_occurances
        self.positivity = positivity
        self.negativity = negativity
    
    def calculate_positivity(self):
        return self.positive/self.total_occurances

    def calculate_negativity(self):
        return self.negative/self.total_occurances
    
    # def word_score(self):
    #     if positivity(self) > negativity(self):
    #         return "+"
    #     else:
    #         return "-"

def extract_words(sentence):
    return re.findall(r'\w+', sentence) 

def learn(word, score):
    """
    gains information from each tuple present in the dataset and adds the same to our dictionary
    """
    if not word in dictionary:
        dictionary[word] = Word(word)
    
    dictionary[word].total_occurances += 1
    
    if score == "__label__1":
        dictionary[word].negative += 1
    else:
        dictionary[word].positive += 1
    dictionary[word].positivity = dictionary[word].calculate_positivity()
    dictionary[word].negativity = dictionary[word].calculate_negativity()




def read_data(file_name):
    with open(file_name, encoding = 'utf-8') as f:
        for line in f:
            review = extract_words(line)
            score = review[0]
            sentence = review[1:]
            for word in sentence:
                learn(word, score)

def compute_sentiment(file_name):
    correct_outcome = 0 
    total_outcome = 0
    total_positivity, total_negativity = 0, 0
    with open(file_name, encoding = "utf-8") as f:
        for line in f:
            review = extract_words(line)
            score = review[0]
            sentence = review[1:]
            for word in sentence:
                total_negativity += dictionary[word].negativity
                total_positivity += dictionary[word].positivity
            if (total_negativity > total_positivity and score == "__label__1") or (total_negativity < total_positivity and score == "__label__2"):
                #result is negative
                correct_outcome += 1
            total_outcome += 1
        print("precision = ", correct_outcome/total_outcome)


# def demo():
#     import re
#         text = 'The quick brown\nfox jumps*over the lazy dog.'
#         re.split('; |, |\*|\n',a)

read_data(file_name)
with open("dictionary_contents.txt", 'w', encoding = "utf-8",) as f:
    for value in dictionary.values():
        f.write(str(value.word) + " " + str(value.positivity) + " " + str(value.negativity) + " " + str(value.total_occurances) + "\n")
compute_sentiment(file_name)
