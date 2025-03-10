class FileUploadHandler {
    constructor() {
        this.dropZone = document.getElementById('drop-zone');
        this.fileInput = document.getElementById('file');
        this.fileInfo = document.getElementById('file-info');
        this.fileName = document.getElementById('file-name');
        this.submitBtn = document.getElementById('submit-btn');
        this.uploadForm = document.getElementById('upload-form');
        
        this.initializeEventListeners();
    }

    initializeEventListeners() {
        // Drag and drop events
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            this.dropZone.addEventListener(eventName, (e) => {
                e.preventDefault();
                e.stopPropagation();
            });
        });

        ['dragenter', 'dragover'].forEach(eventName => {
            this.dropZone.addEventListener(eventName, () => {
                this.dropZone.classList.add('dragover');
            });
        });

        ['dragleave', 'drop'].forEach(eventName => {
            this.dropZone.addEventListener(eventName, () => {
                this.dropZone.classList.remove('dragover');
            });
        });

        // File drop handler
        this.dropZone.addEventListener('drop', (e) => {
            const files = e.dataTransfer.files;
            if (files.length) {
                this.fileInput.files = files;
                this.handleFileSelect();
            }
        });

        // File input change handler
        this.fileInput.addEventListener('change', () => this.handleFileSelect());

        // Form submit handler
        this.uploadForm.addEventListener('submit', (e) => this.handleSubmit(e));
    }

    handleFileSelect() {
        const file = this.fileInput.files[0];
        
        if (file) {
            if (!file.name.toLowerCase().endsWith('.srt')) {
                this.showError('Por favor, selecione um arquivo .srt válido.');
                this.resetForm();
                return;
            }

            this.fileName.textContent = file.name;
            this.fileInfo.classList.remove('d-none');
            this.submitBtn.disabled = false;
        } else {
            this.resetForm();
        }
    }

    async handleSubmit(e) {
        e.preventDefault();
        
        const formData = new FormData(this.uploadForm);
        this.submitBtn.disabled = true;
        this.showProgress();

        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                const blob = await response.blob();
                this.downloadFile(blob);
                this.showSuccess('Arquivo traduzido com sucesso!');
            } else {
                const error = await response.text();
                this.showError(`Erro: ${error}`);
            }
        } catch (error) {
            this.showError('Erro ao processar o arquivo. Tente novamente.');
        } finally {
            this.hideProgress();
            this.submitBtn.disabled = false;
        }
    }

    showProgress() {
        const progressHtml = `
            <div id="progress-container" class="mt-3">
                <div class="progress">
                    <div class="progress-bar progress-bar-striped progress-bar-animated" 
                         role="progressbar" 
                         style="width: 100%">
                        Traduzindo...
                    </div>
                </div>
            </div>`;
        
        this.fileInfo.insertAdjacentHTML('afterend', progressHtml);
    }

    hideProgress() {
        const progressContainer = document.getElementById('progress-container');
        if (progressContainer) {
            progressContainer.remove();
        }
    }

    showError(message) {
        this.showAlert(message, 'danger');
    }

    showSuccess(message) {
        const alertHtml = `
            <div class="alert alert-success alert-dismissible fade show mt-3" role="alert">
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <i class="bi bi-check-circle me-2"></i>
                        ${message}
                    </div>
                    <div>
                        <button type="button" class="btn btn-sm btn-outline-success ms-3" onclick="window.location.href='/open-folder'">
                            <i class="bi bi-folder2-open me-2"></i>
                            Abrir Pasta
                        </button>
                        <button type="button" class="btn-close ms-2" data-bs-dismiss="alert"></button>
                    </div>
                </div>
            </div>`;
        
        const existingAlert = this.uploadForm.querySelector('.alert');
        if (existingAlert) {
            existingAlert.remove();
        }
        
        this.fileInfo.insertAdjacentHTML('afterend', alertHtml);
    }

    showAlert(message, type) {
        const alertHtml = `
            <div class="alert alert-${type} alert-dismissible fade show mt-3" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>`;
        
        const existingAlert = this.uploadForm.querySelector('.alert');
        if (existingAlert) {
            existingAlert.remove();
        }
        
        this.fileInfo.insertAdjacentHTML('afterend', alertHtml);
    }

    downloadFile(blob) {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = this.fileInput.files[0].name.replace('.srt', '_traduzido.srt');
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        a.remove();
    }

    resetForm() {
        this.fileInput.value = '';
        this.fileInfo.classList.add('d-none');
        this.submitBtn.disabled = true;
        this.hideProgress();
    }
}

// Initialize the handler when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new FileUploadHandler();
}); 