import google.generativeai as genai
import streamlit as st 
import os 
from PIL import Image


key="AIzaSyARAzgDZVTtpxQ5HpAtbsBdM5tm3-R7Bxg"
genai.configure(api_key=key)


model=genai.GenerativeModel("gemini-pro") 
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True) 
    response.resolve()  
    return response



st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

if "chat_history" not in st.session_state:
    st.session_state['chat_history']=[]

print(get_gemini_response("write here something ?").text)

input=st.text_input("Input :",key="input")
submit=st.button("Ask the question")
chat_history=[]

if submit and input:
    response=get_gemini_response(str(input)).text
    st.session_state['chat_history'].append(("You",input))
    st.session_state['chat_history'].append(("Bot",response))
    st.subheader("The Response is :")
    # for chunk in resposne:
    #     st.write(chunk.text)
    #     st.session_state['chat_history'].append(('Bot',resposne))
    chat_history.append(("You",input))
    chat_history.append(("Bot",response))
    
  
st.subheader("The chatHistory is:")

# for role,text in chat_history:
#     st.write(f"{role}{text}")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}{text}")

    
    

    


