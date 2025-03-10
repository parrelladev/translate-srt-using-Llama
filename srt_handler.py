import sys
import re
import time
from typing import List, Iterator
from translator import TranslatorInterface, Translator

class SRTFile:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_lines(self) -> List[str]:
        """Lê um arquivo SRT e retorna uma lista de linhas."""
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.readlines()

    def write_lines(self, lines: List[str]) -> None:
        """Escreve um arquivo SRT."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            file.writelines(lines)

class ProgressTracker:
    def __init__(self, total_lines: int):
        self.total_lines = total_lines
        self.current_line = 0
        self.start_time = time.time()

    def update(self, lines_processed: int = 1) -> None:
        self.current_line += lines_processed
        progress = self.current_line / self.total_lines * 100
        sys.stdout.write(f"\rProgresso: {progress:.2f}% concluído")
        sys.stdout.flush()

    def finish(self) -> float:
        end_time = time.time()
        total_time = end_time - self.start_time
        print("\n✅ Tradução concluída!")
        print(f"⏳ Tempo total: {total_time:.2f} segundos")
        return total_time

class SRTHandler:
    def __init__(self, translator: TranslatorInterface = None):
        self.translator = translator or Translator()

    def _is_metadata_line(self, line: str) -> bool:
        """Verifica se a linha é um número de sequência ou timestamp."""
        return bool(re.match(r"^\d+$", line.strip()) or "-->" in line)

    def _translate_line(self, line: str) -> str:
        """Traduz uma linha de texto se não for metadata."""
        if self._is_metadata_line(line):
            return line
        return self.translator.translate_text(line.strip()) + "\n"

    def translate_srt(self, input_path: str, output_path: str) -> None:
        """Traduz as legendas mantendo a formatação e exibe o progresso."""
        input_file = SRTFile(input_path)
        output_file = SRTFile(output_path)
        
        lines = input_file.read_lines()
        progress = ProgressTracker(len(lines))
        
        translated_lines = []
        for line in lines:
            translated_lines.append(self._translate_line(line))
            progress.update()
        
        output_file.write_lines(translated_lines)
        progress.finish()