from langchain_core.prompts import ChatPromptTemplate
import google.generativeai as genai

prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "You are an assistant for question-answering tasks. "
                  "Use the following retrieved context to answer the question. "
                  "If you don't know the answer, say that you don't know. "
                  "Use three sentences maximum and keep the answer concise."
                  "\n\nContext: {context}\n\nQuestion: {input}"),
    ]
)

