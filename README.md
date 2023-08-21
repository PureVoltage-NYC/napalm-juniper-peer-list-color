# napalm-juniper-peer-list-color
PureVoltage Juniper peer list script with color

This script is made in Python3 the point of this script is to log into your Juniper routers and it will pull the peers from any IX configuration it uses Napalm it requires sys, getpass, termcolor.
When running the script it will ask you for the routers hostname, username, and password which uses getpass to securely enter the password required so that it is not pasted in shell in plaintext. 
It will sort peers by active colored in green. Sorting IPv4 first then IPv6. 
It will sort Inactive peers in red. Sorting once again IPv4 first then IPv6.

You can read more about this at https://purevoltage.com
