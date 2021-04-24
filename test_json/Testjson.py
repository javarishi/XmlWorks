'''
Created on 24-Apr-2021

@author: Rishi
'''
import json

x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

print(y["name"])
print(y["age"])
print(y["city"])

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)
print(y)


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
