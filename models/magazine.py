class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

@property
def id(self):
    return self.id

@id.setter
def id(self,value):
    if isinstance(value, int) :
        self.id = value
    else:
        raise ValueError("id must be an integer")
    
@property
def name(self):
    return self.name

@name.setter
def name(self,value):
    if isinstance(value, str) :
        if not hasattr(self, 'name'):
            self.name = value
        else:
            raise ValueError("Name must be a non-empty string")
        
@property
def category(self):
    return self.category

@category.setter
def category(self,value):
    if isinstance(value, str) and 2 <= len(name) <= 15:
        self.category = category
    else:
        raise ValueError("Category must be a string with length between 2 and 15 characters")

    def __repr__(self):
        return f'<Magazine {self.name}>'

magazine = Magazine(1, "Tech Weekly", "Technology")