from docx2pdf import convert
import os

require('dotenv').config();

const express = require('express');
const app = express();

const bodyParser = require('body-parser');
const path = require('path');


const urlencodedParser = bodyParser.urlencoded({ extended: false });

app.use(express.static('public'));

app.post('/convert', urlencodedParser, async (req, res) => {
	try {
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
        docx_filename = secure_filename(file.filename)
        docx_path = os.path.join(app.root_path, 'uploads', docx_filename)
        file.save(docx_path)

        # Caminho para o arquivo de saída PDF
        pdf_filename = f"{os.path.splitext(docx_filename)[0]}.pdf"
        pdf_path = os.path.join(app.root_path, 'downloads', pdf_filename)

        # Converte o arquivo DOCX para PDF
        convert(docx_path, pdf_path)

        # Envia o arquivo PDF convertido como resposta
        return send_file(pdf_path, as_attachment=True)
	} catch (error) {
		console.error(error);
		res.status(500).send('Error adding user');
	}
});

module.exports = app;
