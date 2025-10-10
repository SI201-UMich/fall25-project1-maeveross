
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
    # print (headers)
    # get each entry as a list
    if headers[0].strip() == "":
        headers[0] = "id"

    penguins = []
    for row in file_content:
        if not row:
            continue
        # print (row)
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
        
# print (peng)

def get_flipper_lengths(penguins):
    # Creates a dictionary grouping all flipper lengths by species.
    flipper_data = {}

    for penguin in penguins:
        species = penguin.get("species")
        flipper_length = penguin.get("flipper_length_mm")

        #include valid numeric flipper lengths
        if species and flipper_length is not None:
            if species not in flipper_data:
                flipper_data[species] = []
            flipper_data[species].append(flipper_length)

    return flipper_data
# print (peng2)

def find_max_flipper (flipper_data):
    species_max = {}

    for key, val in flipper_data.items():
        if val:  # make sure list is not empty
            species_max[key] = max(val)

    # Find species with the greatest flipper length overall
    overall_species = ''
    overall_length = 0

    for species in species_max:
        flipper_length = species_max[species]

        if flipper_length > overall_length:
            overall_length = flipper_length
            overall_species = species

    # Step 3: store result in a dictionary
    max_species = {
        "species": overall_species,
        "max_flipper_length": overall_length
    }

    return max_species
def generate_report(max_species):

    species = max_species.get("species")
    flipper_length = max_species.get("max_flipper_length")

    if species and flipper_length:

        print(f"The species with the greatest flipper length is: {species}")
        print(f"Maximum flipper length: {flipper_length} mm\n")
    else:
        print("No valid flipper length data available.")
    with open("flipper_report.txt", "w") as f:
        f.write(f"The species with the greatest flipper length is: {species}\n")
        f.write(f"Maximum flipper length: {flipper_length} mm\n")
        print (f)

# calling every function
penguins = load_penguin_data('penguins.csv')
flipper_data = get_flipper_lengths(penguins)
max_species = find_max_flipper(flipper_data)
generate_report(max_species)