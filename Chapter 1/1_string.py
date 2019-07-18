import string

t = string.Template("Name: $name    Price: $price   Location: $location")

values = {"name": "Bottle", "price": 15.2, "location": "Floor 1"}
print(t.substitute(values))

print(string.printable)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.hexdigits)
print(string.octdigits)
print(string.digits)
print(string.punctuation)
print(string.whitespace)
