from datetime import datet:me
from uuid import uuid4

class BaseModel:

    def __init__(self):
        current_time = datetime.now()
        self.id = str(uuid4())
        self.created_at = current_time
        self.updated_at = current_time

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        instance_dict = self.__dict__.copy()
        instance_dict['class'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
