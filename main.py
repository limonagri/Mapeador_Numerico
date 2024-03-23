Martin_data = {"Name": "Martin", "high": "176", "birthday": "2007-12-06",
               "zodiac": "Sagittarius", "hobby": "video games"}
Alejandro_data = {"Name": "Alejandro", "high": "185", "birthday": "1998-02-22",
               "zodiac": "aquarium", "hobby": "photo"}
Nicolas_data = {"Name": "Nicolas", "high": "175", "birthday": "1996-05-10",
               "zodiac": "gemini", "hobby": "video games"}
person_dict = {"3124356765": Martin_data,
               "3145236478": Alejandro_data,
               "3156784328": Nicolas_data}

print(person_dict)
print(person_dict["3156784328"])
print(person_dict["3156784328"]["hobby"])





