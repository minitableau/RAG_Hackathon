from qdrant_client import QdrantClient
from qdrant_client.http.models import *
# Distance, VectorParams, PointStruct
import pandas as pd
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')


def init_client():
    client = QdrantClient("localhost", port=6333)
    return client


def create_col(client):
    client.recreate_collection(
        collection_name="event",
        vectors_config=VectorParams(size=model.get_sentence_embedding_dimension(), distance=Distance.EUCLID),

    )


client = init_client()
create_col(client)
df = pd.read_csv("future_events_detailed_en.csv", sep=',')


def upsert(client, df):
    points = [
        PointStruct(
            id=idx,
            vector=model.encode(description).tolist(),
            payload={"date": date,
                     "description": description,
                     "titre": event,
                     },
        )
        for idx, (description, date, event) in
        enumerate(zip(df["description"].tolist(), df["date"].tolist(), df["event"].tolist()))
    ]
    client.upsert("event", points)


upsert(client, df)


def search(client, question, date):
    search_result = client.search(
        collection_name="event",
        query_vector=model.encode(question).tolist(),
        query_filter=Filter(
            must=[FieldCondition(key="date", match=MatchValue(value=date))]
        ),

        with_payload=True,
        limit=2,
    )
    return search_result
