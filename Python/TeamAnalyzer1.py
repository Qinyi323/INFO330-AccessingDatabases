import sqlite3  # This is the package for all sqlite3 access in Python
import sys      # This helps with command-line parameters
conn = sqlite3.connect("../pokemon.sqlite")
cur = conn.cursor()

# All the "against" column suffixes:
types = ["bug","dark","dragon","electric","fairy","fight",
    "fire","flying","ghost","grass","ground","ice","normal",
    "poison","psychic","rock","steel","water"]

# Take six parameters on the command-line
if len(sys.argv) < 6:
    print("You must give me six Pokemon to analyze!")
    sys.exit()

team = []
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue

pokedex_numbers = [1, 2, 3, 4, 5, 6]
for pokedex_number in pokedex_numbers:
    cur.execute("SELECT name FROM pokemon WHERE pokedex_number = ?", (pokedex_number,))
    row = cur.fetchone()
    print(f"Pokedex number {pokedex_number} is {row[0]}")


pokedex_numbers = [1, 2, 3, 4, 5, 6]
pokemon_names = {}

# Loop over the Pokedex numbers and retrieve the corresponding Pokemon name
for pokedex_number in pokedex_numbers:
    cur.execute("SELECT name FROM pokemon WHERE pokedex_number = ?", (pokedex_number,))
    row = cur.fetchone()
    if row is not None:
        pokemon_names[pokedex_number] = row[0]
    else:
        print(f"No Pokemon found with Pokedex number {pokedex_number}")

# Print the dictionary to verify the mapping
print(pokemon_names)

pokedex_numbers = [1, 2, 3, 4, 5, 6]
pokemon_info = {}





    # Analyze the pokemon whose pokedex_number is in "arg"

    # You will need to write the SQL, extract the results, and compare
    # Remember to look at those "against_NNN" column values; greater than 1
    # means the Pokemon is strong against that type, and less than 1 means
    # the Pokemon is weak against that type

answer = input("Would you like to save this team? (Y)es or (N)o: ")
if answer.upper() == "Y" or answer.upper() == "YES":
    teamName = input("Enter the team name: ")

    # Write the pokemon team to the "teams" table
    print("Saving " + teamName + " ...")
else:
    print("Bye for now!")

