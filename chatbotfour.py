from flask import Flask, request, render_template, jsonify
from transformers import pipeline
import pandas as pd

app = Flask(__name__)

# Load a pre-trained question-answering model
qa_model = pipeline("question-answering")

# Load custom Q&A data from an Excel file
custom_data = pd.read_excel("B:\BShan\Python\Chatbot\SelfServeChatBot.xlsx")


@app.route('/')
def chatbot_home():
    return render_template('chatbotfour.html')


@app.route('/ask', methods=['POST'])
def ask_question():
    question = request.form['question']

    # Search for the answer in the custom Q&A data
    answer = search_custom_data(question)

    if answer:
        return jsonify({"response": answer})
    else:
        # Use the question-answering model if no custom answer is found
        result = qa_model(question=question, context="")
        return jsonify({"response": result['answer']})


def search_custom_data(question):
    for index, row in custom_data.iterrows():
        if question.lower() in row['Question'].lower():
            return row['Answer']
    return None


if __name__ == '__main__':
    app.run(debug=True)


