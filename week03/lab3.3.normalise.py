# reads in a string and takes away spaces trailing and converts to lower case
# Then outputs the length of both the input and outputted strings

input_string = input("Please enter a string: ")
clean_string = input_string.strip().lower()

length_of_input = len(input_string)
length_of_clean = len(clean_string)

print(f"The string normalised is: {clean_string}")
print(f"The original input length was: {length_of_input} and the final clean output length is: {length_of_clean}")