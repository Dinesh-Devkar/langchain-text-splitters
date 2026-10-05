from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("datasets/The_AI_Marketing_Canvas.pdf")

docs=loader.lazy_load()

splitter=RecursiveCharacterTextSplitter(chunk_size=2000)

documents=splitter.split_documents(docs)

print(len(documents))
print("="*40)
print(documents[10])