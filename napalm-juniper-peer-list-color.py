grouimport napalm
import sys
import getpass
from termcolor import colored

def main():
    # Prompt for the router's hostname, username, and password
    hostname = input("Enter your router's hostname: ")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    driver = napalm.get_network_driver('junos')
    device = driver(hostname=hostname,
                    username=username,
                    password=password)

    try:
        device.open()
    except Exception as e:
        print(f"Error connecting to the device: {e}")
        sys.exit(1)

    bgp_neighbors = device.get_bgp_neighbors()

    if not bgp_neighbors:
        print("No BGP neighbors found.")
        device.close()
        sys.exit(0)

    sorted_neighbors = sorted(bgp_neighbors['global']['peers'].items(), key=lambda x: x[1]['is_up'], reverse=True)

    for peer, peer_data in sorted_neighbors:
        state = 'Active' if peer_data['is_up'] else 'Inactive'
        color = 'green' if peer_data['is_up'] else 'red'
        state_colored = colored(state, color)
        description = peer_data['description'] if 'description' in peer_data else 'N/A'
        group = peer_data['remote_as'] if 'remote_as' in peer_data else 'N/A'
        print(f"Peer: {peer} - State: {state_colored} - Description: {description} - Group: {group}")

    device.close()

if __name__ == "__main__":
    main()


