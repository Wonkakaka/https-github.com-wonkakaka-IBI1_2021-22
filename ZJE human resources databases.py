class staff():
# Create a new class called staff.
    def __init__(self, first_name, last_name, location, role):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.role = role
# Including their first and last name,their location and their role.
    def f(self):
        a = self.first_name + ' ' + self.last_name + ' ' + self.location + ' ' + self.role
        return a
        print(a)
# Collect and export information.
# For example:
Robot_Young = staff('Robot', 'Young', 'Edinburge', 'Faculty')
print(staff.f(Robot_Young))