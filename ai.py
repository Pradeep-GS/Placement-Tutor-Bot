from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

def ai_answer_generator():
    try:
        completion = client.chat.completions.create(
            model="openai/gpt-3.5-turbo-0613",
            messages=[
                {"role": "user", "content": "Hello Who Are You"}
            ],
            extra_headers={
                "HTTP-Referer": "https://your-site.com",
                "X-Title": "Placement-Tutor-Bot"
            }
        )
        answer = completion.choices[0].message.content
        print(answer)
        return answer

    except Exception as e:
        return e
ai_answer_generator()