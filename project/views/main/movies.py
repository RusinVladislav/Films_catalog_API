from flask import request
from flask_restx import Resource, Namespace
from project.container import movie_service
from project.setup.api.models import movie
from project.setup.api.parsers import page_parser

api = Namespace('movies')


@api.route('/')
class MoviesView(Resource):
    @api.expect(page_parser)
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all movies.
        """
        filter = request.args.get('status')

        if filter != None and (filter == "new" or filter == "old"):
            return movie_service.get_all(filter=filter, **page_parser.parse_args())
        else:
            return movie_service.get_all(**page_parser.parse_args())


@api.route('/<int:movie_id>/')
class MovieView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        return movie_service.get_item(movie_id)

# Мой код из домашки №19

# @movie_ns.route('/')
# class MoviesView(Resource):
#     @auth_required
#     def get(self):
#         director = request.args.get("director_id")
#         genre = request.args.get("genre_id")
#         year = request.args.get("year")
#         filters = {
#             "director_id": director,
#             "genre_id": genre,
#             "year": year,
#         }
#         all_movies = movie_service.get_all(filters)
#         res = MovieSchema(many=True).dump(all_movies)
#         return res, 200
#
#     @admin_required
#     def post(self):
#         req_json = request.json
#         movie = movie_service.create(req_json)
#         return "", 201, {"location": f"/movies/{movie.id}"}
#
#
# @movie_ns.route('/<int:bid>')
# class MovieView(Resource):
#     @auth_required
#     def get(self, bid):
#         b = movie_service.get_one(bid)
#         sm_d = MovieSchema().dump(b)
#         return sm_d, 200
#
#     @admin_required
#     def put(self, bid):
#         req_json = request.json
#         if "id" not in req_json:
#             req_json["id"] = bid
#         movie_service.update(req_json)
#         return "", 204
#
#     @admin_required
#     def delete(self, bid):
#         movie_service.delete(bid)
#         return "", 204
