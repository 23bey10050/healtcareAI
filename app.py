import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

#LOAD A PRE-TRAINED HUGGING FACE MODEL
chatbot= pipeline("question-answering", model="deepset/roberta-base-squad2")

#preprocess user input
def preprocess_imput(user_input):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(user_input)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

#define healthcare-specific response logic

def healthcare_response(user_input):
    user_input = preprocess_imput(user_input)
    if "sneeze" in user_input or "sneezing" in user_input:
        return "Frequent sneezing may indicate allergies or a cold. Consult a healthcare professional for a check-up."
    elif "symptom" in user_input :
        return "It seems like you're experiencing symptoms. Please Counsult a healthcare professional for a check-up."
    elif "appointment" in user_input :
        return "Would you like to schedule an appointment with a healthcare professional?"
    elif "medication" in user_input:
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor. "
    else:
        content ="""
         Commom helthcare-related scenarios include symptoms of colds, flu, and allergies,
         along with appointments and medication schedules.
         """

        response = chatbot(question=user_input, context=content)
        return response['answer']

# Streamlit web app interface
def main():
    st.title("Healthcare Assistant chatbot")
    user_input = st.text_input("How can I help you?")
    if st.button("Submit"):
        if user_input:
            st.write("User:", user_input)
            response = healthcare_response(user_input)
            st.write("Healthcare Assistant:", response)
        else:
            st.write("Please enter a valid input.")

if __name__ == "__main__":
    main()
    