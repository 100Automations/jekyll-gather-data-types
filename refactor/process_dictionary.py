class ProcessDictionary:
    def __init__(self):
        self.__key_set = set()
    
    
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
    
    def get_key_set(self):
        return self.__key_set.copy()
    
    def set_key_set(self, key_set):
        self.__key_set = key_set

    