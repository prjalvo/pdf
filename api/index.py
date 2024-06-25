from flask import Flask, send_file, request
from werkzeug.utils import secure_filename
import os
import pdfkit

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/convert', methods=['POST'])
def convert_docx_to_pdf():
    try:
        # Verifica se foi enviado um arquivo DOCX
        if 'file' not in request.files:
            return "Erro: Nenhum arquivo enviado.", 400

        file = request.files['file']

        # Verifica se o arquivo tem um nome e é um arquivo DOCX
        if file.filename == '':
            return "Erro: Nome de arquivo inválido.", 400
        if not file.filename.endswith('.docx'):
            return "Erro: O arquivo deve ser DOCX.", 400

        # Salva o arquivo DOCX em um local temporário
        temp_dir = '/tmp'
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        
        docx_filename = secure_filename(file.filename)
        docx_path = os.path.join(temp_dir, docx_filename)
        file.save(docx_path)

        # Caminho para o arquivo de saída PDF
        pdf_filename = f"{os.path.splitext(docx_filename)[0]}.pdf"
        pdf_path = os.path.join(temp_dir, pdf_filename)

        # Converte o arquivo DOCX para PDF usando pdfkit
        pdfkit.from_file(docx_path, pdf_path)

        # Envia o arquivo PDF convertido como resposta
        return send_file(pdf_path, as_attachment=True)

    except Exception as e:
        return f"Erro: {e}", 500

if __name__ == '__main__':
    app.run(debug=True)

