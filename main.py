from srt_handler import SRTHandler
import os

def main():
    """Função principal para rodar o tradutor de legendas pelo terminal."""
    print("🎬 Tradutor de Legendas - Ollama Llama")
    
    input_srt = input("📂 Digite o caminho do arquivo .srt de entrada: ").strip()
    output_srt = input("📄 Digite o nome do novo arquivo traduzido: ").strip()

    if not input_srt or not output_srt:
        print("⚠️ Caminhos inválidos. Certifique-se de fornecer os arquivos corretamente.")
        return

    export_dir = "./exportados"
    os.makedirs(export_dir, exist_ok=True)

    # Adiciona ".srt" automaticamente caso o usuário não coloque
    if not output_srt.lower().endswith(".srt"):
        output_srt += ".srt"

    output_srt_path = os.path.join(export_dir, output_srt)

    handler = SRTHandler()
    handler.translate_srt(input_srt, output_srt_path)

if __name__ == "__main__":
    main()