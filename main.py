import os
from langchain_community.llms import CTransformers
from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM, AutoTokenizer
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain import FewShotPromptTemplate
import os
from qdrant import init_client, search
# from langchain.llms import CTransformers
import torch

MODEL_PATH = 'model/mistral-7b-instruct-v0.1.Q5_K_S.gguf'

if __name__ == '__main__':
    llm = CTransformers(model=MODEL_PATH, model_type="mistral",
                        gpu_layers=50)
    client = init_client()
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
    context = "Tu es  adjoint à la ville d'Issy-les-Moulineaux. Réponds à la question en Français: "
    # prompt = "Quelle est le prochain évennement à issy les Moulineaux?"
    response = "Cette rencontre proposée par l'association A3N vous donnera des informations sur la préparation et le soutien de votre allaitement. Par Myriam Lafage, consultante en lactation."
    template = """Question: {question}
    Answer: Let's think step by step."""
    search(client, "an event about Cybersecurity", date)

    example_template = """
    User: {query}
    AI: {answer}
    """
    # example_prompt = PromptTemplate(
    #     input_variables=['query', 'answer'],
    #     template=example_template
    # )
    # Define the prefix to introduce the context of the conversation examples
    prefix = """ You are an helpfull AI assistant focused on the city of Issy les Moulineaux.
    The assistant is typically informative and encouraging, providing insightful and motivational responses to the user's questions about Events in Issy les Moulineaux. Here are some examples:
    """

    example_prompt = PromptTemplate(
        input_variables=['query', 'answer'],
        template=example_template
    )

    suffix = """
    User: {query}
    AI: """

    query = "28/03/2024 What's the next event in issy les Moulineaux"
    # date = query[:11]
    # query = query[11:]
    # print(llm.invoke(few_shot_prompt_template.format(query=query)))

    # question= "Who won the FIFA World Cup in the year 1994?"
    # prompt = PromptTemplate.from_template(template)
    # llm_chain = LLMChain(prompt=prompt, llm=llm)
    # print(llm_chain.invoke(question))

    # config = {
    #     "max_new_tokens": 2048,
    #     "context_length": 4096,
    #     "repetition_penalty": 1.1,
    #     "temperature": 0.5,
    #     "top_k": 50,
    #     "top_p": 0.9,
    #     "stream": True,
    #     "threads": int(os.cpu_count() / 2)
    # }
    # llm = CTransformers(model=MODEL_PATH,
    #                     config=config)
    # tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")

    # print(llm(context + "Quelle est le prochain évennement à issy les Moulineaux? Réponse: Cette rencontre proposée par l'association A3N vous donnera des informations sur la préparation et le soutien de votre allaitement. Par Myriam Lafage, consultante en lactation."))
    # output = llm.generate(
    #     prompts=prompt,
    #     context=context,
    #     response=response,
    #     max_new_tokens=50,
    #     temperature=0.7,
    #     top_k=50,
    #     top_p=0.95
    # )
    # print(output)
