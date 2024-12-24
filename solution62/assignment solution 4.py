def reverse_string_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

string = input("Enter a string: ")
print(f"Reversed string: {reverse_string_loop(string)}")