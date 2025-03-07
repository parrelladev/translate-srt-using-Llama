# Translate-SRT: Tradutor Automático de Legendas com Ollama Llama

## Sobre o Projeto
O **Translate-SRT** é uma ferramenta poderosa para **tradução automática de legendas** de filmes e séries, utilizando o modelo **Ollama Llama**. O projeto permite traduzir arquivos `.srt` do **inglês para o português (Brasil)** de forma rápida e eficiente, mantendo a estrutura original da legenda.

O sistema também exibe **um contador de progresso (%)** em tempo real e informa **quanto tempo levou a tradução completa**.

## Funcionalidades
- Tradução **precisa e natural** de legendas de filmes e séries  
- **Preserva o tempo e a estrutura** do arquivo `.srt` original  
- **Adaptação de expressões idiomáticas e gírias** para o português  
- **Manutenção de efeitos sonoros**, traduzindo corretamente entre `[]`  
- **Barra de progresso em tempo real** mostrando o avanço da tradução  
- **Medição do tempo total** para monitorar o desempenho  

## Tecnologias Utilizadas
- **Python 3.9+**
- **Ollama Llama** (modelo de IA para tradução)
- **Requests** (para chamadas HTTP)
- **Regex** (para manipulação do formato `.srt`)

## Estrutura do Projeto
```
Translate-SRT/
│── arquivos/                # Pasta onde você coloca as legendas originais
│── exportados/              # Pasta onde os arquivos traduzidos serão salvos
│── main.py                  # Arquivo principal que executa o programa
│── config.py                # Configuração da API do Ollama
│── translator.py            # Responsável por chamar a API e traduzir frases
│── srt_handler.py           # Manipulação do arquivo .srt e exibição do progresso
│── requirements.txt         # Lista de dependências do projeto
│── README.md                # Documentação do projeto
│── venv/                    # Ambiente virtual (opcional)
```

## Como Instalar e Configurar

### 1️⃣ Instale o Python
Se ainda não tem o Python instalado, baixe e instale a versão **3.9 ou superior**:  
🔗 [Download Python](https://www.python.org/downloads/)

### 2️⃣ Instale o Ollama
O Ollama é um servidor local que executa modelos de IA. Instale-o conforme seu sistema operacional:  
🔗 [Download Ollama](https://ollama.com/)

Depois, baixe o modelo recomendado:
```sh
ollama pull llama3.1:8b
```
Se precisar de um modelo mais leve, pode usar:
```sh
ollama pull llama3.2:3b
```

### 3️⃣ Clone o repositório
```sh
git clone https://github.com/seu-usuario/Translate-SRT.git
cd Translate-SRT
```

### 4️⃣ Crie e ative um ambiente virtual
```sh
python -m venv venv
```
No **Windows**:
```sh
venv\Scripts\activate
```
No **Linux/macOS**:
```sh
source venv/bin/activate
```

### 5️⃣ Instale as dependências
```sh
pip install -r requirements.txt
```

## Como Usar
1. Coloque os arquivos `.srt` na pasta `arquivos/`
2. Execute o programa:
```sh
python main.py
```
3. Digite o caminho do arquivo **.srt** a ser traduzido.
4. Escolha um nome para o arquivo traduzido (ele será salvo em `exportados/`).
5. O progresso da tradução será exibido no terminal:
   ```
   Progresso: 45.67% concluído
   ```
6. No final, o tempo total será exibido:
   ```
   ✅ Tradução concluída!
   ⏳ Tempo total: 32.85 segundos
   ```
7. O arquivo traduzido estará disponível na pasta `exportados/`.

## Configuração Personalizada
Caso queira ajustar o modelo utilizado ou alterar configurações, edite o arquivo **`config.py`**.

Para mudar o modelo:
```python
"model": "llama3.1:8b"  # Ou "llama3.2:3b" se quiser um modelo mais leve
```

Se quiser aumentar a criatividade da IA, altere o **temperature**:
```python
"temperature": 0.3  # Valores entre 0.1 e 0.5 são ideais para tradução
```

## Problemas Comuns e Soluções

### ❌ Erro: "Model Not Exist"
🔹 O modelo informado não foi encontrado no Ollama. Certifique-se de que ele foi baixado corretamente com:
```sh
ollama pull llama3.1:8b
```

### ❌ Erro: "KeyError: 'messages'"
🔹 Isso acontece se `config.py` estiver no formato errado. O Ollama **não usa "messages"**, apenas `"prompt"`. Verifique se o arquivo `config.py` está configurado corretamente.

### ❌ Erro: "ModuleNotFoundError: No module named 'requests'"
🔹 Instale as dependências corretamente:
```sh
pip install -r requirements.txt
```

## Licença
Este projeto é de código aberto e está disponível sob a licença **MIT**.

## Autor
Criado por **[Seu Nome](https://github.com/parrelladev)**.  
Se gostou do projeto, ⭐ marque este repositório!  
Contribuições são bem-vindas!
