import os
import json

class FileStorage:  

    __file_path = "data.json"
    __objects = {}


    def all(self):
        return self.__objects

    def new(self, obj):
        obj_class = obj.__class__.__name__
        obj_id = obj.id
        key = f"{obj_class}.{obj_id}"
        self.__objects[key] = obj.to_dict()



       # obj_key = print("{}.{}".format(obj_class, obj_id))
        #self.__object[obj_key] = obj

        


    def save(self):
        serialised_obj = json.dumps(self__objects)
        with open(self.__file_path, 'w') as file:
            file.write(serialised_obj)


    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_file = file.read() #reads the entire file
                deserialised_file = json.load(json_file)
                self.__objects.update(deserialised_file) #update the __object attri
