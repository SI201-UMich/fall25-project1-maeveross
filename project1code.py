
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
                try:
                    penguin[key] = float(value)
                except ValueError:
                    penguin[key] = None
            elif key == "year":
                try:
                    penguin[key] = int(value)
                except ValueError:
                    penguin[key] = None
            else:
                penguin[key] = value

        penguins.append(penguin)

    open_file.close()
    return penguins
        



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
# print (load_penguin_data)



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



def generate_flipper_report(max_species):
    species = max_species.get("species")
    flipper_length = max_species.get("max_flipper_length")

    if species and flipper_length:
        print(f"The species with the greatest flipper length is {species} with a flipper length of {flipper_length}\n")
    else:
        print("No valid flipper length data available.")

    report_name = "flipper_report.txt"

    with open(report_name, "w") as f:
        f.write(f"The species with the greatest flipper length is {species} with a flipper length of {flipper_length} \n")
    
    
    with open(report_name, "r") as f:
        contents = f.read()
    # return contents

# commented out every function because main() will call it all 
# penguins = load_penguin_data('penguins.csv')
# flipper_data = get_flipper_lengths(penguins)
# max_species = find_max_flipper(flipper_data)
# generate_report(max_species)



# second calculation: how many female penguins are on each island?
# we will call the same opening file definition at the end, no need to define it twice 

def filter_penguins(penguins):
    female = []
    for penguin in penguins: 
        sex = penguin.get("sex", "").strip().lower()
        if sex == "female":
            female.append(penguin)
    
    # print (female)
    return female

def count_females_by_island(female):
    female_counts = {}
    for penguin in female:
        island = penguin.get("island", "").strip()
        if island:
            female_counts[island] = female_counts.get(island, 0) + 1

    # Find the island with the most female penguins
    if female_counts:
        max_island = max(female_counts, key=female_counts.get)
        max_count = female_counts[max_island]
    else:
        max_island = None
        max_count = 0

    return female_counts, {"island": max_island, "count": max_count}


def generate_female_report(female_counts):
    if not female_counts:
        print("No female penguin data available.")
        return

    # Print each island and its count
    for island, count in female_counts.items():
        print(f"{island}: {count}")

    # Find island with the most females — no hardcoding
    max_island1 = None
    max_count1 = 0

    for island, count in female_counts.items():
        if isinstance(count, (int, float)) and count > max_count1:
            max_count1 = count
            max_island1 = island

    print(f"\nThe island with the greatest female penguin population is {max_island1}, with ({max_count1} females).")

    with open("female_penguin_report.txt", "w") as f:
        f.write("Female Penguin Counts by Island:\n")
        for island, count in female_counts.items():
            f.write(f"{island}: {count}\n")
        f.write(f"\nThe island with the greatest female penguin population is {max_island1}, with ({max_count1} females).\n")



# calling every function
def main():
    penguins = load_penguin_data("penguins.csv")

    # Calculation 1
    flipper_data = get_flipper_lengths(penguins)
    max_species = find_max_flipper(flipper_data)
    generate_flipper_report(max_species)

    # Calculation 2
    female_penguins = filter_penguins(penguins)
    female_counts, max_island1 = count_females_by_island(female_penguins)  # ← unpack both values
    generate_female_report(female_counts)


# Run main
if __name__ == "__main__":
    main()
