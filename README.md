# README: MLOps-M2-SISE

## Table of Contents

1. [Description](#description)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contribution](#contribution)
7. [Author](#author)

---

## Description

This project is an MLOps application designed to streamline the training, evaluation, and deployment of a Random Forest Classifier for predicting Iris species. It integrates a robust backend built with **FastAPI** and a user-friendly frontend developed using **Streamlit**, all orchestrated within a **Dockerized environment** for seamless deployment and scalability.

---

## Features

- **Show List of Predictions**: Users can view the predictions that have already been made by clicking the "Affichez la liste des prédictions" button. This will display the length and width of the sepals and petals that were set, along with the prediction provided by the app.

- **Flower Prediction**: Users can select the length and width of the sepals and petals. Once the flower's characteristics have been set, they can click the "Prédire et Ajouter" button. The app will then display the prediction along with its characteristics and ID, where 0 corresponds to Setosa, 1 to Versicolor, and 2 to Virginica.
---

## Project Structure

```
├── client/
│   ├── app.py              # Streamlit frontend application
│   ├── Dockerfile          # Docker configuration for the client
│   └── requirements.txt    # Python dependencies for the client
├── server/
│   ├── app.py              # FastAPI backend application
│   ├── Dockerfile          # Docker configuration for the server
│   └── requirements.txt    # Python dependencies for the server
├── docker-compose.yml      # Docker Compose configuration to orchestrate services
```

---

## Installation

To run this project on your local machine, follow these steps:

1. **Install Docker Desktop**:
   - Download and install Docker from [Docker Desktop](https://www.docker.com/products/docker-desktop/).

2. **Clone the repository**:
   ```bash
   git clone https://github.com/AntoineORUEZABALA/MLOps-M2-SISE
   ```

3. **Navigate to the project directory** and build the Docker image:
   ```bash
   cd mlops
   docker-compose up --build
   ```

4. When it's done you can access the app with this URL:
   - [Streamlit App](http://localhost:8501/)

---

You can now have fun with my app ! 🦦

## Contribution

All contributions are welcome! Here's how you can help:

1. **Fork the Project**
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit Your Changes**:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

---

## Author

This project was developed by **Antoine ORUEZABALA**, a student in the **Master 2 SISE** at the **University of Lyon 2**.

