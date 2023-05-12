
class TVController:

    channel_now = 0

    def __init__(self, channels):

        self.channels = channels

    def first_channel(self):
        self.current_channel = 0
        return f"First channel --> {self.channels[0]}"

    def last_channel(self):
        TVController.current_channel = len(self.channels)
        return f"Last channel --> {self.channels[-1]}"
    
    def turn_channel(self, num):
        try:
            self.channels[num-1]
            TVController.current_channel = num
            return self.channels[num-1]
        except IndexError:
            print("There is no this channel")
            
    def next_channel(self):
        if TVController.channel_now == self.channels.index(self.channels[-1]):
            TVController.channel_now = 0
            return self.channels[0]
        else:
            TVController.channel_now = self.channels.index(self.channels[TVController.channel_now + 1])
            return self.channels[TVController.channel_now]
        
    def previous_channel(self):
        if TVController.channel_now == self.channels.index(self.channels[0]):
            TVController.channel_now = self.channels.index(self.channels[-1])
            return self.channels[-1]
        else:
            TVController.channel_now = self.channels.index(self.channels[TVController.channel_now - 1])
            return self.channels[TVController.channel_now]

    def current_channel(self):
        return f"Current channel --> {TVController.channel_now + 1}"
        
    def is_exist(self, name):
        if isinstance(name, str):
            if name in self.channels: 
                return "Yes"
            else:
                return "No" 
        elif isinstance(name, int):
            if name-1 in range(len(self.channels)):
                return "Yes"
            else:
                return "No" 
        else:
            raise ValueError("Wrong data type")
        




tv = TVController(["BBC", "Discovery", "TV1000"])

print(tv.first_channel())
print(tv.last_channel())
print(tv.next_channel())
# print(tv.previous_channel())
# print(tv.current_channel())
print(tv.is_exist(3))
print(tv.is_exist("TV12000"))








        
