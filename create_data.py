import nltk
from newspaper import Article
import pandas as pd

urls=["https://www.footmercato.net/a6032949137829822881-son-role-de-consultant-son-futur-le-psg-nicolas-anelka-se-livre",
"https://fr.yahoo.com/news/julie-gayet-raison-divorce-santiago-122727027.html",
"https://www.lemonde.fr/sante/article/2021/09/27/les-nouveaux-vaccins-face-au-casse-tete-des-essais-cliniques_6096205_1651302.html",
"https://www.lemonde.fr/culture/article/2021/09/27/sur-mezzo-aux-frontieres-du-free-jazz-miles-davis-electrise-la-salle-pleyel_6096207_3246.html"]


def url_text(url):
    article = Article(url)
    article.download()
    article.parse()
    titre =article.title
    text=article.text
    auteur=article.authors
    return titre,auteur,text

texts = [url_text(url) for url in urls]

#print(texts[2])

colonnes_nom=['titre','auteur','texte']
df=pd.DataFrame(data=texts, columns=colonnes_nom)
print(df)