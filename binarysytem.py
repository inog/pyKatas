
"""An implementation of the Binary System. Generates a binary number from a decimal number and vice versa."""

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
    decimal = int(input("Enter a decimal number: "))
    print("Binary number:", decimal_to_binary(decimal))

    """starts the program and asks the user to enter a binary number and converts it to a decimal number"""
    binary = input("Enter a binary number: ")
    print("Decimal number:", binary_to_decimal(binary))