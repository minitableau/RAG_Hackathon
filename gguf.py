import os
from langchain_community.llms import CTransformers
import os

# from langchain.llms import CTransformers
MODEL_PATH = 'model/mistral-7b-instruct-v0.1.Q5_K_S.gguf'
import torch

from qdrant import init_client, search

client = init_client()
# Define the prefix to introduce the context of the conversation examples
prefix = """ You are an helpfull AI assistant focused on the city of Issy les Moulineaux.
    The assistant is typically informative and encouraging, providing insightful and motivational responses to the user's questions about Events in Issy les Moulineaux.
    INSTRUCTIONS: Answer the users QUESTION using the DOCUMENT text above.
    Keep your answer ground in the facts of the DOCUMENT.
    If the DOCUMENT doesn’t contain the facts to answer the QUESTION return {I can't find any events that match with what you want}
    
    """

llm = CTransformers(model=MODEL_PATH, model_type="mistral",
                    gpu_layers=50, system_prompt=prefix, repetition_penalty=1.1, temperature=0, max_new_token=599)


def model_gguf(query):
    date = query[-8:]
    question = query[:-14]
    content = search(client, question, date)

    if content == []:
        prompt = f"""
        Context information is below.
        ---------------------
        Issy les Moulineaux don't provide any event on this date:
        
        ---------------------
        Given the context information and not prior knowledge, answer the query.
        Query: {question}
        Answer:
        """


    else:
        prompt = f"""
        Context information is below.
        ---------------------
        Issy les Moulineaux provide a event about :
        {content[0].payload['description']}
        ---------------------
        Given the context information and not prior knowledge, answer the query.
        Query: {question}
        Answer:
        """

    return (llm(prompt))
