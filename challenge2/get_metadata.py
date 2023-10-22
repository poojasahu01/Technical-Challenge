import requests
import json

#default API to get metadata of instance
url = 'http://169.254.169.254/latest/'


def call_api(url,data_list):
    output_return = {}
    for data in data_list:
        new_url = url+data
        response = requests.get(new_url)
        response_text = response.text
        if data[-1] == '/':
            #response_line = response_text.split("\n")
            response_line = response_text.splitlines()
            output_return[data[:-1]] = call_api(new_url, response_line)
        elif check_json(response_text):
            output_return[data] = json.loads(response_text)
        else:
            output_return[data] = response_text
    return output_return

def get_metadata(metadata_list):
    metadata_lists = [metadata_list]
    metadata_return = call_api(url, metadata_lists)
    metadata_str = json.dumps(metadata_return, indent=4, sort_keys=True)
    return metadata_str


def check_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True
        

if __name__ == '__main__':
    response_metadata = get_metadata('meta-data/')
    response_dynamic = get_metadata('dynamic/')
    print(response_metadata)
    print(response_dynamic)


