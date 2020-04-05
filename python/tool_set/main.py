import json
from Person import Person

username = ''
age = 18

def setUser():
    username = input('Username : ')
    age = input('Age : ')
    print(username, age)

def getUserData():
    person = Person(username, age)
    personDet = json.dumps(person.getPerson())
    print(personDet)

setUser()
# getUserData()