#Python code to get value for specific key from object
objects = {"w":{"x":{"y":{"z":"a"}}}}

def get_value(objects, key):
    if key in objects.keys():
        return objects[key]
        
    for value in objects.values():
        if isinstance(value, dict):
            response = get_value(value, key)
            if response is not None:
                return response

print(get_value(objects, 'z'))                    
