import os
from srt_handler import SRTHandler
from translator import Translator

class TranslationService:
    def __init__(self):
        self.srt_handler = SRTHandler(Translator())
        self.output_dir = "exportados"
        os.makedirs(self.output_dir, exist_ok=True)

    def get_output_path(self, input_path: str) -> str:
        """Gera o caminho do arquivo de saída baseado no arquivo de entrada."""
        filename = os.path.basename(input_path)
        return os.path.join(self.output_dir, f"traduzido_{filename}")

    def translate_file(self, input_path: str) -> str:
        """Traduz um arquivo SRT e retorna o caminho do arquivo traduzido."""
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {input_path}")
        
        if not input_path.endswith('.srt'):
            raise ValueError("Arquivo deve ter extensão .srt")

        output_path = self.get_output_path(input_path)
        self.srt_handler.translate_srt(input_path, output_path)
        return output_path

def translate_file(input_path: str) -> str:
    """Função de conveniência para manter compatibilidade com código existente."""
    service = TranslationService()
    return service.translate_file(input_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo.srt>")
        sys.exit(1)
    
    try:
        translated_file = translate_file(sys.argv[1])
        print(f"Arquivo traduzido salvo em: {translated_file}")
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)