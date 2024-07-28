def print_pattern1(rows):
 
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(chr(ord('A') + j - 1), end="")
        print()

def print_pattern2(rows):
  
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

if __name__ == "__main__":
    rows = 5  
    print("Pattern 1:")
    print_pattern1(rows)
    print("\nPattern 2:")
    print_pattern2(rows)
