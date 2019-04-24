import pickle
import sys

# from bayes import x

# w_features = x

# print("x =",x)

# take input
s = sys.argv[1]


x = 0

with open('results_features.pkl', 'rb') as input:
    x = pickle.load(input)

w_features = x.keys()

def extract_features(document):
    document_words = set(document)
    features = {}
    for word in w_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

with open('results_classifier.pkl', 'rb') as input:
    classifierx = pickle.load(input)
    # print("FINAL RESULTS = \n")
    # review = "00 y/o potty humor from 00 somethings does not a comedy make....: saw this movie and felt compelled to warn people not to waste 000 agonizing minutes of their lives. in a nutshell, i have heard many more clever jokes and 'one-liners' watching king of queens on cable.....seriously folks, it's that bad....the bad jokes and the 00 references to small jewish penises got old real quick. thought i would always be a sandler fan but he clearly, adam was in need of some rent money and jumped on this script for the cash and ran!why else would the plot line include seth rogan writing for him??? to put things into perspective, this film made bruno look like casablanca!!"
    print(classifierx.classify(extract_features(s.split())))
    sys.stdout.flush()

# print("THE END : ")
