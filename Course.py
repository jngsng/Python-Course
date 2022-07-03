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

def hello(who):
  print("hello",who)

def plus(a,b):
  print(a+b)

def minus(a,b=0):
  print(a-b)

minus(5,2)

def r_plus(a,b):
  return a + b

def p_plus(a,b):
  print(a+b)

p_result = p_plus(2,3)
r_result = r_plus(2,3)

print(p_result,r_result)

# Positional Argument, keyword argument

def plus1(a,b):
  return a-b
  
result = plus1(b=30, a=1)
print(result)

def say_hello1(name,age):
  return f"hello {name}, you are {age} years old"

hello1 = say_hello1("JSkim",27)
print(hello1)

hello2 = say_hello1(age = 27, name="Kim")
print(hello2)

# Calculator
# plus, minus, times(곱셈), division(나눗셈), negation??, power(제곱), remainder???

def calculator(a,b):
  
  print(a+b)
  print(a-b)
  print(a*b)
  print(a/b)
  print(pow(a,b))
  return

calculator(10,10)

