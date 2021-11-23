# models.py


import datetime
from app import db


class Aluno(db.Model):

    __tablename__ = 'Aluno'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    turma = db.Column(db.String, nullable=False)
    nota = db.Column(db.Integer, nullable=False)
    data_postada = db.Column(db.DateTime, nullable=False)

    def __init__(self, nome, turma, nota):
        self.nome = nome
        self.turma = turma
        self.nota = nota
        self.data_postada = datetime.datetime.now()
