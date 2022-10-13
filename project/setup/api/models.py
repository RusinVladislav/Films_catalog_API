from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Владислав'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Бессонная ночь'),
    'description': fields.String(required=True, max_length=250, example='Бессонная ночь началась с февраля 2022 года'),
    'trailer': fields.String(required=True, max_length=100, example='https://www.youtube.com/watch?v=VWPPu54UTes&t=3956s'),
    'year': fields.Integer(required=True, example=2022),
    'rating': fields.Float(required=True, example=9.0),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='etyetwu@gmail.com'),
    'password': fields.String(required=True, max_length=100, example='По1987t'),
    'name': fields.String(required=True, max_length=100, example='Пончик'),
    'surname': fields.String(required=True, max_length=100, example='Иванов'),
    'genre': fields.Nested(genre),
})
