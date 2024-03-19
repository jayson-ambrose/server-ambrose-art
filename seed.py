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

        a1 = Artist(name='Maggie Smith', bio='lorem ipsum dolor...', img_url='https://cdn.imgchest.com/files/d7ogcna9g2y.jpg', user_id=2)
        a2 = Artist(name='Roger Ambrose', bio='lorem ipsum dolor...', img_url='https://cdn.imgchest.com/files/w7pjconezv7.jpg', user_id=3)

        artist_list = [a1, a2]

        db.session.add_all(artist_list)
        db.session.commit()

        print('--ARTISTS GENERATED--')
        print('--GENERATING ARTICLES')

        ar1 = Article(title='Test Article #1', 
                      start_date=datetime.date(2023, 12, 22),
                      end_date=datetime.date(2024, 12, 22),
                      archived=False,
                      img_url=None,
                      user_id=1,
                      text= '''
                          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                          incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                          exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
                          irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
                          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
                          deserunt mollit anim id est laborum
                      ''')
        
        ar2 = Article(title='Test Article #2', 
                      start_date=datetime.date(2023, 12, 22),
                      end_date=datetime.date(2024, 12, 22),
                      archived=False,
                      img_url='https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ce84cd7d-bdf1-4f7a-8855-757550baba4f/d6oidgs-bbb8124b-3f0e-480b-822e-784af866b308.jpg/v1/fit/w_828,h_1250,q_70,strp/pickle_man_by_xmasdog_d6oidgs-414w-2x.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2NlODRjZDdkLWJkZjEtNGY3YS04ODU1LTc1NzU1MGJhYmE0ZlwvZDZvaWRncy1iYmI4MTI0Yi0zZjBlLTQ4MGItODIyZS03ODRhZjg2NmIzMDguanBnIiwiaGVpZ2h0IjoiPD0xMzU5Iiwid2lkdGgiOiI8PTkwMCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS53YXRlcm1hcmsiXSwid21rIjp7InBhdGgiOiJcL3dtXC9jZTg0Y2Q3ZC1iZGYxLTRmN2EtODg1NS03NTc1NTBiYWJhNGZcL3htYXNkb2ctNC5wbmciLCJvcGFjaXR5Ijo5NSwicHJvcG9ydGlvbnMiOjAuNDUsImdyYXZpdHkiOiJjZW50ZXIifX0.BXtK154VCSYIDq8YY-2NOAGr6Y8QcBIE5ww7MEPj-6k',
                      user_id=2,
                      text= '''
                          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                          incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                          exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
                          irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
                          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
                          deserunt mollit anim id est laborum
                      ''')
        
        ar3 = Article(title='Test Article #3', 
                      start_date=datetime.date(2023, 12, 22),
                      end_date=datetime.date(2024, 12, 22),
                      archived=True,
                      img_url=None,
                      user_id=1,
                      text= '''
                          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                          incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                          exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
                          irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
                          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
                          deserunt mollit anim id est laborum
                      ''')
        
        
        article_list = [ar1, ar2, ar3]

        db.session.add_all(article_list)
        db.session.commit()

        print('--ARTICLES GENERATED--')
        print('--GENERATING PIECES--')

        p1 = Piece(title='Piece #1', 
                   img_url='https://cdn.imgchest.com/files/my2pclnb8b7.png',
                   price=20000,
                   category='watercolor',
                   sold=False,
                   artist_id=1)
        
        p2 = Piece(title='Piece #2', 
                   img_url='https://cdn.imgchest.com/files/my2pclnb8b7.png',
                   price=23000,
                   category='watercolor',
                   sold=False,
                   artist_id=1)
        
        p3 = Piece(title='Piece #3', 
                   img_url='https://cdn.imgchest.com/files/84jdc8olwg4.png',
                   price=15000,
                   category='acrylic',
                   sold=False,
                   artist_id=2)
        
        p4 = Piece(title='Piece #4', 
                   img_url='https://cdn.imgchest.com/files/my2pclnb8b7.png',
                   price=45000,
                   category='oil',
                   sold=False,
                   artist_id=2)
        
        p5 = Piece(title='Piece #5', 
                   img_url='https://cdn.imgchest.com/files/84jdc8olwg4.png',
                   price=18500,
                   category='oil',
                   sold=False,
                   artist_id=2)
        
        p6 = Piece(title='Piece #6', 
                   img_url='https://cdn.imgchest.com/files/my2pclnb8b7.png',
                   price=17500,
                   category='watercolor',
                   sold=True,
                   artist_id=1)


        piece_list = [p1, p2, p3, p4, p5, p6]

        db.session.add_all(piece_list)
        db.session.commit()

        print('--PIECES GENERATED--')





