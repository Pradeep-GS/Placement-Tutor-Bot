from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

def Question_generator(Types):
    Input = f"Give me the aptitude Question Based on {Types} "
    try:
            completion = client.chat.completions.create(
                model="openai/gpt-3.5-turbo-0613",
                messages=[{"role": "user", "content": Input}],
                extra_headers={
                    "HTTP-Referer": "https://your-site.com",
                    "X-Title": "Placement-Tutor-Bot"          
                }
            )
            question = completion.choices[0].message.content
            return question
    except Exception as e:
            return f"❌ Error: {str(e)}"