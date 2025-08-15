#rag logic - Purpose: Retrieves relevant finance info and generates LLM response.
from langchain.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader

def get_vector_store():
    loader = TextLoader("data/finance_docs/finance_guide.txt")
    docs = loader.load()
    embeddings = HuggingFaceEmbeddings()
    vectordb = Chroma.from_documents(docs, embeddings)
    return vectordb

def get_llm():
    return LlamaCpp(model_path="models/llama-7b.gguf", n_ctx=2048)

def get_llm_response(query):
    vectordb = get_vector_store()
    retriever = vectordb.as_retriever()
    llm = get_llm()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain.run(query)

