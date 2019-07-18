import string

t = string.Template("Name: $name    Price: $price   Location: $location")

values = {"name": "Bottle", "price": 15.2, "location": "Floor 1"}
print(t.substitute(values))

