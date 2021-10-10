#!/usr/bin/python3

# Entity Users.


class Users:
    """
    It implements add user with roles in an in-memory DB.
    """

    def __init__(self):
        super().__init__()
        
        self.users = {}

    def addUser(self, user, roles=[]):

        for role in roles:
            assert not role or role in self.roles

        self.users.setdefault(user, set())
        self.users[user].update(roles)
