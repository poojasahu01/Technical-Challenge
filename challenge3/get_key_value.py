#Python code to get key and value from object

objects = {"w":{"x":{"y":{"z":"a"}}}}
store_keys = ''
store_values = ''

def check_key_values(objects):
    
    for key,value in objects.items():
        global store_keys
        store_keys += (key + "/")
        if isinstance(value, dict):
           check_key_values(value)
        else:
            global store_values
            store_values = value
        return store_keys, store_values
keys, values = check_key_values(objects)
print("keys: ", keys[:-1])
print("values: ", values)
