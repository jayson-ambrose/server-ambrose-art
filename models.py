from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property 

from config import db, bcrypt

class DefaultBase(db.Model, SerializerMixin):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Instance of {self.__class__.__name__}, ID: {self.id}>'
    
class User(DefaultBase):
    __tablename__ = 'users'

    username = db.Column(db.String, unique=True, nullable=False)
    _password = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean)
    
    articles = db.relationship('Article', backref='user', cascade='all, delete-orphan')
    messages = db.relationship('Message', backref='user', cascade='all, delete-orphan')

    artist = db.relationship('Artist', back_populates='user')
    
    # artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

    chats = association_proxy('messages', 'chats')

    @validates('password')
    def validate_password (self, key, password):
        if(4 > len(password) > 35):
            raise ValueError('Password must be between 5 and 34 characters long.')
        return password
        
    @validates('username')
    def validate_username (self, key, username):
        if(4 > len(username) > 16):
            raise ValueError('Username must be between 5 and 15 characters long.')
        return username
        
    @hybrid_property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        self._password = password_hash

    def auth(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
class Artist(DefaultBase):
    __tablename__ = 'artists'

    name = db.Column(db.String, nullable=False)
    bio = db.Column(db.Text)
    img_url = db.Column(db.String)

    pieces = db.relationship('Piece', backref='artist', cascade='all, delete-orphan')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='artist')


class Piece(DefaultBase):
    __tablename__ = 'pieces'

    title = db.Column(db.String, unique=True, nullable=False)
    img_url = db.Column(db.String)
    price = db.Column(db.Integer)

    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))

class Article(DefaultBase):
    __tablename__ = 'articles'

    title = db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)  
    archived = db.Column(db.Boolean)
    img_url = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Message(DefaultBase):
    __tablename__ = 'messages'

    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'))

class Chat(DefaultBase):
    __tablename__ = 'chats'

    messages = db.relationship('Message', backref='chat', cascade='all, delete-orphan')

    users = association_proxy('messages', 'user')








