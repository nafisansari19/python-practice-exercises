# Create an Object:

from user import User
from post import Post

app_user_one = User("nafis.ansari@email.com", "Nafis Ansari", "pwd1", "QA Engineer")
app_user_one.get_user_info()

app_user_two = User("aa@aa.com", "john Doe", "pwd2", "Junior Devops Engineer")
app_user_two.get_user_info()

new_post = Post("I am currently learning Python", app_user_one.name)
new_post.get_post_info()