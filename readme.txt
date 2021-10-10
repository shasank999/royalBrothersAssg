Role Based Access Control


 Assumptions:
1. Only one system resource 'file'     
2. Roles:   
	a. non-admin having READ access     
	b. admin having read and write access      
	c. super-admin having read, write and delete access         
3. In-memory database for storing users, roles, resources, allowed and denied. 
4. No previous role has been assigned     

 How to run:
$ python3 RoleBasedAccessControl.py