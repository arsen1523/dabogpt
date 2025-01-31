import requests

TOGETHER_API_KEY = "7d43b91b79092eca3be7ced5baa2035406fa9f957b5d32e6f3ca1581f1e98f03"

def chat_with_ai(prompt):
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",  # Или другой (llama, gemma)
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()["choices"][0]["message"]["content"]

print(chat_with_ai("Привет, как дела?"))  # Тест запроса
