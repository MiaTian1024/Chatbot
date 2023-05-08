import os
import openai


def get_response(user_input):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=3000,
        temperature=0.5
    ).choices[0].text
    return response
    
if __name__ == "__main__":    
    response = get_response("Write a joke about birds")
    print(response)
