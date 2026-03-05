#Task 1 : Build a JSON
import json
print("\n****Task 1 : Build a JSON****\n")
user_profile={
    "name": "Lakshmi",
    "age" : 35,
    "email": "lakshmi@json.com",
    "is_active" : True,
    "skills" : ["python", "pandas", "JSON"]
}

json_string = json.dumps(user_profile, indent=4)
print(json_string)


#Task 2 : Parse an API Response
print("\n****Task 2 : Parse an API Response****\n")
response = '{"status": "success", "data": {"user_id": 101, "username": "alex99", "score": 87.5}}'

parsed = json.loads(response) #parse string to dict
username = parsed["data"]["username"]
score = parsed["data"]["score"]

print(username)
print(score)
print(f"\"User {username} scored {score} points\" ")

#Task 3 : Handle Nested JSON
print("\n****Task 3 : Handle Nested JSON****\n")
data={
  "name": "Priya",
  "address": {
    "city": "Bengaluru",
    "state": "Karnataka",
    "zip": "560001"
  }
}
#To extract values
print(data["address"]["city"])
print(data["address"]["zip"])

data["address"]["country"] = "India"#to add country

print(json.dumps(data, indent=4))