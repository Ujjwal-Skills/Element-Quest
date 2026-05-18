#Project Title: Element Quest


#Element database
#storing each element in dictionary
elements = {
    1 : {
        "name":"Hydrogen",
        "symbol":"H",
        "atomic_number":"1",
        "atomic_mass":1.00784,
        "category":"Nonmetal",
        "group":1,
        "period":1,
        "melting":"-259.16 °C",
        "boiling":"-252.87 °C",
        "discovered_by":"Henry Cavendish",
        "year_of_discovery":1766,
        "fact":"Hydrogen is the most common element in the universe, making up about 75% of its mass."
    },

    2 : {
        "name":"Helium",
        "symbol":"He",
        "atomic_number":2,
        "atomic_mass":4.002602,
        "category":"Noble Gas",
        "group":18,
        "period":1,
        "melting":"-272.2 °C",
        "boiling":"-268.93 °C",
        "discovered_by":"Pierre Janssen and Norman Lockyer",
        "year_of_discovery":1868,
        "fact":"Helium was discovered on the sun before it was found on the earth."
        },

    3 : {
        "name":"Lithium",
        "symbol":"Li",
        "atomic_number":3,
        "atomic_mass":6.941,
        "category":"Alkali Metal",
        "group":1,
        "period":2,
        "melting":"180.54 °C",
        "boiling":"1342 °C",
        "discovered_by":"Johan August Arfwedson",
        "year_of_discovery":1817,
        "fact":"Although it is a metal, Lithium it is soft enough to cut with a knife"
        },

    4 : {
        "name":"Beryllium",
        "symbol":"Be",
        "atomic_number":4,
        "atomic_mass":9.012182,
        "category":"Alkali Earth Metal",
        "group":2,
        "period":20,
        "melting":"1287 °C",
        "boiling":"2469 °C",
        "discovered_by":"Louis Nicolas Vauquelin, Martin Heinrich Klaproth",
        "year_of_discovery":1817,
        "fact":"Beryllium is a component of several dental alloys."
        },
    
}

#collection of unlocked element
collection = []

#defining function that can accept atomic number and display all the info. of that element in clean game like format
def display_element(number):
    if number in elements:
        print("========================================")
        print("⚛️ ELEMENT INFORMATION")
        print("========================================")
        print("Name:",elements[number]["name"])
        print("Symbol:",elements[number]["symbol"])
        print("Atomic Number:",elements[number]["atomic_number"])
        print("Atomic Mass:",elements[number]["atomic_mass"])
        print("Category:",elements[number]["category"])
        print("Group:",elements[number]["group"])
        print("Period:",elements[number]["period"])
        print("Melting Point:",elements[number]["melting"])
        print("Boiling Point:",elements[number]["boiling"])
        print("Discovered By:",elements[number]["discovered_by"])
        print("Year of Discovery:",elements[number]["year_of_discovery"])
        print("\n💡 Fun Fact:",elements[number]["fact"])

        print("========================================")
    else:
        print("Element not found.")


# defining function that can generate random number

def my_random(seed,limit):
    seed = (seed*17+23) % 1000
    number = seed % limit + 1
    return seed,number

'''seed,atomic_number = my_random(seed,len(elements))
display_element(atomic_number)'''


#defining function for welcome screen
def welcome_screen():
    print("\n+================================================+")
    print("|         🧪 WELCOME TO ELEMENT QUEST 🧪         |")
    print("|        The Ultimate Chemistry Adventure        |")
    print("+================================================+")
    print("| Collect elements, discover fun facts,          |")
    print("| and become the master of the periodic table!   |")
    print("| 🎁 Unlock new elements                         |")
    print("| 🧠 Play quizzes                                |")
    print("| 🏆 Build your collection                       |")
    print("+================================================+\n")
    input("Press Enter to begin...")


#defining the functions for the different option in menu
# defining function for unlock new elements for player
def unlock_element(seed,collection):
    seed,number = my_random(seed,len(elements))
    print("\n🎰 Spinning the Element Wheel...\n")
    
    if number not in collection:
        print("✨ You unlocked",elements[number]["name"],"(",elements[number]["symbol"],")!\n")
        display_element(number)
        collection.append(number)
        print("🏆 Added to your collection!")
    else:
        print(elements[number]["name"],elements[number]["symbol"])
        print("📦 You already have this element in your collection.")

    return seed
'''seed = unlock_element(seed,collection)'''

#defining the function for searching element
def search_element(search):
    element_name = []
    element_symbol = []
    for i in range(1,len(elements)+1):
        element_name.append(elements[i]["name"].lower().strip())
        element_symbol.append(elements[i]["symbol"].lower().strip())
    
    if search in element_name:
        position = element_name.index(search)
        display_element(position + 1)
    elif search in element_symbol:
        position = element_symbol.index(search)
        display_element(position + 1)

#functions for displaying periodic table in ASCII art for good UX
#defining function for what should appear inside each cell of the periodic table
def get_symbol(number,collection):
    if number in collection:
        return elements[number]["symbol"].center(2)
    else:
        return "??"
