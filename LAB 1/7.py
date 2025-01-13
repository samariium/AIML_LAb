# 1.Create a string variable and find the length of the string:
text = "Hello, welcome to the world of Python programming!"
length_of_string = len(text)
print(f"Length of the string: {length_of_string}")

# 2.Convert the string to uppercase and lowercase:
uppercase_string = text.upper()
lowercase_string = text.lower()
print(f"Uppercase version: {uppercase_string}")
print(f"Lowercase version: {lowercase_string}")


# 3.Check if a substring exists in the string:
substring = "Python"
is_substring_present = substring in text
print(f"Is '{substring}' present in the string? {is_substring_present}")

# 4.Split the string into a list of words:
words_list = text.split()
print(f"List of words: {words_list}")
