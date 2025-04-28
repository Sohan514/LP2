def print_squares(limit):
    for i in range(1, limit + 1):
        square = i * i
        print(f"Square of {i} is {square}")

def main():
    limit = 5
    print_squares(limit)

if __name__ == "__main__":
    main()
