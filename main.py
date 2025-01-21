
# sample input to run the project 
# python main.py --dir input --outfile testfile

import argparse
from load_json import process_files



if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(description='Json parser, to get unique keys across multiple jsons')
    argument_parser.add_argument('--dir', 
                                type=str, 
                                # required=True, 
                                help='Directory where input json files are present')
    argument_parser.add_argument('--outfile', 
                                type=str, 
                                # required=True, 
                                help='Output file name, do not add extention',
                                default='testfile')
    argument_parser.add_argument('--e', 
                                # '--extract',
                                # required=True, 
                                help='Option to extract keys')
    argument_parser.add_argument('srch', 
                                # '--search',
                                # required=True, 
                                help='Option to search for keys in all json files')
    argument_parser.add_argument('--search-strings', 
                                type=str,
                                # required=True, 
                                help='Option to search for keys in all json files')
    
    
    arguments = vars(argument_parser.parse_args())
    # print (arguments)
    # print (arguments['dir'])

    expand_json = False
    search_json = False
    if arguments.get('e'):
        expand_json = True
    
    if arguments.get('srch'):
        search_json = True


    if arguments.get('dir'):
        # If the directory name ends in '/' then use that, else add '/' to input directory name
        input_directory = arguments['dir'] if arguments['dir'][-1] == '/' else arguments['dir'] + '/'
    else:
        raise Exception ("Mandatory parameter '--dir' is missing.")

    output_file_ptr = None
    if expand_json:
        if arguments.get('outfile'):
            # If the directory name ends in '/' then use that, else add '/' to input directory name
            out_file_name = 'output/' + arguments['outfile'].replace(' ', '_').replace('.', '_') + '.txt'
            output_file_ptr = open(out_file_name, 'w')
        else:
            raise Exception ("Mandatory parameter '--outfile' is missing.")
    
    search_keys = ''
    if search_json:
        if arguments.get('search-strings'):
            search_keys = arguments['search-strings']

    
    process_files(input_directory, output_file_ptr, search_json, search_keys)
    


