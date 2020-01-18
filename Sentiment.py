import nltk
from textblob import TextBlob

#take input and give its sentiment analysis 
#-1 means extreme negative and 1 means positive 0 is neutral
text=input("text:")
obj=TextBlob(text)
polarity = obj.sentiment.polarity
print(polarity)