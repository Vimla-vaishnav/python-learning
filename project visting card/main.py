def visiting_card():
    name = input("Enter your name: ")
    designation = input("Enter your designation: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")

    print("\n" + "="*40)
    print(f"{name.upper():^40}")
    print(f"{designation.title():^40}")
    print("-"*40)
    print(f"📞  Phone   : {phone}")
    print(f"✉️   Email   : {email}")
    print(f"🏠  Address : {address}")
    print("="*40)

visiting_card()
