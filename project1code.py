
# name: Maeve Ross
# uniqname + number: maever + 40315854
# name of dataset: penguins.csv
# columns working with: species, island, flipper_length_mm, sex          
# calculations to be performed: 
#.          1 - Which species had the greatest flipper length?
#           2 - How many females were on each island? 
# diagrams are in submission #2 from figma link
# I used AI pretty heavily in this project to help debug and point out why errors were occuring in my function. I also asked Chat to help break down each calculation into 4 different functions because I was unsure where to start. 
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
    # Creates a dictionary where keys are species and values are a list of  all flipper lengths belonging to that species
    flipper_data = {}

    for penguin in penguins:
        species = penguin.get("species")
        flipper_length = penguin.get("flipper_length_mm")

        #include valid numeric flipper lengths
        if species and flipper_length is not None:
            if species not in flipper_data:
                flipper_data[species] = []
            flipper_data[species].append(flipper_length)
    
        # print (flipper_data)
    return flipper_data
    



def find_max_flipper (flipper_data):
    # prints a dictionary where keys are the species and the values are the max flipper length found from the flipper_data dict above
    species_max = {}

    for key, val in flipper_data.items():
        if val:  # make sure list is not empty
            species_max[key] = max(val)
    print (species_max)

    # Find species with the greatest flipper length overall
    overall_species = ''
    overall_length = 0
    # loops through the dictionary with the max flipper lengths for each species and finds the greatest of all species
    for species in species_max:
        flipper_length = species_max[species]

        if flipper_length > overall_length:
            overall_length = flipper_length
            overall_species = species

    # Store result in a dictionary 
    max_species = {
        "species": overall_species,
        "max_flipper_length": overall_length
    }
    print (max_species)
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

    print(f"\nThe island with the greatest female penguin population is {max_island1}, with {max_count1} females.")

    female_report_name = "female_penguin_report.txt"

    with open(female_report_name, "w") as f:
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






import unittest

class TestGetFlipperLengths(unittest.TestCase):
    # use sample of csv data 

    def setUp(self):
        self.sample_penguins = [
            {"species": "Adelie", "island": "Torgersen", "flipper_length_mm": 181.0, "sex": "male"},
            {"species": "Gentoo", "island": "Biscoe", "flipper_length_mm": 230.0, "sex": "female"},
            {"species": "Chinstrap", "island": "Dream", "flipper_length_mm": None, "sex": "female"},
            {"species": "Adelie", "island": "Torgersen", "flipper_length_mm": 190.0, "sex": "female"},
            {"species": "Gentoo", "island": "Biscoe", "flipper_length_mm": 217.0, "sex": None},
            ]
        
    # test get_flipper_lengths(penguins)

    # Usual : Checks correct grouping of flipper lengths by species
    def test_general_species_keys(self):
        result = get_flipper_lengths(self.sample_penguins)
        # True if expected species are present
        contains_a = "Adelie" in result
        contains_g = "Gentoo" in result
        self.assertTrue(contains_a)
        self.assertTrue(contains_g)

    # Usual : Ensure each value type is a list
    def test_general_values_type(self):
        result = get_flipper_lengths(self.sample_penguins)
        for v in result.values():
            self.assertTrue(isinstance(v, list))


    # Edge: Handle missing flipper length (None value)
    def test_edge_no_flipper_value(self):
        result = get_flipper_lengths(self.sample_penguins)
        self.assertFalse(None in result.get("Chinstrap", []))  # should skip None



    # Edge: Handle missing species name (empty string)
    def test_edge_empty_input(self):
        result = get_flipper_lengths(self.sample_penguins)
        self.assertFalse("" in result)




