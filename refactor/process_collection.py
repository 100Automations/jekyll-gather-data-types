import os
import yaml
import marshal
import sys
import json
from process_dictionary import ProcessDictionary

class ProcessCollection:
    def __init__(self, directory_path):
        self.__directory_path = directory_path
        self.__used_data_types = set()
        self.__nested_dictionary = dict()
        self.__data_types_JSON = {}

    def gather_used_types(self):
        pd = ProcessDictionary()
        directory = r'' + self.__directory_path

        for filename in os.listdir(directory):
            if filename.endswith(".md") == False:
                continue
            try:
                md_file = open(self.__directory_path + filename, 'r')
            except:
                print("Failed to open " + filename + "\n")
                continue
            try:
                data = yaml.load_all(md_file)
            except:
                print("yaml failed to parse " + filename + "\n")
                md_file.close()
                continue
            for dictionary in data:
                if(dictionary):
                    pd.gather_dictionary_keys(dictionary)

            md_file.close()

        self.__used_data_types = pd.get_key_set()
        self.__nested_dictionary = pd.generate_nested_dictionary()
    
    def gather_missing_unused_data_types(self):
        pd = ProcessDictionary()
        pd.set_nested_key_dict(self.__nested_dictionary)
        directory = r'' + self.__directory_path

        self.__data_types_JSON['used_data_types'] = self.__used_data_types
        self.__data_types_JSON['unused_data_types'] = dict()
        self.__data_types_JSON['missing_data_types'] = dict()

        for filename in os.listdir(directory):
            if filename.endswith(".md") == False:
                continue
            try:
                md_file = open(self.__directory_path + filename, 'r')
            except:
                print("Failed to open " + filename + "\n")
                continue
            try:
                data = yaml.load_all(md_file)
            except:
                print("yaml failed to parse " + filename + "\n")
                md_file.close()

            pd.set_missing_key_set(set())
            pd.set_key_set(set())

            for dictionary in data:
                if(dictionary):
                    pd.gather_unused_missing_keys(dictionary)

            unused_data_types = self.__used_data_types - pd.get_key_set()

            if unused_data_types:
                self.__data_types_JSON['unused_data_types'][os.path.splitext(filename)[0]] = list(unused_data_types)
            if pd.get_missing_key_set():
                self.__data_types_JSON['missing_data_types'][os.path.splitext(filename)[0]] = list(pd.get_missing_key_set())
            if self.__used_data_types:
                self.__data_types_JSON['used_data_types'][os.path.splitext(filename)[0]] = list(self.__used_data_types)

            md_file.close()
        
        #return json.dumps(self.__data_types_JSON)
        return self.__data_types_JSON

    def export_marshal_data(self, file_path = "./dataTypes.marshal"):
        storage_file = open(file_path, 'wb')
        marshal.dump(self.__directory_path, storage_file)
        marshal.dump(self.__used_data_types, storage_file)
        marshal.dump(self.__nested_dictionary, storage_file)
        storage_file.close()
    
    def import_marshal_data(self, file_path = "./dataTypes.marshal"):
        storage_file = open("./dataTypes.marshal", 'rb')
        self.__directory_path = marshal.load(storage_file)
        self.__used_data_types = marshal.load(storage_file)
        self.__nested_dictionary = marshal.load(storage_file)
        storage_file.close()
    
    def set_directory_path(self, directory_path):
        self.__directory_path = directory_path
    
    def get_directory_path(self):
        return self.__directory_path

    def set_used_data_types(self, used_data_types):
        self.__used_data_types = used_data_types
    
    def get_used_data_types(self):
        return self.__used_data_types

    def set_nested_dictionary(self, nested_dictionary):
        self.__nested_dictionary = nested_dictionary
    
    def get_nested_dictionary(self):
        return self.__nested_dictionary