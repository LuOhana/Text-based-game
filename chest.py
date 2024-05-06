#IN PROGRESS...
class Chest:
    def __init__ (self, chest_type):
        self.type = chest_type
        self.chestinfo = None
        self.content = None

    def set_type (self, chest_type):
        self.type = chest_type

    def get_type (self):
        return self.type

    def set_chestinfo(self, chest_description):
        self.chestinfo = chest_description

    def get_chestinfo(self):
        return self.chestinfo

    #def get_treasure(self, content):
        #return self.content[content]
    
    def set_treasure(self, chest_content):
        self.content = chest_content
    
    def get_treasure(self):
        return self.content
    
    
        