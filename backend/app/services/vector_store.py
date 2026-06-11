from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)


class VectorStore:

    def __init__(self):

        self.client = QdrantClient(
            ":memory:"
        )

        self.collection_name = "webmind"

        collections = [
            collection.name
            for collection in self.client.get_collections().collections
        ]

        if self.collection_name not in collections:

            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=768,
                    distance=Distance.COSINE
                )
            )

    def add_vector(
        self,
        vector,
        text,
        point_id
    ):

        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                PointStruct(
                    id=point_id,
                    vector=vector,
                    payload={
                        "text": text
                    }
                )
            ]
        )

    def search(
        self,
        query_vector
    ):

        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=3
        )

        return results