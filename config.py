API_CONFIG = {
    "name": "Ollama",
    "languages": {
        "source": {"English": "English"},
        "target": {"Portuguese (Brazil)": "Portuguese (Brazil)"}
    },
    "request": {
        "url": "http://localhost:12345/v1/completions",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json"
        },
        "timeout": 60,
        "data": {
            "model": "llama3.1:8b",
            "prompt": (
                "Você é um tradutor profissional de legendas para filmes e séries."
                "Siga estas diretrizes para garantir que as traduções sejam naturais, coerentes e adequadas ao contexto:\n"
                "\n"
                "**NÃO adicione explicações, comentários ou observações. Apenas retorne a tradução.**\n"
                "**Preserve a estrutura original da legenda, incluindo tempos e formatação.**\n"
                "**Traduza expressões idiomáticas de forma natural**, evitando traduções literais estranhas.\n"
                "**Adapte falas e gírias para o português coloquial, garantindo fluidez.**\n"
                "**Mantenha efeitos sonoros entre colchetes ('[]') e traduza-os corretamente.**\n"
                "**Nomes próprios e locais conhecidos NÃO devem ser traduzidos** (exemplo: 'Heisenberg', 'Hell's Kitchen').\n"
                "**Evite formalidade excessiva se o diálogo for casual.**\n"
                "**Antes de retornar a tradução, pergunte-se:**\n"
                "   - As palavras estão escritas corretamente?\n"
                "   - A tradução faz sentido no contexto?\n"
                "   - Mantém a naturalidade e fluidez da fala?\n"
                "   - Evita erros comuns de tradução literal?\n"
                "\n"
                "**IMPORTANTE:** Apenas retorne a legenda traduzida corretamente. "
                "NÃO adicione explicações ou notas adicionais.\n"
                "\n"
                "Texto original:\n<text>"
            ),
            "temperature": 0.1,
            "max_tokens": 512,
            "stream": False
        }
    },
    "response": "response_json['choices'][0]['text']"
}