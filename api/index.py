require('dotenv').config();

const express = require('express');
const app = express();

const bodyParser = require('body-parser');
const path = require('path');


const urlencodedParser = bodyParser.urlencoded({ extended: false });

app.use(express.static('public'));

app.post('/convert', urlencodedParser, async (req, res) => {
	try {
		res.status(200).send('Sucesso');
	} catch (error) {
		console.error(error);
		res.status(500).send('Error adding user');
	}
});

module.exports = app;
