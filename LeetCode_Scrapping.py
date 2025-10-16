import pandas as pd

df = pd.read_csv("preprocessed_data.csv")
unsolved = df[df['solved'] == 'No']
question = unsolved.sample(1).iloc[0] if not unsolved.empty else None

def mark_as_solved(title):
    df = pd.read_csv("preprocessed_data.csv")
    df.loc[df['title'].str.strip().str.lower() == title.strip().lower(), 'solved'] = 'Yes'
    df.to_csv("preprocessed_data.csv", index=False)
    print(f"✅ '{title}' marked as solved!")

def title():
    return question['title'] if question is not None and question['title'] else " "

def problem_description():
    return question['problem_description'] if question is not None and question['problem_description'] else " "

def tag():
    return question['topic_tags'] if question is not None and question['topic_tags'] else " "

def difficulty():
    return question['difficulty'] if question is not None and question['difficulty'] else " "

def similar_questions():
    return question['similar_questions'] if question is not None and question['similar_questions'] else " "

def acceptance():
    return question['acceptance'] if question is not None and question['acceptance'] else " "

def progress():
    df = pd.read_csv("preprocessed_data.csv")
    total = len(df)
    solved = len(df[df['solved'] == 'Yes'])
    return f"Progress: {solved}/{total} questions solved ✅"

def totelegram():
    if question is None:
        return "No unsolved questions left! 🎉"
    return f"""📘 **Today's LeetCode Question**
Title:\n{title()}\n

Description:\n{problem_description()}\n

Tags:\n{tag()}\n

Difficulty:\n{difficulty()}\n

Acceptance:\n{acceptance()}\n

{progress()}
"""