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
    
class Artist(DefaultBase):
    __tablename__ = 'artists'

    username = db.Column(db.String, unique=True, nullable=False)
    _password = db.Column(db.String, nullable=False)

    name = db.Column(db.String, nullable=False)
    bio = db.Column(db.Text)
    _email_address = db.column(db.String)

class Piece(DefaultBase):
    __tablename__ = 'pieces'

    title = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Integer)

class Article(DefaultBase):
    __tablename__ = 'articles'

    title = db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)


