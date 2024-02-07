#
from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Configure the generative AI model
genai.configure(api_key='AIzaSyAass-uhtkfBxUWwOY4yvrhYaqGrfrEN8I')
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return "No selected file"

    # Read the content from the uploaded file
    content_text = file.read().decode('utf-8')

    # Combine content with the predefined instruction
    instruction = '''Generate detailed clinical notes based on a conversation of only doctor or between a doctor and a patient. The conversation should cover the patient's chief complaint, relevant medical history, presenting symptoms, findings from a physical examination, any diagnostic tests recommended or conducted, and the subsequent treatment plan. Ensure the notes are well-organized, concise, and adhere to a standard clinical format.'''
    prompt = content_text + " " + instruction

    # Generate findings using the prompt
    generated_text = model.generate_content(prompt).text

    return generated_text

if __name__ == '__main__':
    app.run(debug=True)
