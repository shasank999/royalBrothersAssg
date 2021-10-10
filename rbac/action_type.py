#!/usr/bin/python3


from rbac.users import Users
from rbac.roles import Roles
from rbac.resources import Resources


class ActionType(Users, Roles, Resources):

    def __init__(self):
        super().__init__()
        
        self.action_types = ['READ', 'WRITE', 'DELETE']
        self.allowed = {}
        self.denied = {}

    def allow(self, role, action_type, resources=[]):
        
        assert not role or role in self.roles
        assert not action_type or action_type in self.action_types
        for resource in resources:
            assert not resource or resource in self.resources
            self.allowed[role, action_type.upper(), resource] = True

    def deny(self, role, action_type, resources=[]):
        
        assert not role or role in self.roles
        assert not action_type or action_type in self.action_types
        for resource in resources:
            assert not resource or resource in self.resources
            self.denied[role, action_type.upper(), resource] = True
