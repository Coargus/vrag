from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def read_course_transcripts(path: str):
    loader = TextLoader(path)
    return loader.load()


def text_splitter(docs: list, chunk_size: int = 1000, chunk_overlap: int = 200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    return text_splitter.split_documents(docs)
