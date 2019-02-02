import random


def generate():
    path = 'traffic.csv'
    file_traffic = open(path, 'w')
    file_traffic.write("source_address,source_port,destination_ip,destination_port,protocol\n")
    file_traffic.close()
    generate_table(path)
    print 'Done!'


def generate_table(path):
    global ips, ports, protocols
    ips = ['165.234.185.96', '65.234.184.96', '165.37.174.96', '111.234.233.222', '1.111.111.222', '123.123.123.123']
    ports = [80, 8080, 123, 63645, 2354, 867, 3456]
    protocols = ['Tcp', 'Udp', 'SMTP', 'FTP', 'SSH', 'RPC']

    file_traffic = open(path, 'a')
    for i in range(0, 100000):
        file_traffic.write(generate_new_row())

    file_traffic.close()


def generate_new_row():
    global ips, ports, protocols

    n = ran_int(ips)
    ip_src = ips[n]

    n = ran_int(ips)
    ip_des = ips[n]

    n = ran_int(ports)
    port_src = ports[n]

    n = ran_int(ports)
    port_des = ports[n]

    n = ran_int(protocols)
    protocol = protocols[n]

    return str.format('{0},{1},{2},{3},{4}\n', ip_src, port_src, ip_des, port_des, protocol).lower()


def ran_int(obj):
    return random.randint(0, len(obj) - 1)


if __name__ == '__main__':
    generate()
