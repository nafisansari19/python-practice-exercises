#1. Object has been created with initial values
#2. Call function on that object to change its password

class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title


        #creating methods:
    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as {self.current_job_title}. You can contact them at {self.email}")





#app_user_one.change_job_title("Aspiring Devops Engineer")
#app_user_one.get_user_info()

"""
That is how we can create a new object from a class and we can use methods of
that class by first saving that object into a variable and then calling that function
on that variable
"""

