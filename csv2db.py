import csv
import os
from pprint import pprint as pp
from termcolor import cprint
from tqdm import tqdm
from database.operations import insert_db_data
os.system('color')

# Just print some info that we're starting (in green)
cprint(f'\n Processing CSV file...', 'green', attrs=['reverse'])

# Get amount of lines in CSV file
num_lines = sum(1 for line in open('data.csv', encoding="utf-8"))

# start progress bar
with tqdm (total=num_lines) as pbar:
    
    # Open CSV file in UTF-8
    with open('data.csv', encoding="utf-8") as csv_file:
        
        # Parse CSV file using csv reader (csv module in python)
        csv_reader = csv.reader(csv_file, delimiter=';')
        
        # line_count will hold line number we're currently at
        line_count = 0

        # for loop where we parse the data
        for row in csv_reader:

            # if line_count is 0 then skip (first row is title)
            if line_count != 0:
                
                # Create SQL query using sqlalchemy params
                result = insert_db_data(name=row[0], address=row[1], postcode=row[2], city=row[3], date=row[5], type=row[6], businessid=row[7])

                if result==False:
                    cprint(f'\n Could not save this row', 'red', attrs=['reverse'])
                
                # add 1 to line_count since we processed this row
                line_count += 1
                
                # update progress bar
                pbar.update(1)
            else:
                
                # add 1 to line_count since we processed this row
                line_count +=1

# close progress bar
pbar.close()

# Output info that we're done!
cprint(f'\n Processed successfully {line_count}', 'green', attrs=['reverse'])