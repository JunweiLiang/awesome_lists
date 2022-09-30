# coding=utf-8
# author: Junwei Liang
# for: setting up a SSH tunnel between this machine and a gateway machine

# sample usage: $ python start_tunnel.py 666.666.666.666 --server_port 21222 --retry_limit 500 --wait_secs 600

# then, on a remote laptop, you can connect to this machine through the gateway machine via
# $ ssh -J your_username@666.666.666.666 -p 21222 your_username@localhost
# $ scp -o ProxyJump=your_username@666.666.666.666 -P 21222 your_username@localhost:source_file dest_path

# Good references:
# https://unix.stackexchange.com/questions/46235/how-does-reverse-ssh-tunneling-work#
# https://www.tecmint.com/create-ssh-tunneling-port-forwarding-in-linux/
# https://serverfault.com/questions/595323/ssh-remote-port-forwarding-failed
# https://unix.stackexchange.com/questions/3026/what-do-options-serveraliveinterval-and-clientaliveinterval-in-sshd-config-d

import os
#import subprocess as commands
import subprocess
import time

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("server_ip")
parser.add_argument("--retry_limit", default=1000, type=int)
parser.add_argument("--server_port", default=22222, type=int)
parser.add_argument("--to_local_port", default=22, type=int)
parser.add_argument("--wait_secs", default=700, type=int,
                    help="this should be larger than server side's sshd_config ClientAliveInterval*ClientAliveCountMax")

def get_time_str_now():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

if __name__ == "__main__":
    args = parser.parse_args()
    trys = 0
    while True:
        if trys >= args.retry_limit:
            break
        print("*"*40)
        print("tunneling start at %s, try # %s" % (get_time_str_now(), trys))
        cmd = "ssh -o ExitOnForwardFailure=yes -N -T -R%d:localhost:%d %s" % (
            args.server_port, args.to_local_port, args.server_ip)
        print("run cmd: %s" % cmd)
        output = subprocess.getoutput(cmd)
        print("Exited at %s, cmd outputs:" % (get_time_str_now()))
        print(output)
        time.sleep(args.wait_secs)
        trys += 1
    print("Full system exit at %s" % get_time_str_now())
