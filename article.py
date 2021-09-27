import nltk
from newspaper import Article

#Telecharger l'article
url="https://www.frandroid.com/guide-dachat/386688_quels-smartphone-samsung-choisir-parmi-les-differentes-gammes-galaxy"
article = Article(url)
article.download()
article.parse()

# Acceder au titre de l'article
print(article.title)
# Acceder au titre de l'article
print(article.authors)
# Acceder au titre de l'article
print(article.publish_date)
# Acceder au texte
print(article.text)