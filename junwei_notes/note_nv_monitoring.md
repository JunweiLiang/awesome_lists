# note for monitoring utilization of independent GPU nodes

当你的组里有很多独立的机器时，比如我的组有9台单机，一共30张卡(RTX 3090/4090)，想知道一段时间里这些机器的GPU利用率（一般商用的集群都会有这样的功能），可以用到下面说的工具。

1. Use upyterlab_nvdashboard

`https://github.com/rapidsai/jupyterlab-nvdashboard`

Run this on the node you want to monitor
```
python -m jupyterlab_nvdashboard.server 9988
```

Then you can open a html to see the log `http://10.30.8.195:9988/GPU-Resources`
The log is only saved on the web page. No database is used. So you need to keep the web page opened.


2. use rntop from run-ai

`https://github.com/run-ai/rntop`

This is better for monitoring multiple nodes. 原理：通过 ssh user@IP nvidia-smi 每个节点，然后记录GPU利用率到一个文件。

Suppose you have a head node. Need to put the head node's id_rsa.pub to all the GPU nodes' authorized_keys.

Run the following in a screen. The output file will be saved to `/home/junweil/nv_monitoring/rntop.log`
```
(base) junweil@junwei-home-lab:~/nv_monitoring$ sudo docker run -it --rm -v $HOME/.ssh:/root/.ssh -v $HOME/nv_monitoring:/host runai/rntop --output /host/rntop.log junweil@10.30.8.195 junweil@10.30.9.54 junweil@10.30.11.195 junweil@10.30.11.48 junweil@10.30.10.22 junweil@10.30.10.151 junweil@10.30.9.197 junweil@10.30.11.44 junweil@10.30.10.99
```

Then you can upload the log file to `https://run-ai.github.io/rntop-board/`
