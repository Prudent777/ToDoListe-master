#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import unicode_literals
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length

class TodoListForm(FlaskForm):
    title = StringField('Demande', validators=[DataRequired(), Length(1, 64)])
    status = RadioField('liste', validators=[DataRequired()],  choices=[("1", '是'),("0",'否')])
    submit = SubmitField('retour')


class LoginForm(FlaskForm):
    username = StringField('bsr', validators=[DataRequired(), Length(1, 24)])
    password = PasswordField('oso', validators=[DataRequired(), Length(1, 24)])
    submit = SubmitField('qoi')
