while True:

    option = input("=====MEGA CONVERTER ===== \n \
    \n      A: Metres to Feet \
    \n      B: Feet to Metres \
    \n      C: Celsius to Farenheit \
    \n      D: Farenheit to Celsius \
    \n      E: Kilograms to Pounds \
    \n      F: Pounds to Kilograms \
    \n Specify the conversion you want: ")

    try:
        if option.lower() == 'a':
            amount = int(input('Enter a value in Metres: '))
            print(f'{amount} m = {amount * 3.28084:.2f} ft')

        elif option.lower() == 'b':
            amount = int(input('Enter a value in Feet: '))
            print(f'{amount} ft = {amount * 0.3048:.2f} m')

        elif option.lower() == 'c':
            amount = int(input('Enter a value in Celsius: '))
            print(f'{amount} C = {amount * 9/5 + 32:.2f} F')

        elif option .lower()== 'd':
            amount = int(input('Enter a value in Farenheit: '))
            print(f'{amount} F = {(amount - 32) * 5/9:.2f} C')

        elif option.lower() == 'e':
            amount = int(input('Enter a value in Kilograms: '))
            print(f'{amount} kg = {amount * 2.20462:.2f} pounds')

        elif option.lower() == 'f':
            amount = int(input('Enter a value in Pounds: '))
            print(f'{amount} pounds = {amount * 0.453592:.2f} kg')

        elif option == '':
            break

        else:
            print("Invalid selection. Please specify a conversion between A - F.")

    except (TypeError,ValueError):
        print("Please enter a numerical value: ")

print('Thanks for using this convertor!')