<div align="center">

![Superwise Logo](./images/superwise.svg)

</div>

Agents hallucinate and it's not going anywhere. Introduce supervision and sandboxes in mission critical systems to reduce the blast radius of the hallucinations.

<div align="center">

<h3>

[Homepage](https://trysuperwise.com/) | [Get Started](https://trysuperwise.com/home)

</h3>

[![GitHub Repo stars](https://img.shields.io/github/stars/xperience-lab/superwise)](https://github.com/xperience-lab/superwise)
[![License: Apache-2](https://img.shields.io/badge/License-Apache-green.svg)](https://opensource.org/licenses/Apache-2)
[![PyPi Version](https://img.shields.io/pypi/v/trysuperwise?color=006dad)](https://pypi.org/project/trysuperwise/)

<img referrerpolicy="no-referrer-when-downgrade" src="https://static.scarf.sh/a.png?x-pxid=fcfc0926-d841-47fb-b8a6-6aba3a6c3228" />

</div>

# Get started with Superwise using Python and OpenAI

### Setup Environment

```sh
mkdir superwise-demo && cd superwise-demo

```

Install the required package with pip:

```sh
pip install langchain langchain-openai trysuperwise
```

Next, get your OpenAI API key from the [OpenAI dashboard](https://platform.openai.com/api-keys).

```sh
export OPENAI_API_KEY=<your-openai-api-key>
```

and set your Superwise Project ID and API key

```sh
export SUPERWISE_PROJECT_ID=<your-superwise-project-id>
export SUPERWISE_API_KEY=<your-superwise-api-key>
```

### Create a Simple Agent

```python
import re
from langchain_openai import ChatOpenAI

from trysuperwise import request_approval

llm = ChatOpenAI(model="gpt-4o", temperature=0)

prompt = """
Generate a linkedin message for an executive from linkedin for connection request.
You must return just the message and nothing before and after it.
Make sure there are no placeholders in the message.
Don't give me a template. If you don't have certain information keep it generic.
"""

def extract_main_content(text):
    cleaned_text = re.sub(r'<think>.*?</think>s*', '', text, flags=re.DOTALL)
    return cleaned_text.strip()


@request_approval(channel_id=<your-slack-channel-id>, channel="slack")
def generate_message():
    llm_response = llm.invoke(prompt)
    message = extract_main_content(llm_response.content)
    return message

def agent():
    message, response = generate_message()
    print('Message: ', message)
    print('Response: ', response)
    return message

if __name__ == '__main__':
    print(agent())
```
