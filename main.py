import csv


class PolicyRow:
    ip_src = None
    port_src = None
    ip_des = None
    port_des = None
    protocol = None
    action = None

    def __init__(self, row):
        self.ip_src = str(row[0]).lower()
        self.port_src = str(row[1]).lower()
        self.ip_des = str(row[2]).lower()
        self.port_des = str(row[3]).lower()
        self.protocol = str(row[4]).lower()
        self.action = str(row[5]).lower()

    def print_all(self):
        print str.format('ip_src: {0}, port_src: {1}, ip_des: {2}, port_des: {3}, protocol: {4}, action: {5}',
                         self.ip_src, self.port_src, self.ip_des, self.port_des, self.protocol, self.action)


def load_policy(policy_file):
    global table_policy
    table_policy = []
    with open(policy_file) as csv_policy:
        csv_reader = csv.reader(csv_policy, delimiter=',')

        line_counter = 0;
        for row in csv_reader:
            if line_counter == 0:
                line_counter += 1
            else:
                table_policy.append(PolicyRow(row))

    for x in table_policy:
        x.print_all()

    print '\n\n\n'


def load_traffic(traffic_file):
    traffic = []
    with open(traffic_file) as csv_traffic:
        csv_reader = csv.reader(csv_traffic, delimiter=',')

        line_counter = 0
        for row in csv_reader:
            if traffic.__contains__(row):
                continue

            traffic.append(row)
            if line_counter == 0:
                line_counter += 1
            else:
                check_allow_drop(row)

    print 'Done!'


def check_allow_drop(t):  # t - traffic row
    global table_policy

    for p in table_policy:
        if compare_values(p, t):
            if p != table_policy[len(table_policy) - 1]:
                # print t, '\t\tAction: ', p.action
                print str.format(
                    '({0}:{1}), ({2}:{3}), ({4}:{5}), ({6}:{7}), ({8}:{9}), Action: {10}',
                    p.ip_src, t[0], p.port_src, t[1], p.ip_des, t[2], p.port_des, t[3], p.protocol, t[4], p.action)


def compare_values(p, t):
    o1 = legit_ip_src(p.ip_src, t[0])
    o2 = legit_port_src(p.port_src, t[1])
    o3 = legit_ip_des(p.ip_des, t[2])
    o4 = legit_port_src(p.port_des, t[3])
    o5 = legit_protocol(p.protocol, t[4])

    return o1 and o2 and o3 and o4 and o5


def legit_ip_src(p, t):  # p - policy, t - traffic
    if str(p).lower() == 'any' or p == t:
        return True
    return False


def legit_port_src(p, t):  # p - policy, t - traffic
    if str(p).lower() == 'any' or p == t:
        return True
    return False


def legit_ip_des(p, t):  # p - policy, t - traffic
    if str(p).lower() == 'any' or p == t:
        return True
    return False


def legit_port_des(p, t):  # p - policy, t - traffic
    if str(p).lower() == 'any' or p == t:
        return True
    return False


def legit_protocol(p, t):  # p - policy, t - traffic
    if str(p).lower() == 'any' or p == t:
        return True
    return False


if __name__ == '__main__':
    load_policy('policy.csv')
    load_traffic('traffic.csv')
