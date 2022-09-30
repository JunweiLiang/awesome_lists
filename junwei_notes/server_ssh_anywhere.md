## How to make home machines SSH-able from anywhere

### Problem

As DL researchers, we may have one or two GPU servers at home that are used to run our own experiments.
However, unlike machines hosted at universities, home servers may not have public IPs
(even if there is one, you usually get one public IP at your doorstep and things get tricky if you have multiple machines).
This guide provides my solution to solve the aforementioned problem.

如果你有GPU电脑在家里，想要能远程访问（一般家庭网络都没有公网IP），这里提供我的经验。


+ [You have a public IP (via port forwarding)](#with-a-public-ip)
+ [No-public-IP home network (via SSH tunnel)](#no-public-ip)


### With a Public IP

In this scenario, assuming you can get a publicly accessible IP for your home network ISP,
whether it is a dynamic IP or a static one, you can achieve SSH capabilities by simply
setting port forwarding on your modem.
You can check this by directly connecting your Linux machine (SSH-server enabled) to the modem through a wired connection,
and use any website to check your IP, and then try to SSH to that IP.
If successful, then you have a public IP for your home network.
From my experience, Comcast provides static IP in Pittsburgh (they say it is dynamic IP but it never changes).

To sum up,

+ Step 1, get your public IP and write it down. Or you could use a free DNS service.
Basically, you install a client in your machine to continuously tell the DNS provider your current IP address.
Then you can SSH through the domain name of your choosing. This is essential if you have a dynamic IP.

+ Step 2, set port forwarding through the admin page of your modem (or maybe the router connected to the modem).
I remembered I had a Comcast-compatible modem+wireless router combo and I could
set port forwarding without much pain. Basically you set a random port for each of your machines (at 192.168.1.xxx)
and then you can SSH to your machine from anywhere on earth via `ssh -p port_number your_username@your_domain_or_IP`.


### No Public IP

This is what I have encountered in China (both with ISPs like 联通 and 移动).
It seems they put their whole customer networks into a giant virtual network so
you cannot access your machines through the reported public IP.
Here we need to use a **middle-man machine** with a public IP.
Basically we are going to set up an "ssh tunnel" between the middle-man machine
and your home machine.
So you could access your home machine directly through one SSH command through the middle-man.

To sum up,

+ Step 1, get a cloud CPU Linux machine with a public IP. I got a machine with 2 vCPUs & 2GB RAM on Aliyun for a year for only ¥230
(the cost of network traffic is pay-as-used).
Install SSH server on your middle-man/cloud machine and your home machines. Duh.
Put your remote laptop and your home machines' SSH public key on the cloud machine's authorized_keys
(so you won't need to enter two passwords each time you try to connect your home machine with your remote laptop).
Put your cloud machine's SSH public key to your home machines' authorized_keys. **Set your cloud machine's SSH server to allow GatewayPorts by modifying the sshd_config.**
See [here](https://www.tecmint.com/create-ssh-tunneling-port-forwarding-in-linux/).

+ Step 2,
On each of your home machines, run [this script](./start_tunnel.py) in the background.
This script is a result of a lot of Googling and it basically helps you keep the SSH tunnel alive.

+ Step 3,
Suppose you put a home machine to port 21222 of the cloud machine for the tunnel.
You can then connect to this home machines on your remote laptop by:
```
$ ssh -J your_username@666.666.666.666 -p 21222 your_username@localhost
$ scp -o ProxyJump=your_username@666.666.666.666 -P 21222 your_username@localhost:source_file dest_path
```

Good references through a lot of Googling:

https://unix.stackexchange.com/questions/46235/how-does-reverse-ssh-tunneling-work#

https://www.tecmint.com/create-ssh-tunneling-port-forwarding-in-linux/

https://serverfault.com/questions/595323/ssh-remote-port-forwarding-failed

https://unix.stackexchange.com/questions/3026/what-do-options-serveraliveinterval-and-clientaliveinterval-in-sshd-config-d

