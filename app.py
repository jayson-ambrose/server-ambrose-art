#!/usr/bin/env python3

# Standard library imports
from datetime import date

# Remote library imports
from flask import request, make_response, session
from flask_cors import cross_origin
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

# Local imports
from config import app, db, api
from models import Artist, Piece, Article, User, Message, Chat, DefaultBase
# from models import User, Task, List, DefaultBase

app.secret_key = 'dkdfkSKDGSDFGdfkvnia;vDAKCni1dkf65kjlfgFJl6kgGsdh4dfgk1fjD3gdKDJ'

class Login(Resource):

    # @cross_origin(methods=['POST'], supports_credentials=True, headers=['Content-Type'], origin='http://127.0.0.1:5173')
    def post(self):
        req_data = request.get_json()
        user = User.query.filter(User.username == req_data['username']).first()
        
        if not user:
            print('no user')
            return make_response({'error':'login error'}, 401)

        try:
            if user.auth(req_data['password']) == False:
                return make_response({'error': 'wrong password enterred'}, 401)
            
            session['user_id'] = user.id
            print (session)

            response = make_response(user.to_dict(rules=('-password',)), 200)
            # response.set_cookie('access_cookie', value=app.secret_key, domain='https://www.ambrosearts.com/')

            return response
        
        except:
            return make_response({'error':'login error'}, 401)
        
class Logout(Resource):

    def delete(self):
        session.clear()
        return make_response({}, 204)
    
class CheckSession(Resource):

    def get(self):
        
        user = User.query.filter(User.id == session.get('user_id')).one_or_none()
        print(user)

        if user:
            return make_response(user.to_dict(rules=('-_password',)), 200)
        else:
            return make_response({'error':'session not found'}, 401)
        
class Artists(Resource):
    
    def get(self):
        artist_list = []
        for artist in Artist.query.all():
            artist_list.append(artist.to_dict())

        return make_response(artist_list, 200)

class Pieces(Resource):
    
    def get(self):
        piece_list = []
        for piece in Piece.query.all():
            piece_list.append(piece.to_dict())

        return make_response(piece_list, 200)        

class Articles(Resource):
    
    def get(self):
        article_list = []
        for article in Article.query.all():
            article_list.append(article.to_dict())
        
        return make_response(article_list, 200)

class Users(Resource):
    
    def get(self):
        user_list = []
        for user in User.query.all():
            user_list.append(user.to_dict())
        
        return make_response(user_list, 200)                

# Views        
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/checksession')
api.add_resource(Artists, '/artists')
api.add_resource(Pieces, '/pieces')
api.add_resource(Articles, '/articles')
api.add_resource(Users, '/users')


if __name__ == '__main__':
    app.run(port=5555, debug=True)