# IMDb Movie Search using Flask and Elasticsearch

This Flask web application allows users to search for movie data from the IMDb Movies Dataset (available on Kaggle) stored in an Elasticsearch index. Users can search by movie title, and the app returns relevant results with movie titles, genres, and descriptions.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Dataset](#dataset)
- [Usage](#usage)
- [Elasticsearch Setup](#elasticsearch-setup)
- [License](#license)

## Introduction
This project demonstrates how to build a Flask web application that integrates with Elasticsearch. We use the IMDb Movies Dataset to index movie data (such as titles, genres, and descriptions) into Elasticsearch. The app provides a search functionality where users can query Elasticsearch for specific movies based on their titles.

## Features
- Search movies by title using Elasticsearch.
- Results include movie title, genre, and description.
- Powered by the **IMDb Movies Dataset** from Kaggle.

## Requirements
- Python 3.x
- Flask 2.x
- Pandas
- Elasticsearch
- IMDb Movies Dataset (from Kaggle)

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/imdb-flask-elasticsearch.git
   cd imdb-flask-elasticsearch

    pip install -r requirements.txt

2. Download the IMDb Movies Dataset from Kaggle:

3. Set up Elasticsearch:

    Install and run Elasticsearch (instructions provided below).
    Dataset
    The application uses the IMDb Movies Dataset, which contains movie titles, genres, descriptions, and other metadata. You can download the dataset from Kaggle here.

    Data Fields Used:
    title: The title of the movie.
    genre: The genre(s) of the movie.
    description: A brief description of the movie.
    Usage
    Start the Flask application:

    ```python app.py
    Access the application:

    Open your browser and navigate to http://127.0.0.1:5000.
    Search for Movies:

    Enter the title of the movie you wish to search in the input field.
    The app will return matching movies with their title, genre, and description.

    Navigate to http://localhost:9200/ in your browser. You should see the Elasticsearch information.