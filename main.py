import json
from flask import Flask, render_template, request, jsonify
import sqlite3
import matplotlib.pyplot as plt

app = Flask(__name__)

# Fonction pour récupérer les articles depuis la base de données
def get_articles():
    conn = sqlite3.connect('ArticleScrape.db')
    cursor = conn.cursor()
    cursor.execute('SELECT section, title, contenu, sentiment, link_section, image_section FROM articles')
    articles = cursor.fetchall()
    conn.close()
    return articles

def generate_statistics(articles):
    num_articles = len(articles)
    unique_sections = set()
    section_article_counts = {}
    sentiment_counts_by_section = {}
    sentiment_counts = {'positif': 0, 'négatif': 0, 'neutre': 0, 'None': 0}
    link_section = {}
    images_section = {}

    for article in articles:
        section = article[0]
        sentiment = article[3]
        linkS = article[4]
        imgS = article[5]

        if section not in sentiment_counts_by_section:
            sentiment_counts_by_section[section] = {'positif': 0, 'négatif': 0, 'neutre': 0, 'None': 0}
        if sentiment is None:
            sentiment = 'None'

        sentiment_counts_by_section[section][sentiment] += 1
        unique_sections.add(section)

        if section in section_article_counts:
            section_article_counts[section] += 1
        else:
            section_article_counts[section] = 1

        sentiment_counts[sentiment] += 1

        # Vérifiez si le lien a déjà été ajouté pour cette section
        if section in link_section:
            if linkS not in link_section[section]:
                link_section[section].append(linkS)
        else:
            link_section[section] = [linkS]

            # Vérifiez si l'image a déjà été ajoutée pour cette section
        if section in images_section:
            if imgS not in images_section[section]:
                images_section[section].append(imgS)
        else:
            images_section[section] = [imgS]
        

    num_sections = len(unique_sections)
    category_data = {
        'num_sections': num_sections,
        'section_article_counts': section_article_counts,
        'sentiment_counts_by_section': sentiment_counts_by_section,
        'link_section': link_section,
        'images_section': images_section
    }
    # sentiment_statistics = []
    # positive_sentiment={"name": "positif", "data": []}
    # negative_sentiment={"name": "négatif", "data": []}
    # none_sentiment={"name": "None", "data": []}
    # neutre_sentiment={"name": "neutre", "data": []}
    # for s in sentiment_counts_by_section.values():
    #     positive_sentiment['data'].append(s["positif"])
    #     negative_sentiment['data'].append(s["négatif"])
    #     none_sentiment['data'].append(s["None"])
    #     neutre_sentiment['data'].append(s["neutre"])
    
    # positive_sentiment['data'] = json.dumps(positive_sentiment['data'])
    # negative_sentiment['data'] = json.dumps(negative_sentiment['data'])
    # none_sentiment['data'] = json.dumps(none_sentiment['data'])
    # neutre_sentiment['data'] = json.dumps(neutre_sentiment['data'])
    
    # sentiment_statistics.append(positive_sentiment)
    # sentiment_statistics.append(negative_sentiment)
    # sentiment_statistics.append(none_sentiment)
    # sentiment_statistics.append(neutre_sentiment)

    sentiment_statistics = []
    section_names = []
    

    sentiments = ["positif", "négatif", "None", "neutre"]

    for sentiment in sentiments:
        data = {"name": sentiment, "data": []}
        for section_name, s in sentiment_counts_by_section.items():
            data['data'].append(s[sentiment])
        data['data'] = json.dumps(data['data'])
        sentiment_statistics.append(data)

    for section_name, s in sentiment_counts_by_section.items():
            section_names.append(section_name)




    return num_articles, num_sections, section_article_counts, sentiment_counts, sentiment_counts_by_section, link_section, images_section, category_data,sentiment_statistics, section_names


# Création de graphiques avec Matplotlib
# Par exemple, un histogramme du nombre d'articles par section
# sections = section_article_counts.keys()
# article_counts = section_article_counts.values()

# # Création de l'histogramme
# plt.bar(sections, article_counts)
# plt.xlabel('Section')
# plt.ylabel('Nombre d\'articles')
# plt.title('Nombre d\'articles par section')
# plt.xticks(rotation=45)
# plt.savefig('static/section_histogram.png')  # Sauvegarde le graphique comme une image

@app.route('/Dashboard')
def dashboard():
    articles = get_articles()
    num_articles, num_sections, section_article_counts, sentiment_counts, sentiment_counts_by_section, link_section, images_section, category_data,sentiment_statistics, section_names= generate_statistics(articles)    
    return render_template(
        'dash.html.jinja',
        articlesAPP=articles, 
        num_articles=num_articles,
        num_sections=num_sections,
        section_article_counts=section_article_counts, 
        sentiment_counts=sentiment_counts,
        sentiment_counts_by_section = sentiment_counts_by_section, 
        link_section = link_section, 
        images_section = images_section, 
        category_data = category_data,
        sentiment_statistics = sentiment_statistics,
        section_names = section_names,
                
    )


# @app.route('/statistics', methods=['GET'])
# def update_statistics():
#     articles = get_articles()
#     num_articles, num_sections, section_article_counts, sentiment_counts, link_section, images_section = generate_statistics(articles)
#     return jsonify({
#         'num_articles': num_articles,
#         'num_sections': num_sections,
#         'sentiment_counts': sentiment_counts,
#         'link_section' : link_section,
#         'images_section' : images_section
#     })




if __name__ == '__main__':
    app.run(debug=True)
