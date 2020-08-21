import os
import yaml
import marshal
import sys
from refactor.process_dictionary import ProcessDictionary

class ProcessCollection:
    def __init__(self, directory_path):
        self.__directory_path = directory_path
        self.__used_data_types = set()
        self.__nested_dictionary = dict()

    def parse_collection(self):
        pd = ProcessDictionary()
        directory = r'' + self.__directory_path

        for filename in os.listdir(directory):
            if filename.endswith(".md"):
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
    
    def export_marshal_data(self, file_path = "./dataTypes.marshal"):
        storage_file = open(file_path, 'wb')
        marshal.dump(self.__directory_path, storage_file)
        marshal.dump(self.__used_data_types, storage_file)
        marshal.dump(self.__nested_dictionary, storage_file)
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