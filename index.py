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
        "fact":"Helium was discovered on the sun before it was found on the earth."
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
seed = 53
def my_random(seed,limit):
    seed = (seed*17+23) % 1000
    number = seed % limit + 1
    return seed,number

'''seed,atomic_number = my_random(seed,len(elements))
display_element(atomic_number)'''


# defining function unlock new elements for player
def unlock_element(seed):
    seed,number = my_random(seed,len(elements))
    print("\n🎰 Spinning the Element Wheel...")
    print("✨ You unlocked",elements[number]["name"],"(",elements[number]["symbol"],")!\n")
    display_element(number)
    return seed
'''seed = unlock_element(seed)'''


#Creating welcome screen
print("\n+================================================+")
print("|         🧪 WELCOME TO ELEMENT QUEST 🧪         |")
print("|        The Ultimate Chemistry Adventure        |")
print("+================================================+")
print("| Collect elements, discover fun facts,          |")
print("| and become the master of the periodic table!   |")
print("| 🎁 Unlock new elements                         |")
print("| 🧠 Play quizzes                                |")
print("| 🏆 Build your collection                       |")
print("+================================================+")
