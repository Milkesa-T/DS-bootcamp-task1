#!/usr/bin/env python3
"""
Level 1, Task 3: Reverse a String
This script takes a string input from the user and outputs its reverse.
"""

def reverse_string(input_str: str) -> str:
    """
    Reverses the given string.
    
    Args:
        input_str (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    # Using Python slicing for an efficient and idiomatic reversal
    return input_str[::-1]

def main():
    print("--- String Reversal Tool ---")
    user_input = input("Enter a string to reverse: ")
    
    if not user_input:
        print("Empty string provided.")
    else:
        reversed_result = reverse_string(user_input)
        print(f"Original: {user_input}")
        print(f"Reversed: {reversed_result}")

if __name__ == "__main__":
    main()
