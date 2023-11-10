# Restaurant Sentiment Analysis

An NLP project for sentiment analysis on restaurant review data using Multinomial Naive Bayes.

## Overview

This project aims to analyze sentiments in restaurant reviews using a Multinomial Naive Bayes classifier. The trained model achieves a precision of 0.89, recall of 0.88, and an F1-score of 0.88, indicating its effectiveness in sentiment classification.


## Features

- Sentiment analysis on restaurant reviews
- Multinomial Naive Bayes classification
- Precision: 0.89, Recall: 0.88, F1-score: 0.88

## confusion matrix
<img src="https://github.com/mahayasa/restaurant-review-sentiment-analysis/blob/main/image/cm.png" alt="Sample Image" width="500" height="500">


## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Docker version 24.x
- FastAPI
  
### Usage
You can use postman to try the model, make sure run your docker engine and go to project url, in my case the url is localhost using default port 80, use localhost/predict url and POST the text input

<img src="https://github.com/mahayasa/restaurant-review-sentiment-analysis/blob/main/image/negative.png" alt="Sample Image" width="500" height="500">
<img src="https://github.com/mahayasa/restaurant-review-sentiment-analysis/blob/main/image/positive.png" alt="Sample Image" width="500" height="500">

## Acknowledgments
Thanks to AssemblyAI for the tutorial : https://www.youtube.com/watch?v=h5wLuVDr0oc&list=WL&index=1 
