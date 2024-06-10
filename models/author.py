class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

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
    if isinstance(value, str) and len(value) > 0 :
        if not hasattr(self, 'name'):
            self.name = value
        else:
            raise ValueError("Name must be a non-empty string")

    def __repr__(self):
        return f'<Author {self.name}>'
