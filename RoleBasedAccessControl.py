#!/usr/bin/python3



from rbac.acl import Registry

ACCESS_LEVELS = {
    'super-admin': ['READ', 'WRITE', 'DELETE'],
    'admin': ['READ', 'WRITE'],
    'non-admin': ['READ']
}


RESOURCES = ['file']


class RBAC:
   

    def __init__(self):
    
        self.acl = Registry()

    def add_role(self):
        
        for role, access_levels in ACCESS_LEVELS.items():
            self.acl.addRole(role, access_levels)

    def add_resource(self):
        
        for resource in RESOURCES:
            self.acl.addResource(resource)

    def allow_rule(self):
        
        for role, access_levels in ACCESS_LEVELS.items():
            for acl in access_levels:
               
                self.acl.allow(role, acl, RESOURCES)

    def deny_rule(self):
        
        for role, access_levels in ACCESS_LEVELS.items():
    
            for acl in ACCESS_LEVELS['super-admin']:
                if acl not in access_levels:
                    
                    self.acl.deny(role, acl, RESOURCES)

    def add_users(self):
       
        self.acl.addUser('shasank', ['non-admin', 'admin'])
        self.acl.addUser('user', ['super-admin'])

    def perform_operations(self):
        
        self.acl.isAllowed('shasank', 'READ', 'file')
        self.acl.isAllowed('shasank', 'WRITE', 'file')

        
        self.acl.deleteRole('shasank', 'admin')

        self.acl.isAllowed('shasank', 'READ', 'file')
        self.acl.isAllowed('shasank', 'WRITE', 'file')


if __name__ == "__main__":
    rbac = RBAC()
    rbac.add_role()
    rbac.add_resource()
    rbac.allow_rule()
    rbac.deny_rule()
    rbac.add_users()
    rbac.perform_operations()
