from flask import Flask, render_template, request, jsonify
import pandas as pd
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Initialize Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Load the Kaggle dataset (assuming you have it saved locally)
def load_movies_data():
    df = pd.read_csv('IMDb_movies.csv')
    return df

# Function to index the dataset into Elasticsearch
def store_data_in_elasticsearch():
    df = load_movies_data()
    
    # Index each movie into Elasticsearch
    for _, row in df.iterrows():
        doc = {
            'title': row['title'],
            'genre': row['genre'],
            'description': row['description']
        }
        # Store movie data in Elasticsearch (index: "movies", document ID: movie title)
        es.index(index='movies', id=row['title'].lower(), body=doc)

# Function to search movies by title in Elasticsearch
def search_elasticsearch(query):
    search_body = {
        "query": {
            "match": {
                "title": query
            }
        }
    }
    res = es.search(index="movies", body=search_body)
    return res['hits']['hits']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        
        # Search the dataset in Elasticsearch
        results = search_elasticsearch(query)
        return render_template('index.html', results=results, query=query)
    
    return render_template('index.html')

if __name__ == '__main__':
    # Store data in Elasticsearch when the application starts (indexing the dataset)
    store_data_in_elasticsearch()
    app.run(debug=True)