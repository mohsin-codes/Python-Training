customer = {
    "name" : "John Smith",
    "age" : 23,
    "is_verified" : True
}

print(customer)
print(customer["name"])
print(customer.get("is_verified"))

# updating dict using get method
print(customer.get("birthDate", "01 Jan 1990"))

# updating values of existing keys
customer["name"] = "Bruce Wayne"
print(customer["name"])