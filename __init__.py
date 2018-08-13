import paramiko
import time

def ssh_connect(device_ip):
    print("Connecting to: " + device_ip)
    hostname = device_ip
    username = "administrator"
    password = "password"
    port = 22

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=username, password=password)
    channel = client.invoke_shell()

    print("Successfully connected to: " + device_ip)
    return client, channel


def esend(command, channel):

    channel.send(command)


def ewait(waitstr, channel, tout=0):
    startTime = int(time.time())
    stroutput = ''
    while waitstr not in stroutput:
        currentTime = int(time.time())
        if channel.recv_ready():
            try:
                current = channel.recv(9999).decode()
                stroutput += current
                if current.strip() != '':
                    print(current, end='')
            except:
                continue

        if tout != 0:
            if (currentTime - startTime) > tout:
                try:
                    if current.strip() != '':
                        print(current, end='')
                except:
                    pass
                return stroutput

    return stroutput