# Video Retrieval-Augmented Generation (RAG)

Video RAG Prototype project.

Vector DB:

1. Qdrant

```
docker run -p 6333:6333 -p 6334:6334 \
    -v $(pwd)/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant
```
