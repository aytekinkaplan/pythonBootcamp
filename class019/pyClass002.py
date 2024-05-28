user_info = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

print(user_info)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(car)

planet = {
    "name": "Earth",
    "moons": 1
}

print(planet)


users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
    "wathena": {
        "first": "wolfgang",
        "last": "wathena",
        "location": "berlin",
    }
}


for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")