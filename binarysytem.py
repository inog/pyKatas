
"""An implementation of the Binary System. Generates a binary number from a decimal number and vice versa.
Default is decimal to binary conversion but calling the file with the argument 'binary' or 'b' will convert binary to decimal."""
import sys

def decimal_to_binary(decimal):
    """Converts a decimal number to a binary number."""
    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

def binary_to_decimal(binary):
    """Converts a binary number to a decimal number."""
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2 ** (len(binary) - i - 1)
    return decimal


"""starts the program and asks the user to enter a decimal number and converts it to a binary number"""
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] in ['--binary', '--b']:
            binary = input("Enter a binary number: ")
            print("Decimal number:", binary_to_decimal(binary))
    else:
        decimal = int(input("Enter a decimal number: "))
        print("Binary number:", decimal_to_binary(decimal))