class TestFindMaxFlipper(unittest.TestCase):

    # test cases for find_max_flipper(flipper_data)

    # Usual: verifies correct species is returned when comparing valid numeric data.
    def test_general_max_species_value(self):
        flipper_data = {"Adelie": [181.0, 190.0], "Gentoo": [230.0, 217.0]}
        result = find_max_flipper(flipper_data)
        self.assertTrue(result["species"] == "Gentoo")


    # Usual: checks that maximum flipper length value is computed accurately.
    def test_general_max_length_float(self):
        flipper_data = {"Adelie": [181.0, 190.0], "Gentoo": [230.0, 217.0]}
        result = find_max_flipper(flipper_data)
        self.assertAlmostEqual(result["max_flipper_length"], 230.0)


    # Edge: handles case where all species lists are empty — should not crash.
    def test_edge_empty_dict(self):
        flipper_data = {"Adelie": [], "Gentoo": []}
        result = find_max_flipper(flipper_data)
        self.assertFalse(result["species"])


    # Edge: handles empty dictionary input — returns zero-length safely.
    def test_edge_raises_type_error(self):
        # Wrong type passed (not a dict)
        flipper_data = {}
        result = find_max_flipper(flipper_data)
        self.assertTrue(result["max_flipper_length"] == 0)




class TestFilterPenguins(unittest.TestCase):
    def setUp(self):
        self.sample_penguins = [
            {"species": "Adelie", "island": "Torgersen", "flipper_length_mm": 181.0, "sex": "male"},
            {"species": "Gentoo", "island": "Biscoe", "flipper_length_mm": 230.0, "sex": "female"},
            {"species": "Chinstrap", "island": "Dream", "flipper_length_mm": 194.0, "sex": "female"},
            {"species": "Adelie", "island": "Torgersen", "flipper_length_mm": 190.0, "sex": "female"},
        ]
    # test case for filter_penguins(penguins)

    # Usual: ensures the correct number of female penguins are filtered.
    def test_correct_count(self):
        result = filter_penguins(self.sample_penguins)
        self.assertTrue(len(result) == 3)

    # Usual: confirms all returned penguins are female 
    def test_general_all_females(self):
        result = filter_penguins(self.sample_penguins)
        all_females = all(p["sex"] == "female" for p in result)
        self.assertTrue(all_females)


    # Edge: handles case of empty input list gracefully.
    def test_empty_list_input(self):
        result = filter_penguins([])
        self.assertTrue(len(result) == 0)


    # Edge: handles missing sex field — should not cause errors.
    def test_missing_sex_field(self):
        data = [{"species": "Adelie", "island": "Dream"}]
        result = filter_penguins(data)
        self.assertTrue(len(result) == 0)


class TestCountFemalesByIsland(unittest.TestCase):

    # test case for count_females_by_island(female_penguins) 

    def setUp(self):
        self.sample_penguins = [
            {"species": "Adelie", "island": "Torgersen", "flipper_length_mm": 181.0, "sex": "male"},
            {"species": "Gentoo", "island": "Biscoe", "flipper_length_mm": 230.0, "sex": "female"},
            {"species": "Chinstrap", "island": "Dream", "flipper_length_mm": 194.0, "sex": "female"},
            {"species": "Adelie", "island": "Torgersen", "flipper_length_mm": 190.0, "sex": "female"},
        ]

    # Usual: ensures each island's female count is accurate.
    def test_female_counts_match(self):
        female_penguins = filter_penguins(self.sample_penguins)
        counts, _ = count_females_by_island(female_penguins)
        self.assertTrue(counts["Torgersen"] == 1)


    # Usual: confirms output is a dictionary mapping islands to counts.
    def test_returns_dict_type(self):
        female_penguins = filter_penguins(self.sample_penguins)
        counts, _ = count_females_by_island(female_penguins)
        self.assertTrue(isinstance(counts, dict))


    # Edge: tests case where no female penguins exist.
    def test_no_females(self):
        data = [{"island": "Dream", "sex": "MALE"}]
        female_penguins = filter_penguins(data)
        counts, _ = count_females_by_island(female_penguins)
        self.assertTrue(len(counts) == 0)


    # Edge: handles missing island field gracefully — should skip entry.
    def test_missing_island_field(self):
        data = [{"sex": "FEMALE"}]
        female_penguins = filter_penguins(data)
        counts, _ = count_females_by_island(female_penguins)
        self.assertTrue(len(counts) == 0)

if __name__ == "__main__":
    unittest.main()