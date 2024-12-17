## Class
class User:
    
    def __init__(self,user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0
        
        
    def follow(self, user):
        user.followers +=1
        self.following +=1
        
user = User("001", "C1djey")
user_2 = User("002", "Heusx")
user.follow(user_2)

print(user_2.followers)
print(user.following)