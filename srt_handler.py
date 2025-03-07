import sys
import re
import time
from translator import Translator

class SRTHandler:
    def __init__(self):
        self.translator = Translator()

    def read_srt(self, file_path):
        """Lê um arquivo SRT e retorna uma lista de linhas."""
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()

    def write_srt(self, file_path, lines):
        """Escreve um arquivo SRT traduzido."""
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(lines)

    def translate_srt(self, input_srt, output_srt):
        """Traduz as legendas mantendo a formatação e exibe o progresso e tempo total."""
        lines = self.read_srt(input_srt)
        total_lines = len(lines)  # Número total de linhas
        translated_lines = []

        start_time = time.time()  # Inicia a contagem do tempo

        for index, line in enumerate(lines):
            if re.match(r"^\d+$", line.strip()) or "-->" in line:
                translated_lines.append(line)  # Mantém números e timestamps
            else:
                translated_lines.append(self.translator.translate_text(line.strip()) + "\n")

            # Cálculo da porcentagem concluída
            progress = (index + 1) / total_lines * 100
            sys.stdout.write(f"\rProgresso: {progress:.2f}% concluído")
            sys.stdout.flush()

        end_time = time.time()  # Finaliza a contagem do tempo
        total_time = end_time - start_time  # Calcula o tempo total em segundos

        print("\n✅ Tradução concluída!")  # Mensagem final
        print(f"⏳ Tempo total: {total_time:.2f} segundos")  # Exibe o tempo gasto

        self.write_srt(output_srt, translated_lines)