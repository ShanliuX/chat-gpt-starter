from openai import OpenAI
import config

api_key = config.DevelopmentConfig.OPENAI_KEY

client = OpenAI()
client.api_key = api_key

def generateChatResponse(prompt):

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
      ]
    )
