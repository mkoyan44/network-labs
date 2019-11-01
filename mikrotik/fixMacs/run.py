import argparse
import configparser


parser = argparse.ArgumentParser()

parser.add_argument('--interface', type=str, required=False, default='ether1')
parser.add_argument('--macs', type=str, required=False, default='00:50:79:66:68:01,00:50:79:66:68:00')

'''
/interface bridge filter add action=accept chain=forward in-interface=ether1 src-mac-address=00:50:79:66:68:01/FF:FF:FF:FF:FF:FF
/interface bridge filter add action=drop chain=forward in-interface=ether1

'''

args = parser.parse_args()

def run():
    for mac in args.macs.split(','):
        addFirewall = "/interface bridge filter add action=accept chain=forward in-interface={interface} src-mac-address={mac}/FF:FF:FF:FF:FF:FF".format(interface=args.interface,mac=mac)
        print(addFirewall)

    print(
        "/interface bridge filter add action=drop chain=forward in-interface={interface}".format(interface=args.interface)
    )
if __name__ == '__main__':
    run()

