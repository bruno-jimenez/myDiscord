class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.channels = []

#[--------------------------]
#   join and leave channel
#[--------------------------]

    def join_channel(self, channel):
        self.channels.append(channel)
    
    def leave_channel(self, channel):
        self.channels.remove(channel)