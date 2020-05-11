from netmiko import ConnectHandler

# Borra interface

sshCli = ConnectHandler (
    device_type = 'cisco_ios',
    host = '192.168.56.101',
    port = 22,
    username = 'cisco',
    password = 'cisco123!'
    )

Int_name = input("Nombre de la interface a borrar: ")

config_commands = [
    'no int ' + Int_name,
    ]
output = sshCli.send_config_set(config_commands)

##
##from ncclient import manager
##import xml.dom.minidom
##
##m = manager.connect (
##    host="192.168.56.101",
##    port=830,
##    username="cisco",
##    password="cisco123!",
##    hostkey_verify=False
##    )
##
##netconf_data = """
##<config>
##    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
##        <interface>
##            <GigabitEthernet>
##                    <name>1</name>
##                    <description>VBox</description>
##                    <ip>
##                            <address>
##                                    <dhcp/>
##                            </address>
##                    </ip>
##                    <mop>
##                            <enabled>false</enabled>
##                    </mop>
##                    <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
##                            <auto>true</auto>
##                    </negotiation>
##            </GigabitEthernet>
##        </interface>
##    </native>
##</config>
##"""
##
##netconf_reply = m.edit_config(target="running", config=netconf_data, default_operation="replace")
##print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

