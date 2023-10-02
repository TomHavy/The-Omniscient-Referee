import streamlit as st

from haystack import Pipeline
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import (
    EmbeddingRetriever,
    AnswerParser, 
    PromptNode, 
    PromptTemplate,
    )
from src.constants import(
    MODEL_PATH,
    EMBED_MODEL,
)


def load_model(prompt_template):
    prompt_node = PromptNode(model_name_or_path=MODEL_PATH,
                max_length=500,
                use_gpu=True,
                api_key=st.secrets.api_credentials.hf_api_key,
                default_prompt_template=prompt_template,
                )
    return prompt_node

def load_retriver():
    document_store = ElasticsearchDocumentStore()

    retriever = EmbeddingRetriever(
        document_store=document_store,
        embedding_model=EMBED_MODEL,
        use_gpu=True,
    )

    return retriever

def load_prompt_template():
    prompt_template = PromptTemplate(prompt = """"
You are an NBA referre. Using the extract from the official NBA rule book below to support your answer to the question/situation. Your response must be in the tone of a basketball referre.\n
Question: {query}\n
Rule: {join(documents)}
Answer: 
                                    """,
                                    output_parser=AnswerParser())
    return prompt_template


def build_pipeline(retriever, prompt_node):
    query_pipeline = Pipeline()
    query_pipeline.add_node(component=retriever, name="Retriever", inputs=["Query"])
    query_pipeline.add_node(component=prompt_node, name="PromptNode", inputs=["Retriever"])
    return query_pipeline


def get_result(query):

    retriver = load_retriver()
    prompt_template = load_prompt_template()
    prompt_node = load_model(prompt_template)
    query_pipeline = build_pipeline(retriver,prompt_node)
   
    json_response = query_pipeline.run(query = query , params={"Retriever" : {"top_k":1}})

    answers = json_response['answers']
    for ans in answers:
        answer = ans.meta["prompt"]
        break
    print("Prompt: \n",answer)

    for ans in answers:
        answer = ans.answer
        break

    documents = json_response["documents"]
    for document in documents:
        document = document.content
        break

    print(answer)
    
    return answer,document