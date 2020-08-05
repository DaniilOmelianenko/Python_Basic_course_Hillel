import json

with open("questions.json", "r") as temp_file:
    data = json.load(temp_file)

for answers in data.get("questions"):
    answers["answer"] = input(f"{answers.get('q')}: ")

with open("questions.json", "w") as temp_file:
    json.dump(data, temp_file, indent=4)
