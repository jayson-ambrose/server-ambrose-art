#!/usr/bin/env python3

import datetime
from random import randint, choice as rc

from faker import Faker

from config import app, db
from models import User, Artist, Article, Piece, Message, Chat, DefaultBase

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():

        print("--REMOVING OLD DATA--")

        User.query.delete()
        Artist.query.delete()
        Article.query.delete()
        Piece.query.delete()
        Message.query.delete()
        Chat.query.delete()

        db.session.commit()

        print('--OLD DATA DELETED--')
        print('--GENERATING USERS--')

        u1 = User(id=1, username='jambrose', password='password', admin=True)
        u2 = User(id=2, username='msmith', password='password', admin=True)
        u3 = User(id=3, username='rambrose', password='password', admin=True)

        user_list = [u1, u2, u3]

        db.session.add_all(user_list)
        db.session.commit()

        print('--USERS GENERATED--')
        print('--GENERATING ARTISTS--')

        a1 = Artist(name='Maggie Smith', bio='lorem ipsum dolar...', img_url='https://cdn.imgchest.com/files/d7ogcna9g2y.jpg', user_id=2)
        a2 = Artist(name='Roger Ambrose', bio='lorem ipsum dolar...', img_url='https://cdn.imgchest.com/files/w7pjconezv7.jpg', user_id=3)

        artist_list = [a1, a2]

        db.session.add_all(artist_list)
        db.session.commit()

        print('--ARTISTS GENERATED--')



