from openai import OpenAI
import config
import httpx

client = OpenAI(
    base_url="https://api.xiaoai.plus/v1",
    api_key = config.DevelopmentConfig.OPENAI_KEY,
    http_client=httpx.Client(
        base_url="https://api.xiaoai.plus/v1",
        follow_redirects=True,
    ),
)

def generateChatResponse(prompt):
    messages = []
    messages.append({"role": "system", "content": "You are a helpful assistant."})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)
    
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

    try:
        answer = response.choices[0].message.content
    except:
        answer = 'Oops you beat the AI, try a different question, if the problem persists come back later.'

    return answer
