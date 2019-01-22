# coding: utf-8

from google.cloud import datastore


class UserRepository:
    _instances = {}

    def __init__(self, env):
        project = env.PROJECT
        namespace = env.DATASTORE_NAMESPACE
        self.client = datastore.Client(project=project, namespace=namespace)

    @classmethod
    def get_instance(cls, env):
        if env.ENV not in cls._instances:
            cls._instances[env.ENV] = UserRepository(env)
        return cls._instances[env.ENV]

    def add_user(self, user):
        key = self.client.key('User')
        entity = datastore.Entity(key)
        entity.update({
            'name': user.name,
            'email': user.email,
            'password': user.password,
            'description': user.description,
            'following': user.following,
            'created_at': user.created_at,
            'modified_at': user.modified_at
        })

        self.client.put(entity)
        user.id = user.key.id
        return user

