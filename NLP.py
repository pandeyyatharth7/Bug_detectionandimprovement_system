import os
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "Salesforce/codet5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


def analyze_code_files(local_path):
    analysis_results = []
    for root, _, files in os.walk(local_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    code = f.readlines()
                    for line_number, line in enumerate(code, start=1):
                        inputs = tokenizer(line, return_tensors="pt", truncation=True, padding=True)
                        outputs = model(**inputs)
                        analysis_results.append((file_path, line_number, line, outputs.logits))
    return analysis_results


def suggest_improvements(analysis_results):
    suggestions = []
    for file_path, line_number, line, logits in analysis_results:
        # Example logic to interpret logits and provide suggestions
        if logits[0][1] > logits[0][0]:  # If the probability of being buggy is higher
            suggestions.append((file_path, line_number, line, "Possible error detected. Consider refactoring this line."))
    return suggestions


def display_suggestions(suggestions):
    file_suggestions = {}
    for file_path, line_number, line, suggestion in suggestions:
        if file_path not in file_suggestions:
            file_suggestions[file_path] = []
        file_suggestions[file_path].append((line_number, line, suggestion))

    for file_path, issues in file_suggestions.items():
        print(f"File: {file_path}")
        for line_number, line, suggestion in issues:
            print(f"  Line {line_number}: {line.strip()}")
            print(f"    Suggestion: {suggestion}")
        print("\n")


local_path = "C:/Users/Asus/Desktop/Hackathons/Makethon' 25/QuixBugs/python_testcases"
analysis_results = analyze_code_files(local_path)
suggestions = suggest_improvements(analysis_results)
display_suggestions(suggestions)
