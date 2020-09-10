import os
import yaml
import marshal
import json
from process_dictionary import ProcessDictionary

class ProcessCollection:
    def __init__(self, directory_path = None):
        if directory_path and directory_path.endswith('/') == False:
            directory_path = directory_path + '/'
        self.__directory_path = directory_path
        self.__used_data_types = set()
        self.__nested_dictionary = dict()
        self.__data_types_JSON = dict()

    def gather_used_types(self):
        """
        Gathers all data types used in collection found in __directory_path
        All used data types are stored in a set __used_data_types
        Nested data types are stored in a nested dictionary __nested_dictionary

        Paramaters
        ----------
        None

        Returns
        -------
        Nothing
        """
        pd = ProcessDictionary()
        directory = r'' + self.__directory_path

        for filename in os.listdir(directory):
            data = self.parse_collection_file(filename)

            if not data:
                continue

            for dictionary in data:
                if(dictionary):
                    pd.gather_dictionary_keys(dictionary)

        self.__used_data_types = pd.get_key_set()
        self.__nested_dictionary = pd.generate_nested_dictionary()
    
    def gather_missing_unused_data_types(self):
        """
        Given __used_data_types and __nested_dictionary generate sets of unused and missing
        data types in __directory_path. 
        
        Generates a JSON string of All Data Types, Unused Data Types, and Missing Data Types in collection.

        Paramaters
        ----------
        None

        Returns
        -------
        string:
            Outputs JSON formatted string with
            All Data Types, Unused Data Types, and Missing Data Types in collection.
        """
        pd = ProcessDictionary()
        pd.set_nested_key_dict(self.__nested_dictionary)
        directory = r'' + self.__directory_path

        self.__data_types_JSON['All Data Types'] = list(self.__used_data_types)
        self.__data_types_JSON['Unused Data Types'] = dict()
        self.__data_types_JSON['Missing Data Types'] = dict()

        for filename in os.listdir(directory):
            data = self.parse_collection_file(filename)

            if not data:
                continue

            pd.set_missing_key_set(set())
            pd.set_key_set(set())

            for dictionary in data:
                if(dictionary):
                    pd.gather_unused_missing_keys(dictionary)

            unused_data_types = self.__used_data_types - pd.get_key_set()

            if unused_data_types:
                self.__data_types_JSON['Unused Data Types'][os.path.splitext(filename)[0]] = list(unused_data_types)
            if pd.get_missing_key_set():
                self.__data_types_JSON['Missing Data Types'][os.path.splitext(filename)[0]] = list(pd.get_missing_key_set())
        
        return json.dumps(self.__data_types_JSON)

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
    
    def parse_collection_file(self, filename):
        if filename.endswith(".md") == False:
            return None
        try:
            md_file = open(self.__directory_path + filename, 'r')
        except:
            print("Failed to open " + filename + "\n")
            return None
        try:
            data = list()
            data_object = yaml.load_all(md_file)
            for dictionary in data_object:
                data.append(dictionary)
        except:
            print("yaml failed to parse " + filename + "\n")
            md_file.close()
            return None
        
        md_file.close()
        return data

    def set_directory_path(self, directory_path):
        if directory_path and directory_path.endswith('/') == False:
            directory_path = directory_path + '/'
        else:
            return
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