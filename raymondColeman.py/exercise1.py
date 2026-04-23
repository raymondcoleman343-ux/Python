#Python Fundamentals

#1
market = ["Yam", "Tomato", "Onion"]
market.append("Fish")
print(market) 

#2
grades = [80, 90, 70]
grades.insert(1, 85)
print(grades)

#3
gadgets = ["Laptop", "Phone", "Tablet", "Phone"]
gadgets.remove("Phone")
print(gadgets)

#4
colors = ["Red", "Blue", "Green"]
colors.clear()
print(colors)

#5
votes = ["Yes", "No", "Yes", "Yes", "No"]
(votes.count("Yes"))
print(votes)

#6
alphabets = ["a", "b", "c", "d", "e", "f"]
print(alphabets[2:5])

#7
students = ["Kofi", "Ama", "Yaw"]
students.reverse()
print(students)

#8
list_a = [1, 2]
list_b = [3, 4]
list_a.extend(list_b)
print(list_a)

#9
cities = ["Accra", "Kumasi", "Tamale"]
removed_city = cities.pop(2)
print(removed_city)

#10
items = ["Pen", "Ruler", "Eraser"]
print(items.index("Ruler"))

#Section 2: Tuples & Data Types

#1
student_info = ("Araba", 20)
student_info[1] = 21
print(student_info)


#2
tup = (1, 2, 3)
temp_list = list(tup)
temp_list.append(4) 
tup = tuple(temp_list)
print(tup)

#3
data = (10, 20, 10, 30, 10)
print(data.count(10)) 

#4
colors = ("Red", "Blue", "Green")
print(colors.index('blue'))

#5
coords = (5.6, -0.1)
lat, lon = coords
print(lat, lon) 


#6
nest = [2,3,4,5]
nest.append((5, 10))
print(len(nest)) 

#7
numbers = (10, 20, 30, 40, 50)
print(numbers[-2:]) 


#8
my_list = [1, 2]
my_list.extend((3, 4))
print(my_list)

#9
# del my_tup

#10
x = (5)   
y = (5,)  
print(type(x)) 
print(type(y)) 


