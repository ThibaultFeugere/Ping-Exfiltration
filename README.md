# Ping Exfiltration

Ping Exfiltration with Scapy Python library. 
The goal is to send, step by step, an /etc/shadow file with ICMP request.

## Client

It's where the ICMP Exfiltration gonna happen.

## Server

It's where we gonna receive content of /etc/save_shadow file

## Hash

A hash system has been implemented in order to guarantee the integrity of the ICMP Exfiltration

## Upcoming features

Actually, the ip addresses are in python files. Soon, i gonna add args system in order to precise the ip address.
