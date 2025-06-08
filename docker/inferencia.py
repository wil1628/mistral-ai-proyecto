import requests

prompt = "Explica qué es un modelo de lenguaje (LLM) con ejemplos."
response = requests.post("http://host.docker.internal:11434/api/generate", json={
    "model": "mistral",
    "prompt": prompt,
    "stream": False
})
print(response.json()["response"])
