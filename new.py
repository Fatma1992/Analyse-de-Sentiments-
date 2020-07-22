# -*- coding: utf-8 -*-

import string
from collections import Counter
import re 
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

text = open('read.txt', encoding='utf-8-sig').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))


# Using word_tokenize because it's faster than split()
tokenized_words = word_tokenize(cleaned_text, "french")

stop_words = ["à", "à demi", "à peine", "à peu près", "absolument", "actuellement", "ainsi", "alors", "apparemment", "approximativement", 
              "après", "après-demain", "assez", "assurément", "au", "aucun", "aucunement", "aucuns", "aujourd’hui", "auparavant", "aussi",
              "aussitôt", "autant", "autre", "autrefois", "autrement", "avant", "avant-hier", "avec", "avoir","beaucoup", "bien", "bientôt", "bon",
              "c’", "ça", "car", "carrément", "ce", "cela", "cependant", "certainement", "certes", "ces", "ceux", "chaque", "ci", "comme", "comment", 
              "complètement", "d’", "d’abord", "dans", "davantage", "de", "début", "dedans", "dehors", "déjà", "demain", "depuis", "derechef", "des",
              "désormais", "deux", "devrait", "diablement", "divinement", "doit", "donc", "dorénavant", "dos", "droite", "drôlement", "du", "elle", "elles", 
              "en", "en vérité", "encore", "enfin", "ensuite", "entièrement", "entre-temps", "environ", "essai", "est", "et", "étaient", "état", "été", "étions", 
              "être", "eu", "extrêmement", "fait", "faites", "fois", "font", "force", "grandement", "guère", "habituellement", "haut", "hier", "hors",
              "ici", "il", "ils", "infiniment", "insuffisamment", "jadis", "jamais", "je", "j'ai", "joliment", "ka", "la", "là", "le", "les", "leur", "leurs", 
              "lol", "longtemps", "lors", "ma", "maintenant", "mais", "mdr", "même", "mes", "me", "moins", "mon", "mot", "naguère","ne", "ni", 
              "nommés", "non", "notre", "nous", "nouveaux", "nullement", "ou", "où", "oui",  "par", "parce", "parfois", "parole", "pas", "pas mal", "passablement", 
              "personne", "personnes", "peu", "peut", "peut-être", "pièce", "plupart", "plus", "plutôt", "point", "pour", "pourquoi", "précisément", "premièrement",
              "presque", "probablement", "prou", "puis", "quand", "quasi", "quasiment", "que", "quel", "quelle", "quelles", "quelque", "quelquefois", "quels", 
              "qui", "quoi", "quotidiennement", "rien", "rudement", "s’", "sa", "sans", "sans doute", "ses", "seulement", "si", "sien", "sitôt", "soit", "son",
              "sont", "soudain", "sous", "souvent", "soyez", "subitement", "suffisamment", "sur", "t’", "ta", "tandis", "tant", "tantôt", "tard", "tellement",
              "tels", "terriblement", "tes", "ton", "tôt", "totalement", "toujours", "tous", "tout", "tout à fait", "toutefois", "très", "trop", "tu", "un", "une",
              "valeur", "vers", "voie", "voient", "volontiers", "vont", "votre", "vous", "vraiment", "vraisemblablement","soudainement", "brusquement"]


# La suppression des mots vides de la liste des mots (une autre liste sans les mots vides)
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
#print (final_words)


# Lemmatization - From plural to single + Base form of a word (example better-> good)
lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)
#print (lemma_words)

import json
with open('data.txt', 'w') as outfile:
    json.dump(lemma_words, outfile)

emotion_list = []
with open('emotions.txt') as file:
    for line in file:
        words = re.split(",.?! ]+" , line)
        #print (words)
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in lemma_words:
            emotion_list.append(word, emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)


def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")


sentiment_analyse(cleaned_text)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()


# dico = {}
# with open ('emotions.txt') as f : 
    # for line in f: 
        # words = re.split (",.?! ]+" , line)
        # print (words)
        # for w in words : 
            # if dico.get (w): 
                # print (w, dico [w])
            # else : 
                # print (w, "Forme Inconnu") 

