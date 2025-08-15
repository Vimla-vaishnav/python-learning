def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I am inside of finally.")
main()
# finally use fuction me ata hai,finally override karta hai ,return ke bad bhi chalta hai