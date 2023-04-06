import csv


def add(x, y):
    retval = x + y
    print(f'{x} + {y} = {retval}')
    return retval


class Developer:
    def __int__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary

    def __str__(self):
        print(f"Name: {self.name} - Language: {self.language}")

        dan = Developer('Dan Pickles', 'Python', '$90,000')

        class Developer:
            def __init__(self, name, salary, language):
                self.name = name
                self.salary = salary
                self.language = language
                print(f"Name: {name}, Language: {language}")

        ryan = Developer('Ryan Ellis', 252525252, 'French')
        print(ryan)

#ForLoop
word = "bigjoeeatss"
for num in range(11):
    print(num)

#WhileLoop
number = 90
while number < 1234190817:
    number = number * 2
    print(number)

#List
groceries = ["milk", "eggs", "bread", "bacon"]
i = 0
for items in groceries:
    groceries[i] = f"{items}ay"
    i = i + 1

#Tuple
the_best_of_friends = ("Gus", "Beer", "Dip", "caffeine", "coochie")

#dictionary
phone_dictionary = {
    "CEO": "Dan Pickles",
    "CEOext.": "(123) 456-7890",
    "Manager": "Randolph Scott",
    "Managerext.": "(456) 789-0123",
    "HR": "Howard Johnson",
    "frontdesk": "(789) 123-4567"
}
position = input("What is your parties name?")
search = input("Search by role for phone number:")

if ("Dan Pickles"):
    print("(123) 456-7890")

elif ("Randolph Scott"):
    print("(456) 789-0123")

elif ("HR"):
    print("(789) 123-4567")

else:
    print(phone_directory(search, "Value not Found"))


file = open("D:\\Professional\\SkillStorm Docs\\Pride_and_Prejudice.txt", "r")

for line in file:
    print(line)

else:
    file.close()

#class to correspond with data from database
class User:
    row_number: int
    first: str
    last: str
    email: str

    def __int__(self, row_number, first, last, email):
        self.row_number = row_number
        self.first = first
        self.last = last
        self.email = email

class CsvParser:

    def parse_file(self, file_path):
        user_list = []

        with open(file_path, "r") as file:
            csv_reader = csv.reader(file, delimiter=",")
            next(csv_reader)
            for row in csv_reader:
                user = User(csv_reader.line_num, row[0], row[1], row[2])
                user_list.append(user)

        return user_list

parser = CsvParser()
users = parser.parse_file("users.csv")
for user in users:
    print(users)
