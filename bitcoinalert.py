"""
    In this project, you'll create a program that that tells
    you when the value of your Bitcoin falls below $30,000.

    You will need to:
    - Create a function to convert Bitcoin to USD
    - If your Bitcoin falls below $30,000, print a message.

    You can assume that 1 Bitcoin is worth $40,000

"""
investment_in_bitcoin = 1.2
bitcoin_to_usd = 25000
minAmount = 30000

# 1) write a function to calculate bitcoin to usd
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    return bitcoin_amount * bitcoin_value_usd


# 2) use function to calculate if the investment is below $30,000
value = bitcoinToUSD(investment_in_bitcoin, bitcoin_to_usd)
if value < minAmount:
    print("Warning! Bitcoin value is lower than $30000 you should sell now! ", value)
else:
    print("All god value of your bitcoin is:", value)
