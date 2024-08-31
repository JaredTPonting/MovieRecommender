# Movie Recommendation System
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Status](https://img.shields.io/badge/project--status-work--in--progress-orange)

A comprehensive movie recommendation system that leverages various machine learning techniques to provide personalized movie suggestions. The system includes both content-based and collaborative filtering approaches and integrates these methods into a hybrid model for enhanced recommendation accuracy. The recommendations are presented through an interactive web dashboard built with Plotly Dash.

## TO DO
- Make use of SQLite3, the CSVs are too large

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)

## Project Overview

This project implements a movie recommendation system using the [Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) from Kaggle. The system uses multiple recommendation algorithms to provide personalized suggestions to users. The results are presented through a web-based dashboard that allows users to input movie titles, select recommendation methods, and view the recommendations.

## Features

- **Data Preprocessing**: Cleans and processes raw movie data to prepare it for analysis.
- **Feature Engineering**: Generates new features to enhance the recommendation quality.
- **Recommendation Algorithms**:
  - **Content-Based Filtering**: Recommends movies similar to a given movie based on content features.
  - **Collaborative Filtering**: Recommends movies based on user preferences and movie popularity.
  - **Hybrid Model**: Combines content-based and collaborative filtering for improved recommendations.
- **Interactive Dashboard**: Allows users to input movie titles and select recommendation methods to get personalized movie suggestions.

## Technologies

- **Programming Languages**: Python
- **Libraries & Frameworks**:
  - **Data Processing**: Pandas, NumPy
  - **Machine Learning**: scikit-learn
  - **Web Framework**: Plotly Dash
  - **Visualization**: Plotly
- **Database**: SQLite (or use a CSV file for simplicity)
- **Development Environment**: Jupyter Notebook (for experimentation), Python scripts

