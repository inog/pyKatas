"""Here are some popular libraries you may find useful in scripting as a pentester:

    Request - simple HTTP library.
    Scapy - send, sniff, dissect and forge network packets
    https://scapy.readthedocs.io/en/latest/introduction.html
    Pwntools - a CTF & exploit development library.
    https://docs.pwntools.com/en/stable/

"""
import pprint
import requests

r = requests.get("https://tryhackme.com")
print("status code : ", r.status_code)
pprint.pprint(r.headers)

