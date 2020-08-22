class ProcessDictionary:
    def __init__(self):
        self.__key_set = set()
        self.__missing_key_set = set()
        self.__nested_key_dict = dict()
    
    
    def gather_dictionary_keys(self, dictionary, prefix = ""):
        """
        Adds all keys in the dictionary to __key_set. 
        If the dictionary has nested entries, 
        the keys are concatenated recursively in comma deliminated form.

        Paramaters
        ----------
        dictionary: dictionary 
            processed and keys added to __key_set

        prefix: string 
            used to track parent keys deliminated by commas during recursive calls

        Returns
        -------
        Nothing
        """
        for k,v in dictionary.items():
                if(prefix):
                    self.__key_set.add(prefix + "," + k)
                else:
                    self.__key_set.add(k)

                if type(v) is dict:
                    self.gather_dictionary_keys(v, prefix + "," + k if prefix else k)
                
                if type(v) is list:
                    for item in v:
                        if type(item) is dict:
                            self.gather_dictionary_keys(item, prefix + "," + k if prefix else k)

    def generate_nested_dictionary(self):
        """
        Expands all comma deliminated keys in __key_set into a nested dictionary.

        Paramaters
        ----------
        None

        Returns
        -------
        dictionary:
            a nested dictionary containing all comma deliminated entries in __key_set
            with empty dictionaries as the final values.
        """
        nested_dictionary = dict()
        for key in self.__key_set:
            if "," in key :
                key_list = key.split(",")
                # current_dictionary is used to traverse nested_dictionary
                current_dictionary = nested_dictionary
                for item in key_list:
                    if item in current_dictionary.keys():
                        current_dictionary = current_dictionary[item]
                    else:
                        current_dictionary[item] = dict()
                        current_dictionary = current_dictionary[item]
        return nested_dictionary
    
    def __gather_missing_keys(self, dictionary, prefix, k, v):
        prefix_list = (prefix + k).split(",")
        if(self.__nested_key_dict[prefix_list[0]]):
            current_set = set(dictionary.keys())
            expected_set = set()
            data_type_dictionary = dict(self.__nested_key_dict)

            for key in prefix_list:
                data_type_dictionary = data_type_dictionary[key]

            expected_set = set(data_type_dictionary.keys())
            current_set = expected_set - current_set
            
            for key in current_set:
                self.__missing_key_set.add(prefix + k + ": " + key)

    def gather_unused_missing_keys(self, dictionary, prefix = ""):
        for k,v in dictionary.items():
            if(prefix):
                self.__key_set.add(prefix + "," + k)
            else:
                self.__key_set.add(k)

            if type(v) is dict:
                self.gather_unused_missing_keys(v, prefix + "," + k if prefix else k)
            
            if type(v) is list:
                for item in v:
                    if type(item) is dict:
                        self.__gather_missing_keys(item, prefix, k, v)
                        self.gather_unused_missing_keys(item, prefix + "," + k if prefix else k)
    
    def get_key_set(self):
        return self.__key_set.copy()
    
    def set_key_set(self, key_set):
        self.__key_set = key_set
    
    def set_missing_key_set(self, missing_key_set):
        self.__missing_key_set = missing_key_set
    
    def get_missing_key_set(self):
        return self.__missing_key_set

    def get_nested_key_dict(self):
        return self.__nested_key_dict
    
    def set_nested_key_dict(self, nested_key_dict):
        self.__nested_key_dict = nested_key_dict
    