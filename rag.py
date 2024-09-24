from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
import pandas as pd
import numpy as np
from langchain_community.vectorstores import Qdrant

# Connectez-vous à votre instance Qdrant locale
client = QdrantClient("localhost", port=6333)

# Récupérez la collection existante avec le nom spécifié
collection_name = "event"
collection = client.get_collection(collection_name=collection_name)

# Créez une instance Qdrant en utilisant la collection existante
db = Qdrant(collection=collection)

# Récupérez les phrases à partir de votre base de données Qdrant
phrases = db.similarity_search(query="votre requête ici", k=10)
retriever = db.as_retriever(search_type="mmr", search_kwargs={'k': 4, 'fetch_k': 20})


# Formatez les phrases
def format_phrases(phrases):
    return "\n\n".join(phrase for phrase in phrases)


prompt = hub.pull("rlm/rag-prompt")
# Passez les phrases formatées à la chaîne rag_chain
rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
)
rag_chain.invoke("prompt utilisateur")
