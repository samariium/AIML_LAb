# 1.Create a list of fruits:
fruits = ["Apple", "Banana", "Cherry", "Date", "Orange"]
print("Accessing elements using indexing:")
print(f"First fruit: {fruits[0]}")
print(f"Third fruit: {fruits[2]}")
print(f"Last fruit: {fruits[-1]}")

# 2.Access elements using indexing:
fruits[1] = "Kiwies"
print(f"Modified list is: {fruits}")

#3.Add and remove elements from the list
fruits.append("Watermelon")
fruits.remove("Watermelon")
print(f"Modified list is: {fruits}")

#4.Find the length of the list
length = len(fruits)
print(length)

#5.Sort the list in ascending order:
fruits.sort()
print(f"Sorted fruits list is: {fruits}")
