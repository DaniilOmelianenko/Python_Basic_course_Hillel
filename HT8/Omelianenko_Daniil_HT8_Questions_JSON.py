import json

with open("questions.json", "r") as tempfile:
    data = json.load(tempfile)

for answers in data.get("questions"):
    print(answers.get('q'))
    answers["answer"] = input()

with open("questions.json", "w+") as tempfile:
    json.dump(data, tempfile, indent=4)
