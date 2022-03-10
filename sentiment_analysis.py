from textblob import TextBlob
from newspaper import Article

url = "The url of the article should be given"
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity

if sentiment > 0:
    print(f"The article is positive with {sentiment} quotient.")
else:
    print(f"The article is negative with: {sentiment} quotient. ")
