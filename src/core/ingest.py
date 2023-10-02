from haystack.preview.components.file_converters.pypdf import PyPDFToDocument
from haystack.document_stores import ElasticsearchDocumentStore
from haystack.nodes import (
    EmbeddingRetriever, 
    PreProcessor,
)


print("Import Successfully")

path_doc =["data/2022-2023-NBA-RULE-BOOK.pdf"]

document_store = ElasticsearchDocumentStore()

converter = PyPDFToDocument()

output = converter.run(paths=path_doc)
docs = output["documents"]

final_doc = []
for doc in docs:
    print(doc.text)
    new_doc = {
        'content': doc.text,
        'meta': doc.metadata
    }
    final_doc.append(new_doc)
    print("#####################")

preprocessor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=True,
    clean_header_footer=True,
    split_by="word",
    split_length=200,
    split_respect_sentence_boundary=True,
    split_overlap=0,
    language="en",
)

print("#####################")
preprocessed_docs = preprocessor.process(final_doc)
print("Preprocessed Docs: ", preprocessed_docs)
print("#####################")

document_store.write_documents(preprocessed_docs)

retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="sentence-transformers/multi-qa-mpnet-base-dot-v1"
)

document_store.update_embeddings(retriever)

print("Embeddings Done.")
