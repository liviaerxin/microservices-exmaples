# Purpose  
install Kontena Pharos on local host and create a Kubernetes cluster in aws. see `cluster.yaml` for configuration.  

# Installation  
Before installing pharos in loca and spinning up machines in aws cluster, Please read the [Host Requirements](https://pharos.sh/docs/requirements.html) in depth.  

Referring [Get Started](https://pharos.sh/docs/getting-started.html) will boostrap and manage a Kubernetes cluster easily.


# After Setup  
```sh
$ kubectl cluster-info
Kubernetes master is running at https://18.232.115.164:6443
KubeDNS is running at https://18.232.115.164:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
Metrics-server is running at https://18.232.115.164:6443/api/v1/namespaces/kube-system/services/https:metrics-server:/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.


$ kubectl get nodes
NAME            STATUS   ROLES    AGE   VERSION
ip-10-0-2-122   Ready    worker   50m   v1.12.4
ip-10-0-2-20    Ready    worker   50m   v1.12.4
ip-10-0-2-206   Ready    master   51m   v1.12.4

```

port `6443` on master is occupied by `kube-apiserver`.  