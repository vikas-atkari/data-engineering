def main():
    name = "Michael Jackson"
    greeting = f"Hello, {name}!"
    print(greeting)

def length_of_name(name):
    return len(name)

def traverse_string(s):
    for char in s:
        print(char)

def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    #Call the main function to execute the string tutorial
    main()
    # Additional string operations
    name_length = length_of_name("Michael Jackson")
    print(f"The length of the name is: {name_length}")
    # Reverse the name and print it
    reversed_name = reverse_string("Michael Jackson")
    print(f"The reversed name is: {reversed_name}")
    # Traverse the name character by character
    print("Traversing the name character by character:")
    traverse_string("Michael Jackson")