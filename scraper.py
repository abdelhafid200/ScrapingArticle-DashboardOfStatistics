from textblob import TextBlob

# Exemple de texte
text = "C'est un excellent produit, je l'adore!"

# Analyse de sentiment
blob = TextBlob(text)

# Obtenez la polarité (positif, négatif, neutre)
polarity = blob.sentiment.polarity

if polarity > 0:
    sentiment = "positif"
elif polarity < 0:
    sentiment = "négatif"
else:
    sentiment = "neutre"

print(f"Texte : {text}")
print(f"Sentiment : {sentiment}")