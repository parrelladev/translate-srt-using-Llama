from abc import ABC, abstractmethod
import requests
from config import API_CONFIG

class TranslatorInterface(ABC):
    @abstractmethod
    def translate_text(self, text: str) -> str:
        pass

class OllamaTranslator(TranslatorInterface):
    def __init__(self, api_config=None):
        self.api_config = api_config or API_CONFIG
        self._validate_config()

    def _validate_config(self):
        required_keys = ["request", "response"]
        if not all(key in self.api_config for key in required_keys):
            raise ValueError("Configuração da API inválida")

    def _prepare_request_data(self, text: str) -> dict:
        data = self.api_config["request"]["data"].copy()
        data["prompt"] = data["prompt"].replace("<text>", text)
        return data

    def _make_api_request(self, data: dict) -> requests.Response:
        return requests.post(
            self.api_config["request"]["url"],
            headers=self.api_config["request"]["headers"],
            json=data,
            timeout=self.api_config["request"]["timeout"]
        )

    def _process_response(self, response: requests.Response) -> str:
        if response.status_code == 200:
            response_json = response.json()
            return eval(self.api_config["response"]).strip()
        raise ValueError(f"Erro na API: {response.text}")

    def translate_text(self, text: str) -> str:
        """Traduz um texto usando a API do Ollama."""
        if not text.strip():
            return text

        try:
            data = self._prepare_request_data(text)
            response = self._make_api_request(data)
            return self._process_response(response)
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return text
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return text

# Alias para manter compatibilidade com código existente
Translator = OllamaTranslator