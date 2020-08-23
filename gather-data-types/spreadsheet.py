from openpyxl import Workbook

class Spreadsheet:
    def __init__(self, file_path = './', file_name = 'DataTypes.xlsx'):
        if file_path.endswith('/'):
            self.__file_path = file_path
        else:
            self.__file_path = file_path + '/'
        
        if file_name.endswith('.xlsx'):
            self.__file_name = file_name
        else:
            self.__file_name = file_name + '.xlsx'
    
    def json_to_spreadsheet(self,json_dictionary):
        save_path = self.__file_path + self.__file_name

        workbook = Workbook()

        for k,v in json_dictionary.items():
            if workbook.active.title == 'Sheet':
                sheet = workbook.active
                sheet.title = k
            else:
                sheet = workbook.create_sheet(k)

            if type(v) is dict:
                for key,value in v.items():
                    for item in value:
                        sheet.append([key, item])
            elif type(v) is list:
                for data_type in v:
                    sheet.append([data_type])
        
        workbook.save(save_path)
    
    def set_file_path(self, file_path):
        if file_path.endswith('/'):
            self.__file_path = file_path
        else:
            self.__file_path = file_path + '/'
    
    def get_file_path(self):
        return self.__file_path
    
    def set_file_name(self, file_name):
        if file_name.endswith('.xlsx'):
            self.__file_name = file_name
        else:
            self.__file_name = file_name + '.xlsx'
    
    def get_file_name(self):
        return self.__file_name