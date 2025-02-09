import re
from langchain_ollama import ChatOllama

from trysuperwise import request_approval

llm = ChatOllama(
    model="deepseek-r1",
    temperature=0
)

prompt = """
Generate a linkedin message for an executive from linkedin for connection request.
You must return just the message and nothing before and after it.
Make sure there are no placeholders in the message.
Don't give me a template. If you don't have certain information keep it generic.
"""

def extract_main_content(text):
    cleaned_text = re.sub(r'<think>.*?</think>\s*', '', text, flags=re.DOTALL)
    return cleaned_text.strip()


@request_approval(channel_id="C089J5WCRL2", channel="slack")
def generate_message():
    # llm_response = llm.invoke(prompt)
    # message = extract_main_content(llm_response.content)
    message = 'hellloooo'
    return message

def agent():
    message, response = generate_message()
    print('Message: ', message)
    print('Response: ', response)
    return message

if __name__ == '__main__':
    print(agent())