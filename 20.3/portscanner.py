# BT Port Scanner - Exercise 6.19 Solution

from scapy.all import sr1, IP, TCP

print "[BT PORT SCANNER]\n"
dest = raw_input("Enter destination IP address: ")
for i in range(20, 1025):
    tcp_seg = TCP(dport=i, sport=2057, flags='S')
    tcp_packet = IP(dst=dest)/tcp_seg
    tcp_res = sr1(tcp_packet, timeout=1, verbose=0)
    if str(type(tcp_res)) == "<type 'NoneType'>":
        print "[" + str(i) + "] => CLOSED\n"
    elif tcp_res.haslayer(TCP):
        if tcp_res.getlayer(TCP).flags == 18:
            tcp_seg.flags = 'A'
            tcp_seg.ack = tcp_res.getlayer(TCP).seq + 1
            tcp_packet = IP(dst=dest)/tcp_seg
            tcp_res = sr1(tcp_packet, timeout=1, verbose=0)
            print "[" + str(i) + "] => OPEN\n"
        else:
            print "[" + str(i) + "] => CLOSED\n"
