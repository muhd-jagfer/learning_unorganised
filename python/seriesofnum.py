def getint():
    while True:
        try:
            n = int(input("Enter a number: "))
            return n
        except ValueError:
            print("Invalid input. Please enter an integer.")



def main():
    n = getint()
    while True:
        series = input("enter whether you want 'odd' or 'even' series: ").lower()
        if series == 'odd':
            for i in range(1, n+1, 2):
                print(i, end=" ")
            break
        elif series == 'even':
            for i in range(0, n+1, 2):
                print(i, end=" ")
            break
        else:
            print("Please enter 'odd' or 'even'.")

if __name__ == "__main__":
    main()