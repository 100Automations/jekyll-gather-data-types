from process_collection import ProcessCollection
from process_dictionary import ProcessDictionary
from spreadsheet import Spreadsheet
import argparse
import json

def gather_collection_data_types(target_directory):
    """
    Iterates through all files in target_directory and collects
    all used data types and stores this information in ./dataTypes.marshal

    Paramaters
    ----------
    target_directory: string 
        string holding the directory path to directory with collection files to be parsed

    Returns
    -------
    Nothing
    """
    pc = ProcessCollection(target_directory)
    pc.gather_used_types()
    pc.export_marshal_data()

def data_types_report(is_spreadsheet = False, output_directory = './', output_name = 'data-types'):
    """
    Uses data type information stored in ./dataTypes.marshal to generate a JSON report of
    All Data Types, Unused Data Types, and Missing Data Types in collection.

    Paramaters
    ----------
    None

    Returns
    -------
    string:
        JSON string of All Data Types, Unused Data Types, and Missing Data Types in collection.
    """
    if not output_directory:
        output_directory = './'
    
    if not output_name:
        output_name = 'data-types'

    pc = ProcessCollection()
    pc.import_marshal_data()

    json_dict = json.loads(pc.gather_missing_unused_data_types())

    if is_spreadsheet:
        spreadsheet = Spreadsheet(output_directory, output_name)
        spreadsheet.json_to_spreadsheet(json_dict)
    
    return json_dict

def validate_through_template_report(target_directory, 
                                     is_spreadsheet = False, output_directory = './', 
                                     output_name = 'template-data-types'):

    if not output_directory:
        output_directory = './'
    
    if not output_name:
        output_name = 'template-data-types'

    pc = ProcessCollection(target_directory)
    json_dict = json.loads(pc.gather_important_missing_untracked_data_types("./template.md"))

    if is_spreadsheet:
        spreadsheet = Spreadsheet(output_directory, output_name)
        spreadsheet.json_to_spreadsheet(json_dict)
    
    return json_dict

if __name__ == '__main__':
    argumentParser = argparse.ArgumentParser(description='Generate spreadsheet or json of data types used and missing from jekyll collection')
    argumentParser.add_argument('-x',
                                action='store_true',
                                help='Enables spreadsheet output (.xlsx)')

    argumentParser.add_argument('-d',
                                metavar='output_directory',
                                type=str,
                                nargs='?',
                                help='Path to output')

    argumentParser.add_argument('-o',
                                metavar='output_name',
                                type=str,
                                nargs='?',
                                help='name for spreadsheetfile -> [output_name].xlsx')
    
    argumentParser.add_argument('-i',
                            metavar='target_directory',
                            type=str,
                            nargs='?',
                            help='directory of jekyll collection to be parsed',
                            default=None)

    argumentParser.add_argument('-j', 
                                action='store_true',
                                help='Enables JSON output')

    argumentParser.add_argument('-t',
                            metavar='target_directory',
                            type=str,
                            nargs='?',
                            help='directory of jekyll collection to be parsed and compared to template',
                            default=None)

    args = argumentParser.parse_args()

    is_spreadsheet = True if args.x else False
    is_json = True if args.j else False

    if args.i:
        gather_collection_data_types(args.i)
    elif args.t:
        json_dict = validate_through_template_report(args.t, args.x, args.d, args.o)

        if not args.x or args.j:
            print(json_dict)
    elif args.j or args.x:
        json_dict = data_types_report(is_spreadsheet, args.d, args.o)
        
        if not args.x or args.j:
            print(json_dict)
    else:
        print("Missing flag: Use -h flag for help")