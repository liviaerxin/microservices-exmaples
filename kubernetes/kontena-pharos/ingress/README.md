# Ingress

# Manually configure SSL
## Create SSL certificate for host `ec2-52-203-197-40.compute-1.amazonaws.com`:

```sh
$ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=ec2-52-203-197-40.compute-1.amazonaws.com/O=nginxsvc"

$ kubectl create secret tls secret-tls --key tls.key --cert tls.crt

# or

$ cat tls.crt | base64 -w 0
# or
$ base64 tls.crt -w 0

# finally

$ kubectl get secret secret-tls
```

## Integrate SSL certificate with ingress `ingress-tls.yaml`

```sh
$ kubectl apply -f ingress/ingress-tls.yaml
```

# Automatically configure, rotate SSL

## cert-manager

[Installing cert-manager](https://docs.cert-manager.io/en/latest/getting-started/install.html#installing-with-regular-manifests)

[Quick-Start using Cert-Manager with NGINX Ingress](https://docs.cert-manager.io/en/latest/tutorials/acme/quick-start/index.html)


[How to Set Up an Nginx Ingress with Cert-Manager on DigitalOcean Kubernetes ](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nginx-ingress-with-cert-manager-on-digitalocean-kubernetes)








# Debug

```sh
$ kubectl describe pod/nginx-ingress-controller-4q7pg -n ingress-nginx
$ kubectl logs nginx-ingress-controller-4q7pg -n ingress-nginx
$ kubectl describe ing ingress-tls
$ kubectl describe configmap nginx-config -n ingress-nginx

$ kubectl exec -it nginx-ingress-controller-4q7pg -n ingress-nginx -- /bin/bash
/etc/nginx$ 

```