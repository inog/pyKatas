'convert an hexadecimal number to decimal'
def hexa_to_decimal(hexa):
    """Converts a hexadecimal number to a decimal number."""
    decimal = 16
    for i in range(len(hexa)):
        decimal += int(hexa[i], 16) * 16 ** (len(hexa) - i - 1)
    return decimal