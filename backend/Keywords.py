class Keywords():
    def __init__(self, Item):
        self.Item = Item
        self.match = False
        self.matchedItems = []

    # iterates through the AIDescription keywords and see if it matches a given searchWord -- provided from front end
    def searchMatch(self, searchWord):
        for word in self.Item.getKeywords():
            if searchWord == word:
                self.match = True
                self.matchedItems += [self.Item]

    def hasMatch(self):  
        return self.match

    # some other function to find the item that had the description. keyword --> AI description --> item
    