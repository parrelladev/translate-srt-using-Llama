# Tradutor de Legendas SRT usando Ollama

Uma aplicação web para traduzir arquivos de legendas (.srt) usando o modelo de linguagem Ollama localmente.

![Interface do Tradutor de Legendas](static/images/preview.png)

## 🚀 Funcionalidades

- ✨ Interface web moderna e intuitiva
- 📁 Suporte a drag-and-drop de arquivos
- 🔄 Tradução automática de legendas
- 💾 Download automático do arquivo traduzido
- 📂 Acesso rápido à pasta de arquivos traduzidos
- 🎯 Preservação do formato e timing das legendas
- 🔒 Processamento local das traduções

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Ollama instalado e rodando localmente
- Conexão com a internet (para baixar as dependências)

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/translate-srt-using-Llama.git
cd translate-srt-using-Llama
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:

No Windows:
```powershell
.\venv\Scripts\activate
```

No Linux/macOS:
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 💻 Como Usar

1. Certifique-se de que o Ollama está rodando no seu sistema

2. Inicie o servidor Flask:
```bash
python app.py
```

3. Acesse a aplicação em seu navegador:
```
http://localhost:5000
```

4. Use a interface para:
   - Arrastar e soltar arquivos .srt
   - Ou clicar no botão para selecionar um arquivo
   - O arquivo traduzido será baixado automaticamente
   - Use o botão "Abrir Pasta" para acessar os arquivos traduzidos

## 📁 Estrutura do Projeto

```
translate-srt-using-Llama/
├── app.py              # Aplicação Flask principal
├── config.py           # Configurações do Ollama
├── main.py            # Serviço de tradução
├── translator.py      # Interface com o Ollama
├── srt_handler.py     # Manipulação de arquivos SRT
├── requirements.txt   # Dependências do projeto
├── static/           # Arquivos estáticos
│   ├── css/         # Estilos CSS
│   └── js/          # Scripts JavaScript
├── templates/        # Templates HTML
├── arquivos/        # Pasta temporária de uploads
└── exportados/      # Pasta de arquivos traduzidos
```

## 🔧 Configuração

O arquivo `config.py` contém as configurações para a API do Ollama. Você pode ajustar:
- URL da API
- Modelo de linguagem
- Parâmetros de tradução
- Timeouts

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
1. Fazer um fork do projeto
2. Criar uma branch para sua feature
3. Commitar suas mudanças
4. Fazer push para a branch
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✨ Agradecimentos

- [Ollama](https://ollama.ai/) pelo modelo de linguagem
- [Flask](https://flask.palletsprojects.com/) pelo framework web
- [Bootstrap](https://getbootstrap.com/) pelo framework CSS 