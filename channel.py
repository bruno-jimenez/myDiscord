class Channel:
    def __init__(self, name, is_public):
        self.name = name
        self.is_public = is_public
        self.messages = []
        self.users = []
    
    def add_message(self, message):
        self.messages.append(message)
    
    def add_user(self, user):
        self.users.append(user)
    
    def remove_user(self, user):
        self.users.remove(user)