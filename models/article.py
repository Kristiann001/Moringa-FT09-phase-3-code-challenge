class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

@property 
def title(self):
    return self.title

@title.setter
def title(self,title):
    if not isinstance(title , str):
        raise ValueError("Title must be a string")
    if len(title) < 5 or len(title) > 50:
        raise ValueError("Title must be between 5 and 50 characters")
    
    self.title = title

    def __repr__(self):
        return f'<Article {self.title}>'
