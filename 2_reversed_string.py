my_data = "I love my annimal very much"

# Using a loop
data_length = len(my_data)
reversed_string = ""
for i in range(data_length - 1, -1, -1):
    reversed_string += my_data[i] 
print(reversed_string)

# Using Python function
my_data = "I love my annimal very much"
list_of_strings = list(my_data)
list_of_strings.reverse()
reversed_string = "".join(list_of_strings)
print(reversed_string)
