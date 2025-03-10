from flask import Flask, render_template, request, send_file
import os
import subprocess
from main import translate_file
from werkzeug.utils import secure_filename

class FileUploadHandler:
    def __init__(self, upload_folder, max_content_length):
        self.upload_folder = upload_folder
        self.max_content_length = max_content_length
        os.makedirs(self.upload_folder, exist_ok=True)

    def validate_file(self, file):
        if not file or file.filename == '':
            raise ValueError('Nenhum arquivo selecionado')
        if not file.filename.endswith('.srt'):
            raise ValueError('Arquivo deve ser do tipo .srt')
        return True

    def save_file(self, file):
        filename = secure_filename(file.filename)
        filepath = os.path.join(self.upload_folder, filename)
        file.save(filepath)
        return filepath, filename

app = Flask(__name__)
file_handler = FileUploadHandler(
    upload_folder='arquivos',
    max_content_length=16 * 1024 * 1024  # 16MB max-limit
)
app.config['MAX_CONTENT_LENGTH'] = file_handler.max_content_length
app.config['EXPORT_FOLDER'] = 'exportados'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/open-folder')
def open_folder():
    """Abre a pasta de arquivos exportados no explorador de arquivos."""
    try:
        export_path = os.path.abspath(app.config['EXPORT_FOLDER'])
        os.makedirs(export_path, exist_ok=True)
        
        if os.name == 'nt':  # Windows
            os.startfile(export_path)
        elif os.name == 'posix':  # macOS e Linux
            subprocess.run(['xdg-open' if os.system('which xdg-open') == 0 else 'open', export_path])
            
        return '', 204  # Retorna sem conteúdo, mas com sucesso
    except Exception as e:
        return f'Erro ao abrir pasta: {str(e)}', 500

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return 'Nenhum arquivo enviado', 400

        file = request.files['file']
        file_handler.validate_file(file)
        filepath, filename = file_handler.save_file(file)

        # Traduz o arquivo
        translated_file = translate_file(filepath)

        # Retorna o arquivo traduzido
        return send_file(
            translated_file,
            as_attachment=True,
            download_name=f"traduzido_{filename}"
        )
    except ValueError as e:
        return str(e), 400
    except Exception as e:
        return f'Erro ao processar arquivo: {str(e)}', 500

if __name__ == '__main__':
    app.run(debug=True) 