# type
a_string = "like this"
a_number = 3
a_float = 3.12
a_boolean = True
a_none = None


# sequence type (list, tuple)
days = "mon,Tue,Wed,Thur,Fri"
print(days) 

days = ["Mon","Tue","Wed","Thur","Fri"]
print(days)

print("Mon" in days)
print(days[3])
print(len(days))

# mutable 값을 바꿀 수 있음 / immutable 값을 바꿀 수 없음
# list는 mutable

days.append("Sat")
print(days)

days.reverse()
print(days)

days = ("Mon","Tue","Wed","Thur","Fri")
print(type(days))

# dictionary
JS = {
  "name" : "JS",
  "age" : 27,
  "korean" : True,
  "fav_food" : ["Pizza","Chicken"]
}

print(JS["name"])

print(JS)
JS["bool"] = True
print(JS)

# Function

print(len("asdfasdfsdf"))

age = "27"
print(type(age))
n_age = int(age)
print(type(n_age))

def say_hello():
  print("hello")
  print("bye")

say_hello()