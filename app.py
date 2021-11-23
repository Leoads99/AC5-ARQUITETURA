#!/usr/bin/env python
# app.py

import os
from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


from models import *


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        turma = request.form['turma']
        nota = request.form['nota']
        aluno = Aluno(nome, turma, nota)
        db.session.add(aluno)
        db.session.commit()
    alunos = Aluno.query.order_by(Aluno.data_postada.desc()).all()
    return render_template('index.html', alunos=alunos)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)

