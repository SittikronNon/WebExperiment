people = [
    {"name": "Harry", "house": "Peepo"},
    {"name": "Cookie", "house": "Sheesh"},
    {"name": "Dizzien", "house": "Booky"}
]



people.sort(key=lambda person: person["name"])

print(people)