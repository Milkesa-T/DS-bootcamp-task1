#!/usr/bin/env python3
"""
Level 2, Task 3: Fibonacci Sequence Generator
This script generates a Fibonacci sequence up to the nth term specified by the user.
"""

def generate_fibonacci(n_terms: int) -> list:
    """
    Generates a list containing the Fibonacci sequence up to specified terms.
    
    Args:
        n_terms (int): The number of sequence terms to generate.
        
    Returns:
        list: The list of Fibonacci numbers.
    """
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
        
    sequence = [0, 1]
    
    # Iterate and build the sequence using an iterative approach
    while len(sequence) < n_terms:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
        
    return sequence

def main():
    print("--- Fibonacci Sequence Generator ---")
    try:
        n = int(input("Enter the number of terms of the Fibonacci sequence you would like to generate? "))
        
        if n < 0:
            print("Please enter a positive integer.")
            return
            
        result = generate_fibonacci(n)
        print(f"Fibonacci Sequence ({n} terms):")
        print(", ".join(map(str, result)))
        
    except ValueError:
        print("Invalid input! Please enter a numeric integer value.")

if __name__ == "__main__":
    main()
