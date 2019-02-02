import random


def generate():
    path = 'policy.csv'
    file_policy = open(path, 'w')
    file_policy.write("source_address,source_port,destination_ip,destination_port,protocol,action\n")
    file_policy.close()
    generate_table(path)
    print 'Done!'


def generate_table(path):
    global ips, ports, protocols
    ips = ['165.234.185.96', '65.234.184.96', '165.37.174.96', '111.234.233.222', '1.111.111.222', '123.123.123.123']
    ports = [80, 8080, 123, 63645, 2354, 867, 3456]
    protocols = ['Tcp', 'Udp', 'SMTP', 'FTP', 'SSH', 'RPC']

    file_policy = open(path, 'a')
    for i in range(0, 10):
        file_policy.write(generate_new_row())

    file_policy.write('{a},{a},{a},{a},{a},block'.format(a='any'))
    file_policy.close()


def generate_new_row():
    global ips, ports, protocols

    n = ran_int(ips)
    if n < 0:
        ip_src = 'any'
    else:
        ip_src = ips[n]

    n = ran_int(ips)
    if n < 0:
        ip_des = 'any'
    else:
        ip_des = ips[n]

    n = ran_int(ports)
    if n < 0:
        port_src = 'any'
    else:
        port_src = ports[n]

    n = ran_int(ports)
    if n < 0:
        port_des = 'any'
    else:
        port_des = ports[n]

    n = ran_int(protocols)

    if n < 0:
        protocol = 'any'
    else:
        protocol = protocols[n]

    if random.randint(0, 3) == 0:
        action = 'Drop'
    else:
        action = 'Allow'

    return str.format('{0},{1},{2},{3},{4},{5}\n', ip_src, port_src, ip_des, port_des, protocol, action).lower()


def ran_int(obj):
    return random.randint(-3, len(obj) - 1)


if __name__ == '__main__':
    generate()
