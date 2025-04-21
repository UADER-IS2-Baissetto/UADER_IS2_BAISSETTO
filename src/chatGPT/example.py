"""Script de consulta interactiva con OpenAI mediante prompt_toolkit."""

from openai import OpenAI
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory

client = OpenAI()
history = InMemoryHistory()
session = PromptSession(history=history)

try:
    request = session.prompt("Hola, ingresa tu consulta a continuación:\n")
    history.append_string(request)

    while request.strip() != "":
        print("You:", request)
        response = client.responses.create(
            model="gpt-4.1",
            input=request
        )
        print("ChatGPT:", response.output_text)
        request = input("Ingresa tu siguiente consulta a continuación:\n")

    print("No ingresaste ninguna consulta.")

except Exception as error:  # Mejor evitar capturar Exception directamente
    print("Ocurrió un error al procesar la consulta:", str(error))