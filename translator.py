import requests
from config import API_CONFIG

class Translator:
    def __init__(self):
        self.api_config = API_CONFIG

    def translate_text(self, text):
        """Traduz um texto usando a API do Ollama."""
        if not text.strip():
            return text  # Retorna o original se for uma linha vazia

        # Configura a requisição
        data = self.api_config["request"]["data"].copy()
        data["prompt"] = data["prompt"].replace("<text>", text)  # Ajusta o prompt

        try:
            response = requests.post(
                self.api_config["request"]["url"],
                headers=self.api_config["request"]["headers"],
                json=data,
                timeout=self.api_config["request"]["timeout"]
            )

            if response.status_code == 200:
                response_json = response.json()
                translated_text = eval(self.api_config["response"])  # Avalia a resposta
                return translated_text.strip()
            else:
                print(f"Erro na tradução: {response.text}")
                return text  # Retorna o original em caso de erro
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return text