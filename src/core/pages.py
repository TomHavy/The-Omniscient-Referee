import streamlit as st

from core.functions import(
    get_result,
)
from core.style import page_style

def info():
    text =   f"""
    #### Use-case: 
    - A chatbot specilised in answer NBA basketball related questions or situation. This use-case can be of value, as in real life referres \
    cannot have access to the rule book in real time. Here you can ask any question or situation, and with the official rule book in context, \
    the bot should provide a more accurate and non-biais answer.
    - This projet was made for demonstration purposes to try out the new Mistral model on a fully open-source and scalable stack.

    #### A fully open-source stack:
    - **Mistral 7b:** It's impressive 7.3 billion parameters, takes center stage. \
    It's a powerhouse model that outperforms even larger models on various benchmarks. \
    Notably, it excels in English tasks while also holding its ground in code-related tasks. \
    Mistral 7B utilizes Grouped-query attention (GQA) for swift inference and employs Sliding Window Attention (SWA) to handle longer sequences more efficiently. \
    And the best part? It's open-source under the Apache 2.0 license, offering unrestricted access.
    
    - Haystack: It's open-source framework that simplifies the development of production-ready applications. \
    It provides a seamless experience for leveraging the latest Large Language Models (LLMs), like Mistral 7B, for various tasks. \
    With Haystack, you can effortlessly manage preprocessing, pipelines, agents, and evaluation. \
    Plus, it offers flexibility in choosing databases, from Elasticsearch to Weaviate, allowing you to scale up to handling millions of documents with ease.\

    - Elastic Search: ES is a NoSQL database and search engine that stores its documents in a decentralized manner, distributing them over several nodes. \
    Developers love ES for its ease of use, scalability, and the speed with which it returns keyword-based search results, even from large datasets.\
    But did you know that you could leverage the latest Transformer models to add semantic search capabilities to your ES index?    
    
    - Streamlit: Is open-source Python library, simplifies the development of user-friendly web applications for our project, seamlessly integrating with this tech stack.
    """    
    st.markdown(text, unsafe_allow_html=True)

def chat():
    query = st.text_input("Question NBA referree: ")

    col1,col2 = st.columns(2)
    if query:
            answer,document = get_result(query)
            col1.subheader("Answer:")
            col1.markdown(f'<div style="text-align: justify;">{answer}</div>', unsafe_allow_html=True)

            col2.subheader("Extract from the official NBA rule book:")
            col2.markdown(f'<div style="text-align: justify;">{document}</div>', unsafe_allow_html=True)

def file():
    st.markdown("""
    <div style="display: flex; justify-content: center;">
    <embed src="https://ak-static.cms.nba.com/wp-content/uploads/sites/4/2022/10/Official-Playing-Rules-2022-23-NBA-Season.pdf" width="800" height="1000" type="application/pdf">
    </div>
    """, unsafe_allow_html=True)