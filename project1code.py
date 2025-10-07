
# name: Maeve Ross
# uniqname + number: maever + 40315854
# name of dataset: penguins.csv
# columns working with: species, island, flipper_length_mm, sex          
# calculations to be performed: 
#.          1 - Which species had the greatest flipper length?
#           2 - How many females were on each island? 
# diagrams are in submission #2 from figma link
import csv 

def load_penguin_data (file1):
    open_file = open (file1, 'r')
    file_content = csv.reader(open_file)
    print (file_content) #iterator that reads each row of your CSV file as a list of strings
    headers = next(file_content) # list of names of columns
    print (headers)

    # get each entry as a list
    if headers[0].strip() == "":
        headers[0] = "id"

    penguins = []
    for row in file_content:
        if not row:
            continue
            print (row)
        penguin = {}
        for i in range(len(headers)):
            key = headers[i]
            value = row[i].strip()

            # convert numbers where possible
            if key in ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]:
                if value.isdigit():  # checks if it’s a valid float string
                    penguin[key] = float(value) 
                else:
                    penguin[key] = None

            elif key == "year":
                if value.isdigit():
                    penguin[key] = int(value)
                else:
                    penguin[key] = None

            elif key == "id":  # make sure ID stays as string or int
                if value.isdigit():
                    penguin[key] = int(value)
                else:
                    penguin[key] = value

            else:
                penguin[key] = value

        penguins.append(penguin)

    open_file.close()
    return penguins
        
peng = load_penguin_data ('penguins.csv')
print (peng)

# if len(row) == 9:
#             entry_num = row[0]
#             species = row[1]
#             island = row[2]
#             bill_length = float(row[3])
#             bill_depth = float(row[4])
#             flipper_length = float(row[5])
#             body_mass = float(row[6])
#             sex = row[7]
#             year = int(row[8])

#             year_d = {}
#             year_d[headers[1]] = species
#             year_d[headers[2]] = island
#             year_d[headers[3]] = bill_length
#             year_d[headers[4]] = bill_depth
#             year_d[headers[5]] = flipper_length
#             year_d[headers[6]] = body_mass
#             year_d[headers[7]] = sex
#             year_d[headers[8]] = year
#             penguins[entry_num] = year_d



