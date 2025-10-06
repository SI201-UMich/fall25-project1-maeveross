
# name: Maeve Ross
# uniqname + number: maever + 40315854
# name of dataset: penguins.csv
# columns working with: species, island, flipper_length_mm, sex          
# calculations to be performed: 
#.          1 - Which species had the greatest flipper length?
#           2 - How many females were on each island? 
# diagrams are in submission #2 from figma link

def get_file (file1):
    open_file = open (file1, 'r')
    file_content= open_file.read()
    # print (file_content) #prints entire file in multiple line
    # column_names = open_file.readline().strip().split(",") # list of names of columns
    # print (column_names)
    # Split into lines, then split each line by commas
    
    # list of lists where each list is an entry
    lines = file_content.strip().split('\n')
    result = []
    for line in lines: 
        parts = line.strip().split(',')  # split each line into a list
        result.append(parts)             # add to the overall list

    print (result)

        
get_file ('penguins.csv')