#print(get_symbol(1,collection))

#defining function so that each symbol will be placed inside a bordered ASCII “tile” 
def make_cell(text):
    top = "+----+"
    middle = "|"+text.center(4)+"|"
    bottom = "+----+"
    return top,middle,bottom
'''top,middle,bottom = make_cell("??")
print(top)
print(middle)
print(bottom)'''

#defining function to display table row layout
def row_layout(row):
    top_line = ""
    middle_line = ""
    bottom_line = ""

    for symbol in row:
        if symbol == " ":
            top_line += "      "
            middle_line += "      "
            bottom_line += "      "
        else:
            top,middle,bottom = make_cell(symbol)
            top_line += top
            middle_line += middle
            bottom_line += bottom

    print(top_line)
    print(middle_line)
    print(bottom_line)
#row_layout(row)

#defining function to get 1st row of table layout
def show_period_1 (collection):
    row = [" "]*18

    row[0] = get_symbol(1,collection) #group 1
    row[17] = get_symbol(2,collection) #group 18

    row_layout(row)
    
#show_period_1(collection)

#defining function to get 2nd row of table layout
def show_period_2 (collection):
    row = [" "]*18
    row[0] = get_symbol(3,collection) #group 1
    row[1] = get_symbol(4,collection) #group 2
    for i in range(5,11):
        j = i + 7
        row[j] = get_symbol(i,collection) #group from 13 to 18
    
    row_layout(row)

#defining function to get 3rd row of table layout
def show_period_3 (collection):
    row = [" "]*18
    row[0] = get_symbol(11,collection) #group 1
    row[1] = get_symbol(12,collection) #group 2
    for i in range(13,19):
        j = i - 1
        row[j] = get_symbol(i,collection) #group from 13 to 18
    
    row_layout(row)

#defining function to get 4th row of table layout
def show_period_4 (collection):
    row = [" "]*18
    for i in range(19,37):
        j = i - 19
        row[j] = get_symbol(i,collection) #group from 1 to 18
        
    row_layout(row)

#defining function to get 5th row of table layout
def show_period_5 (collection):
    row = [" "]*18
    for i in range(37,55):
        j = i - 37
        row[j] = get_symbol(i,collection) #group from 1 to 18

    row_layout(row)

#defining function to get 6th row of table layout
def show_period_6 (collection):
    row = [" "]*18
    row[0] = get_symbol(55,collection) #group 1
    row[1] = get_symbol(56,collection) #group 2
    row[2] = get_symbol(57,collection) #group 3
    for i in range(72,87):
        j = (i+3) - 72
        row[j] = get_symbol(i,collection) #group from 4 to 18
    
    row_layout(row)

#defining function to get 7th row of table layout
def show_period_7 (collection):
    row = [" "]*18
    row[0] = get_symbol(87,collection) #group 1
    row[1] = get_symbol(88,collection) #group 2
    row[2] = get_symbol(89,collection) #group 3
    for i in range(104,119):
        j = (i+3) - 104
        row[j] = get_symbol(i,collection) #group from 4 to 18
    
    row_layout(row)

#defining function to get lanthanides row of table layout
def show_lanthanides (collection):
    row = [" "]*18

    for i in range(58,72):
        j = (i+3) - 58
        row[j] = get_symbol(i,collection) #group from 4 to 18

    row_layout(row)

#defining function to get actinides row of table layout
def show_actinides (collection):
    row = [" "]*18

    for i in range(90,104):
        j = (i+3) - 90
        row[j] = get_symbol(i,collection) #group from 4 to 18
    
    row_layout(row)

#defining function to display my collection in proper layout
def show_collection():
    show_period_1(collection)
    show_period_2(collection)
    show_period_3(collection)
    show_period_4(collection)
    show_period_5(collection)
    show_period_6(collection)
    show_period_7(collection)
    show_lanthanides(collection)
    show_actinides(collection)

# defining the function for the main menu
def main_menu():
    seed = 53
    while True: #Return to the menu until player chooses to exit
        print("\n+=================== MAIN MENU ===================+\n")
        print("1. 🎁 Unlock Random Element")
        print("2. 🔍 Search Element")
        print("3. 🧠 Quiz Challenge")
        print("4. 🏆 My Collection")
        print("5. 🚪 Exit")

        choice = int(input("Enter your choice: ")) #taking input from user

        #handling the choices made by player
        if choice == 1:
            seed = unlock_element(seed,collection)

        elif choice == 2:
            search = input("\nSearch the Element by entering the Name or Symbol: ").lower().strip()
            search_element(search)
        
        elif choice == 3:
            print("Quiz feature coming soon!")
        
        elif choice == 4:
            #print("Collection feature coming soon!")
            print()
            show_collection()

        elif choice == 5:
            print("Thanks for playing Element Quest!")
            break

        else:
            print("Invalid choice. Please try again.")


#final structure of program
welcome_screen()
main_menu()