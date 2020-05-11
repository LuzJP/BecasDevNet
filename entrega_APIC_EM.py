import json
import requests
from tabulate import *

def get_ticket():

    requests.packages.urllib3.disable_warnings()
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "username": "devnetuser",
        "password": "Xj3BDqbU"
    }

    resp=requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)
    response_json = resp.json()
    serviceTicket = response_json["response"]["serviceTicket"]  
    return serviceTicket

def print_hosts():
    #Saca por pantalla tipo de conexion e IP

    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
    ticket = get_ticket()
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)
    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json()

    host_list = []
    i = 0
    for item in response_json["response"]:
         i+=1
         host = [
                 i,
                 item["hostType"],
                 item["hostIp"] 
                ]
         host_list.append( host )
    table_header = ["Number", "Type", "IP"]
    print( tabulate(host_list, table_header) )

def print_devices ():
    #Saca por pantalla tipo de dispositivo e IP
    
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
    ticket = get_ticket()
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)
    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json()

    device_list = []
    i = 0
    for item in response_json["response"]:
         i+=1
         device = [
                 i,
                 item["family"],
                 item["managementIpAddress"] 
                ]
         device_list.append( device )
    table_header = ["Number", "Type", "IP"]
    print( tabulate(device_list, table_header) )

def print_MAC_wireless ():
    #Saca por pantalla equipos vía WIFI y el AP al que conectan

    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
    ticket = get_ticket()
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)
    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json()

    host_list = []
    for item in response_json["response"]:
        if item["hostType"] == "wireless":
             host = [
                 item["connectedAPName"],
                 item["hostMac"] 
                ]
             host_list.append( host )
    table_header = ["AP Hostname", "MAC"]
    print( tabulate(host_list, table_header) )

def print_hostname ():
    #Saca por pantalla modelo de dispositivo y hostname

    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
    ticket = get_ticket()
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }

    resp = requests.get(api_url, headers=headers, verify=False)
    if resp.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + resp.text)
    response_json = resp.json()

    device_list = []
    for item in response_json["response"]:
         device = [
                 item["type"],
                 item["hostname"] 
                ]
         device_list.append( device )
    table_header = ["Device", "Hostname"]
    print( tabulate(device_list, table_header) )

opcion = input ( """
Seleccione una de las siguientes opciones:

1. Listar equipos y su IP asociada
2. Listar dispositivos de red y su IP
3. Listar equipos conectados vía WIFI y su MAC
4. Listar equipos de red con su modelo y 'hostname'

""")

if (int(opcion)== 1):
    print_hosts()
elif (int(opcion)== 2):
    print_devices()
elif (int(opcion)== 3):
    print_MAC_wireless()
elif (int(opcion)== 4):
    print_hostname()
else:
    print("La opcion marcada no es correcta")
    



