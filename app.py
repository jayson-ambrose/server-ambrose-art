#!/usr/bin/env python3

# Standard library imports
from datetime import date

# Remote library imports
from flask import request, make_response, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

# Local imports
from config import app, db, api
from models import Artist, Piece, Article, DefaultBase
# from models import User, Task, List, DefaultBase

app.secret_key = 'dkdfkSKDGSDFGdfkvnia;vDAKCni1dkf65kjlfgFJl6kgGsdh4dfgk1fjD3gdKDJ'

class Login(Resource):

    def post(self):
        req_data = request.get_json()
        artist = Artist.query.filter(Artist.username == req_data['username']).first()

        try:
            if artist.auth(req_data['password']) == False:
                return make_response({'error': 'wrong password enterred'}, 401)
            
            session['user_id'] = artist.id

            make_response(artist.to_dict(), 200)
        
        except:
            return make_response({'error':'login error'})
            

# Views

if __name__ == '__main__':
    app.run(port=5555, debug=True)