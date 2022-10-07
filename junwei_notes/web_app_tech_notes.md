## How To Make Web-Accessible Demos For Your AI Research/Applications

### Problem

As DL researchers, we may want to put up web apps to showcase our research work.
Here I present my experiences in setting up different types of demos.
You can use it as a guide to put up a project page and/or **quickly** deploy a minimum viable product.
Here I also show you how to make a publicly accessible web app that requires GPU computation from a home machine.

这篇指南总结我组建demo网站的经验，从简单的静态项目页面到需要GPU计算的Web程序，并介绍如何可以通过公网IP访问（比如部署在家庭网络的GPU机器）。


+ [What framework/server to use](#choosing-the-framework)
+ [How to make it publicly accessible from home](#how-to-make-it-publicly-accessible-from-home)
+ [GPU Demo Tech Tips](#gpu-demo-tech-tips)

### Choosing The Framework

I believe every published research paper in CV/AI should be accompanied by a Github repo and a project page.

In the simplest form, the project page could be just images (GIFs would be better to show your ideas) and text, and pointers to the repo and paper.
In this case, simple static htmls would be enough.
In terms of **where to host them**, here are the **free** options.
At CMU each student has a folder under the cs.cmu.edu domain so we could just put the projects under our folder and they are publicly accessible.
Some people would create a Github account specifically for that project to get it accessible through project.github.io.
If you don't mind spending some money, you could get your own domain and rent a cloud machine to host your projects there.
In this case, you will need to install your own server on the cloud machine.
I use [XAMPP](https://www.apachefriends.org/) since it is easy to install and the Apache server comes with PHP and MySQL.
Remember to learn some basic security-related configuration tips.
Then you can serve the project htmls on the cloud machine through your domain.
You can checkout my static page [project1](https://github.com/JunweiLiang/VERA_3D_Reconstruction), [project2](https://github.com/JunweiLiang/junweiliang.github.io), and PHP [project1](https://github.com/JunweiLiang/VERA_Shooter_Localization), [project2](https://github.com/JunweiLiang/Lecture_Attendance_Management).

For more complex demos that require some computing (especially with GPUs) during inference time, I would recommend building one with [Flask](https://flask.palletsprojects.com/en/2.2.x/).
It requires minimal additional code. Basically you write a python function for each POST/GET request and that's all (and some htmls).

### How to make it publicly accessible from home

Let's say you want to host your complex AI projects or even static htmls on your home GPU machines.
But you don't have a public IP for your home network.
We could use the SSH tunneling technique I mentioned [in another note](./server_ssh_anywhere.md).
Here is what we need to do:

+ Step 1,
rent the cheapest Linux cloud machine with a public IP.
I got a machine with 2 vCPUs & 2GB RAM on Aliyun for a year for only ¥230
(the cost of network traffic is pay-as-used).
Install SSH server on your middle-man/cloud machine and your home machines. Duh.
Put your remote laptop and your home machines' SSH public key on the cloud machine's authorized_keys
(so you won't need to enter two passwords each time you try to connect your home machine with your remote laptop).
Put your cloud machine's SSH public key to your home machines' authorized_keys. **Set your cloud machine's SSH server's GatewayPorts and AllowTcpForwarding to yes by modifying the sshd_config.** (at `/etc/ssh/sshd_config`)
See [here](https://www.tecmint.com/create-ssh-tunneling-port-forwarding-in-linux/).
Also, you need to configure the cloud machine to allow TCP traffic through your port(s) for the demos (21222 in the example below).

+ Step 2,
on your demo machine, run [this script](./start_tunnel.py) in the background.
This script is a result of a lot of Googling and it basically helps you keep the SSH tunnel alive.
Example for Apache server (default using port 80):
```
$ python start_tunnel.py 666.666.666.666 --retry_limit 500 --wait_secs 800 --server_port 21222 --to_local_port 80
```
So then you could access your project page from the browser through http://666.666.666.666:21222.
For any Flask app, change the `--to_local_port` accordingly.

### GPU Demo Tech Tips

We usually use Python with Tensorflow/PyTorch to build models for our research work.
Let's say you want to build a demo that could run model inference given any user-provided inputs.
[Flask](https://flask.palletsprojects.com/en/2.2.x/) is Python-based so you could directly copy-and-paste your inference code.
All you need to do is add some good-looking htmls to show the results (and provide a uploading inferface of course).
I would even just use subprocess to invoke a shell call to the model inference main script within the Flask app
(so you don't need to change any more code if you update your model inference code).

When building GPU demo with Flask, it usually involves uploading images/videos from the browser and then a long computing time before results are presented.
I use Ajax POST to submit the computing job to a Flask function that calls model inference (and the users would stay on that page).
And to improve user experiences, I would design a progress bar for the computing wait time.
I would use simple [Ajax Pooling](https://medium.com/geekculture/ajax-polling-vs-long-polling-vs-websockets-vs-server-sent-events-e0d65033c9ba#:~:text=Polling%20is%20a%20standard%20technique,an%20empty%20response%20is%20returned.) to repeatedly get the progress of the processing (so in the processing script, step-wise progress should be updated to a file. No database needed).
Users would be directed to the result page once the computing is completed.

