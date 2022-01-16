import json

person_string = "{'name':'Ali', 'languages':['python', 'C++']}"


#json string to dict

result = json.loads(person_string)
print(result)



# with open('person.json') as f:
#     data = json.load(f)
#     print(data)