# from imaplib import Literal

import multi_fuel_dispenser_system

message = """
Welcome to Semicolon Station!
Available petroleum
1. Buy Petroleum
2. Show Transaction History 
                            """
print(message)


operation = int(input("Enter operation: "))
transaction_history = []

if operation == 1:
    available_petroleum = """
        Available Petroleum
            1. Petrol ⇒  650/Literal
            2. Diesel ⇒ 720 / Liter
            3. Kerosene ⇒ 550 / Liter
            4. Gas ⇒ 480 / Liter """
    print(available_petroleum)

    petroleum_choice = int(input("Enter operation: "))
    amount_or_litre = input("Enter Litre or Amount: ").lower()


    if petroleum_choice == 1:
        if amount_or_litre == "amount":
            fuel_price = int(input("How much Petrol are you  buying (650/L): "))
            litres = fuel_price / 650
            customers_transaction_value = ["Petrol", fuel_price, litres]

            while(fuel_price < 650):
                print("Amount must be above a liter price !!!")
                fuel_price = int(input("How much Petrol are you  buying (650/L): "))
            litres = fuel_price / 650
            customers_transaction_value = ["Petrol", fuel_price, litres]

        elif amount_or_litre == "litre":
            litres = int(input("How many litres of Petrol are you  buying (650/L): "))
            amount = litres * 650
            customers_transaction_value = ["Petrol", amount, litres]

            while (litres < 1 or litres > 50):
                print("Liters must be between 1 - 50 !!!")
                litres = int(input("How many litres of Petrol are you  buying (650/L): "))
            amount = litres * 650
            customers_transaction_value = ["Petrol", amount, litres]


        customers_transaction_key = ["product", "Amount", "Litres"]
        customers_transaction_receipt = dict(zip(customers_transaction_key, customers_transaction_value))
        show_transaction_history = transaction_history.append(customers_transaction_receipt)

        print("Customers Transaction Receipt")
        print("==============================")
        for key, value in customers_transaction_receipt.items():
            print(f"{key} : {value}")

        print("===============================")
        print("Saving Transaction History. . . . . .")


    elif petroleum_choice == 2:
        if amount_or_litre == "amount":
            fuel_price = int(input("How much Diesel are you  buying (720/L): "))
            litres = fuel_price / 720
            customers_transaction_value = ["Diesel", fuel_price, litres]

            while(fuel_price < 720):
                print("Amount must be above a liter price !!!")
                fuel_price = int(input("How much Diesel are you  buying (720/L): "))
            litres = fuel_price / 720
            customers_transaction_value = ["Diesel", fuel_price, litres]

        elif amount_or_litre == "litre":
            litres = int(input("How many litres of Diesel are you  buying (720/L): "))
            amount = litres * 720
            customers_transaction_value = ["Diesel", amount, litres]

            while (litres < 1 or litres > 50):
                print("Liters must be between 1 - 50 !!!")
                litres = int(input("How many litres of Diesel are you  buying (720/L): "))
            amount = litres * 720
            customers_transaction_value = ["Diesel", amount, litres]


        customers_transaction_key = ["Diesel", "Amount", "Litres"]
        customers_transaction_receipt = dict(zip(customers_transaction_key, customers_transaction_value))
        show_transaction_history = transaction_history.append(customers_transaction_receipt)

        print("Customers Transaction Receipt")
        print("==============================")
        for key, value in customers_transaction_receipt.items():
            print(f"{key} : {value}")

        print("===============================")
        print("Saving Transaction History. . . . . .")



    elif petroleum_choice == 3:
        if amount_or_litre == "amount":
            fuel_price = int(input("How much Kerosene are you  buying (550/L): "))
            litres = fuel_price / 550
            customers_transaction_value = ["Kerosene", fuel_price, litres]

            while(fuel_price < 550):
                print("Amount must be above a liter price !!!")
                fuel_price = int(input("How much Kerosene are you  buying (720/L): "))
            litres = fuel_price / 550
            customers_transaction_value = ["Kerosene", fuel_price, litres]

        elif amount_or_litre == "litre":
            litres = int(input("How many litres of Kerosene are you  buying (550/L): "))
            amount = litres * 550
            customers_transaction_value = ["Kerosene", amount, litres]

            while (litres < 1 or litres > 50):
                print("Liters must be between 1 - 50 !!!")
                litres = int(input("How many litres of Kerosene are you  buying (550/L): "))
            amount = litres * 550
            customers_transaction_value = ["Kerosene", amount, litres]


        customers_transaction_key = ["Kerosene", "Amount", "Litres"]
        customers_transaction_receipt = dict(zip(customers_transaction_key, customers_transaction_value))
        show_transaction_history = transaction_history.append(customers_transaction_receipt)

        print("Customers Transaction Receipt")
        print("==============================")
        for key, value in customers_transaction_receipt.items():
            print(f"{key} : {value}")

        print("===============================")
        print("Saving Transaction History. . . . . .")



    elif petroleum_choice == 4:
        if amount_or_litre == "amount":
            fuel_price = int(input("How much Gas are you  buying (480/L): "))
            litres = fuel_price / 480
            customers_transaction_value = ["Gas", fuel_price, litres]

            while(fuel_price < 480):
                print("Amount must be above a liter price !!!")
                fuel_price = int(input("How much Gas are you  buying (480/L): "))
            litres = fuel_price / 480
            customers_transaction_value = ["Gas", fuel_price, litres]

        elif amount_or_litre == "litre":
            litres = int(input("How many litres of Gas are you  buying (480/L): "))
            amount = litres * 480
            customers_transaction_value = ["Gas", amount, litres]

            while (litres < 1 or litres > 50):
                print("Liters must be between 1 - 50 !!!")
                litres = int(input("How many litres of Gas are you  buying (480/L): "))
            amount = litres * 480
            customers_transaction_value = ["Gas", amount, litres]


        customers_transaction_key = ["Gas", "Amount", "Litres"]
        customers_transaction_receipt = dict(zip(customers_transaction_key, customers_transaction_value))
        show_transaction_history = transaction_history.append(customers_transaction_receipt)

        print("Customers Transaction Receipt")
        print("==============================")
        for key, value in customers_transaction_receipt.items():
            print(f"{key} : {value}")

        print("===============================")
        print("Saving Transaction History. . . . . .")



    elif transaction_history == 2:
        print(transaction_history)


