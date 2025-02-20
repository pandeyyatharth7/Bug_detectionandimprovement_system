# backend/app.py
from flask import Flask, render_template, request, jsonify
import os
from model.code_analyzer import analyze_code_files, suggest_improvements

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    code = request.form.get('code')
    if not code:
        return jsonify({"error": "No code provided"}), 400

    # Save the code to a temporary file
    temp_path = "temp_code.py"
    with open(temp_path, 'w') as f:
        f.write(code)

    # Analyze the code
    analysis_results = analyze_code_files(os.path.dirname(temp_path))
    suggestions = suggest_improvements(analysis_results)

    # Clean up the temporary file
    os.remove(temp_path)

    return jsonify({"suggestions": suggestions})

if __name__ == '__main__':
    app.run(debug=True)