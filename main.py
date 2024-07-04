#Importations des librairies nécessaires
import pandas as pd
import requests
import random
from fastapi import FastAPI
from typing import List, Dict
from typing import Union
import random

#Télécharge le fichier csv contenant les questions du questionnaire
url = "https://raw.githubusercontent.com/phbarbe/inclusiveness-fast-api/main/Questionnaire.csv?token=GHSAT0AAAAAACTW6MUMAEKFKYXF3GP6HWW2ZUGRKDQ"
r = requests.get(url)

df_questionnaire = pd.read_csv(url, sep=";")
df_questionnaire.head()

#transforme le dataframe en dictionnaire

quiz = df_questionnaire.to_dict('index')
quiz

#Tire au sort 20 questions du questionnaire


def obtenir_20_questions(quiz):
    if len(quiz) < 20:
        raise ValueError("La liste des questions doit contenir au moins 20 questions.")
    # Convert the dictionary keys to a list before sampling
    return random.sample(list(quiz.keys()), 20)  

# Obtenir 20 questions aléatoires
questions_aleatoires = obtenir_20_questions(quiz)

# Afficher les 20 questions aléatoires
for question_key in questions_aleatoires:
    print(quiz[question_key])  # Access the question details using the key



app = FastAPI()

def obtenir_20_questions(quiz: Dict):
    if len(quiz) < 20:
        raise ValueError("La liste des questions doit contenir au moins 20 questions.")
    return random.sample(list(quiz.values()), 20)

@app.get("/", response_model=List[Dict])
def lire_questions():
    try:
        questions = obtenir_20_questions(quiz)
        return questions
    except ValueError as e:
        return {"error": str(e)}


                