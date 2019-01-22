# coding: utf-8
import hashlib
from datetime import datetime


class User:
    def __init__(self,
                 id,
                 name,
                 email,
                 password,
                 description=None,
                 following=None,
                 icon=None,
                 background=None,
                 created_at=None,
                 modified_at=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.description = description if description else ''
        self.following = following if following else []
        self.icon = icon
        self.background = background
        self.created_at = created_at if created_at else datetime.now()
        self.modified_at = modified_at if modified_at else datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            # 'password': self.password,
            'description': self.description,
            'following': self.following,
            'icon': self.icon,
            'background': self.background,
            'created_at': self.created_at.isoformat(),  # TODO Presenter
            'modified_at': self.modified_at.isoformat()
        }


class UserConstants:
    MIN_NAME_LENGTH = 3
    MIN_PASSWORD_LENGTH = 8


def hash_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode('UTF-8'))

    return md5.hexdigest()
