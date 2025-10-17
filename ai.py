from openai import OpenAI
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes
load_dotenv()
API_KEY = os.getenv("API_KEY")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

def ai_answer_generator(qus):
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-3.5-turbo-0613",
            messages=[
                {"role": "user", "content": qus}
            ],
            extra_headers={
                "HTTP-Referer": "https://your-site.com",
                "X-Title": "Placement-Tutor-Bot"
            }
        )
        answer = completion.choices[0].message.content
        return answer

    except Exception as e:
        return e
def leetcode_answer_check(title,mysol):
    prompt=f"""I solved the LeetCode problem{title} and my solution is {mysol} this is correct or not just say yes correct or no wrong if wrong give me the percentage of i was near to answer don't give solution  """
    return ai_answer_generator(prompt)