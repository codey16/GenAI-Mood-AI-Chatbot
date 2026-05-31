from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model = "sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "Hello my name is Amol Gupta. ",
    "Hello your name is Buddy. ",
    "And you all are very beautiful! "

]

vector = embedding.embed_documents(texts) 

print (vector)