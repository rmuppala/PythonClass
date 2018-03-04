from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
import re

#read the cancer details
infile = open('cancer.txt','r', encoding="utf-8")
text = infile.read();


#tokenize all the words
lwords = word_tokenize(text.lower())
words = list()
#apply Lemmatization
lem = WordNetLemmatizer()
for word in lwords:
  words.append(word)

#generage bigrams
bgs = nltk.bigrams(words)

# findout the frequency of the bigrams
fdist = nltk.FreqDist(bgs)
freq = dict()
for k,v in fdist.items():
    key = k[0] + ' '+ k[1]
    #print( key,v)
    freq[key] = v #create dictionary bigram and repeating frequency

#sort in reverse to find the most repeating bigram
slist = sorted(freq, key=freq.__getitem__, reverse=True)

#print top 5 most repeating bigrams
print("Most repeating bigrams : ")
for i in range(0,5):
 print(slist[i])

sentences = sent_tokenize(text)

summary = ""

print("\nSummary of sentenses got most repeating bigrams \n ")


for i in range(0, len(sentences)):
    if (slist[0] in sentences[i].lower() or slist[1] in sentences[i].lower() or slist[2] in sentences[i].lower() or
        slist[3] in sentences[i].lower() or slist[4] in sentences[i].lower()) :
        summary = summary + sentences[i]

print(summary)
