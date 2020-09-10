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

def json_data_types_report():
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
    pc = ProcessCollection()
    pc.import_marshal_data()

    return json.loads(pc.gather_missing_unused_data_types())

def spreadsheet_data_types_report(output_directory = './', output_name = 'data-types'):
    """
    Uses data type information stored in ./dataTypes.marshal to generate a .xlsx spreadsheet report of
    All Data Types, Unused Data Types, and Missing Data Types in collection.

    Paramaters
    ----------
    output_directory: string
        path to directory where .xlsx file will be output

    output_name

    Returns: string
        name to give .xlsx file to be output in output_directory
        
    -------
    Nothing
    """
    pc = ProcessCollection()
    pc.import_marshal_data()

    json_dict = json.loads(pc.gather_missing_unused_data_types())

    spreadsheet = Spreadsheet(output_directory, output_name)
    spreadsheet.json_to_spreadsheet(json_dict)

if __name__ == '__main__':
    argumentParser = argparse.ArgumentParser(description='Generate spreadsheet or json of data types used and missing from jekyll collection')
    argumentParser.add_argument('-x',
                                action='store_true',
                                help='Enables spreadsheet output (.xlsx)')

    argumentParser.add_argument('-d',
                                metavar='output_directory',
                                type=str,
                                nargs='?',
                                help='Path to output',
                                default='./')

    argumentParser.add_argument('-o',
                                metavar='output_name',
                                type=str,
                                nargs='?',
                                help='name for spreadsheetfile -> [output_name].xlsx',
                                default='data-types')
    
    argumentParser.add_argument('-i',
                            metavar='target_directory',
                            type=str,
                            nargs='?',
                            help='directory of jekyll collection to be parsed',
                            default=None)

    argumentParser.add_argument('-j', 
                                action='store_true',
                                help='Enables JSON output')

    args = argumentParser.parse_args()

    if args.i:
        gather_collection_data_types(args.i)
    elif args.j:
        print(json_data_types_report())
    elif args.x:
        spreadsheet_data_types_report(args.d, args.o)