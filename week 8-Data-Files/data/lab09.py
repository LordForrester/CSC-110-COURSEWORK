def main():
    try:
        userAge = int(input("Enter Age: "))
    except ValueError:
        userAge = -99
main()


