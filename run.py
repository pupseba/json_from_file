#! /usr/bin/env python3

import os, requests

def listall(directory):
    """returns a list with all files and directories under the given path provided as argument"""
    filelist = []
    for i in os.listdir(directory):
        filelist.append(i)
    return filelist

def createdict(file):
    """returns a dictionary with the contents of a file. The file should have a title, name, date and feedback info in separate lines"""
    request_dict = {}
    keys = ["title", "name", "date", "feedback"]
    temp_list = []
    with open(file, "r") as f:
        for line in f.readlines():
            new_line = line.replace("\n", "")
            temp_list.append(new_line)
    return dict(zip(keys, temp_list))

if __name__ == "__main__":
    source_path = "/data/feedback/"
    lista = listall(source_path)
    url = "34.69.9.40"
    for i in lista:
        feedback = createdict(source_path + i)
        response = requests.post("http://" + url + "/feedback/", json=feedback)
        print(response.request.body)
        print(response.status_code)
#        print(createdict(source_path + i))

