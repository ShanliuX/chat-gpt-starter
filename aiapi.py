from openai import OpenAI
import config

client = OpenAI(api_key = config.DevelopmentConfig.OPENAI_KEY)

def generateChatResponse(prompt):
    messages = []
    messages.append({"role": "system", "content": "You are a helpful assistant."})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)
    
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

    try:
        answer = completion.choices[0].message.content
    except:
        answer = 'Oops you beat the AI, try a different question, if the problem persists come back later.'

    return answer
