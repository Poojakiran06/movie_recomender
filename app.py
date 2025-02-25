import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import 
# Google Gemini Model and Source the Recommendations...
movie_template ='''Based on {user_input} provide Movie Recommendations'''
movie_prompt = PromptTemplate(input_variables = ["user_input"],
                          template = movie_template)
# Initiate the Model...
llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro",
                             api_key = os.getenv("GOOGLE_API_KEY"))
if submit:
    prompt = movie_prompt.format(user_input=user_input)
    recommendations = llm.predict(text = prompt)
    st.write(f"Recommendations for you: {recommendations}")
else:
    st.write(" ")