class Task:
    def __init__(self, name,description,duedate,complete=False):
        self.name = name
        self.description = description
        self.complete=complete
        self.duedate=duedate

    def to_dict(self):
        return {'name':self.name,
                'description':self.description,
                'duedate':self.duedate,
                'complete':self.complete}






