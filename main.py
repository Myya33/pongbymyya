Tim_Grade=100

if 100 <= Tim_Grade >= 90:
    print('A')
elif 89 >= Tim_Grade >= 80:
    print('B')
elif 79 >= Tim_Grade >= 70:
    print('C')
elif 69 >= Tim_Grade >= 60:
    print('D')
else:
    print('F')

word = 'onomatopoeia'
for letter in word:
    print('nice cock')


number = 115784

while number > 23:
    number = number / 2
    print(number)
#continue will skip one iteration of loop
#break will terminate loop completely

for num in range(11):
    print(num)

#List: storing multiple related values in same variable
#[] signify the creation of a list
#the items in the list are labled by 'index'
#Slice is staring from somewhere in the list to print it. signified by ':'
#to update a list the cmd is 'listname'[indexifneeded] = updatedmaterial


Groceries = ['milk', 'eggs', 'bread', 'butter', 'bacon']
    i = 0
    for item in Groceries:
    Groceries[i] = f"{item}ay"
    i = i + 1



#tupil is an immutable (unchangeable) (use case = data you dont want changed
# i.e auth. files ) list
BestFriends = ('Diego, Isaac, Stevie, Hatch, Gustavo')

phone_dictionary = {
    "contact": "Dan Pickles",
    "Dan_phone_number": "(123) 456-7890",
    "contact_2": " Randolph Scott",
    "Randolph_phone_number": "(456) 789-0123",
    "contact_3": "Howard Johnson",
    "Howard_phone_number": "(789) 123-4567"
}
print{phone_dictionary["contact_2"]}

#Class defines the state and behavior of a set of objects
class Product:
    #data, state
    price: float
    name: str
    def update_price(self, price):
            #data validation
            if price < 0:
                self.price = 0
            self.price = price

    def fet_price(self):
        return self.price

#create an object using the class
product = Product ()
product.name = 'TV'
product2 = Product()

class Robot:
    def introduce_self(self):
        print( "My name is " + self.name)
r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

