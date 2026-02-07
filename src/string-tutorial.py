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

def string_operations():
    name = "Michael Jackson"
    print(f"Original name: {name}")
    
    # Concatenation
    full_name = name + " is a legendary musician."
    print(full_name)
    
    # Length
    print(f"Length of the name: {len(name)}")
    
    # Upper and Lower case
    print(f"Uppercase: {name.upper()}")
    print(f"Lowercase: {name.lower()}")
    
    # Split and Replace
    split_name = name.split()
    print(f"Split name: {split_name}")
    
    replaced_name = name.replace("Michael", "MJ")
    print(f"Replaced name: {replaced_name}")

    strideng_name = name[::2]
    print(f"String with every second character: {strideng_name}")

    sliced_name = name[1:7]
    print(f"Sliced name (characters 1 to 6): {sliced_name}")

    print(f"Michael Jackson is \n the best musician in the world.")
    print(f"Michael Jackson is \t the best musician in the world.")
    print(f"Michael Jackson is \\ the best musician in the world.")
    print(r'Michael Jackson is \ the best musician in the world.')

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

    # Call the string_operations function to demonstrate various string operations
    string_operations()

    paragrapgh = """Michael Jackson was an American singer, songwriter, and dancer. He was one of the most famous and influential entertainers in the world. 
 His contributions to music, dance, and fashion made him a global icon. He is often referred to as the "King of Pop"."""
    print(paragrapgh)