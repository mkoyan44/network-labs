import os
from jinja2 import *

# Capture our current directory
cwd = os.path.dirname(os.path.abspath(__file__))
def render_doc():
    j2_env = Environment(loader=FileSystemLoader(cwd),
                         trim_blocks=True)
    with open(os.path.join(cwd, 'RB_Config.txt'), 'w') as f:
        f.write(
            j2_env.get_template('template.txt').render(
                    hostname='Arandzin',
                    password='to2korpus',
                    MGNMT_IP='10.0.158.1/24',
                    MGNMT_Subnet='10.0.158.0/24',
                    ether1_IP='10.10.11.134/30',
                    ether1_Subnet='10.10.11.132/30',
                    lo0_IP='10.255.254.158/32',
                    BR_VRF_VoIP_phones_IP='10.2.91.1/24',
                    dhcp_start='10.2.91.10',
                    dhcp_end='10.2.91.254',
                    RR_IP='10.255.254.1'
            )
        )
if __name__ == '__main__':
    render_doc()
