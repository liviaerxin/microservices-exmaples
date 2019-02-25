# cert-manager

referencing to [Welcome to cert-manager’s documentation!
](https://docs.cert-manager.io/en/latest/index.html).


# Step Up Issuers

```
$ kubectl apply -f ingress/cert-manager/issuer/letsencrypt-staging.yaml
$ kubectl kubectl describe ClusterIssuer
```

# Manully Issue Certificate for Ingress resources

1. issue certificates

```
$ kubectl apply -f ingress/cert-manager/certificate/amazonaws-com.yaml

```


2. use certificates in form of secrets


```
$ kubectl apply -f ingress/cert-manager/ingress-tls.yaml

```



# Automatically Create Certificates for Ingress resources

[How it works
](https://docs.cert-manager.io/en/latest/tasks/issuing-certificates/ingress-shim.html)



```
$ kubectl apply -f ingress/cert-manager/ingress-auto-tls.yaml

```


# Verify SSL

```
$ curl -v https://peggy.gq/apple
*   Trying 52.203.197.40...
* Connected to peggy.gq (52.203.197.40) port 443 (#0)
* found 148 certificates in /etc/ssl/certs/ca-certificates.crt
* found 592 certificates in /etc/ssl/certs
* ALPN, offering http/1.1
* SSL connection using TLS1.2 / ECDHE_RSA_AES_256_GCM_SHA384
*    server certificate verification OK
*    server certificate status verification SKIPPED
*    common name: peggy.gq (matched)
*    server certificate expiration date OK
*    server certificate activation date OK
*    certificate public key: RSA
*    certificate version: #3
*    subject: CN=peggy.gq
*    start date: Fri, 22 Feb 2019 09:02:27 GMT
*    expire date: Thu, 23 May 2019 09:02:27 GMT
*    issuer: C=US,O=Let's Encrypt,CN=Let's Encrypt Authority X3
*    compression: NULL
* ALPN, server accepted to use http/1.1
> GET /apple HTTP/1.1
> Host: peggy.gq
> User-Agent: curl/7.47.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Server: nginx/1.15.6
< Date: Fri, 22 Feb 2019 10:12:29 GMT
< Content-Type: text/plain; charset=utf-8
< Content-Length: 6
< Connection: keep-alive
< X-App-Name: http-echo
< X-App-Version: 0.2.3
< Strict-Transport-Security: max-age=15724800; includeSubDomains
< 
apple
* Connection #0 to host peggy.gq left intact

```



# Debug && Trouble Shooting

```
$ kubectl get pods -n cert-manager

$ kubectl describe pod cert-manager-554888495d-g2tpp -n cert-manager

$ kubectl logs cert-manager-554888495d-g2tpp -n cert-manager
I0222 08:48:18.334147       1 controller.go:183] orders controller: syncing item 'default/amazonaws-com-3751265414'
I0222 08:48:18.334327       1 logger.go:38] Calling CreateOrder
E0222 08:48:18.526672       1 controller.go:185] orders controller: Re-queuing item "default/amazonaws-com-3751265414" due to error processing: error creating new order: acme: urn:ietf:params:acme:error:rejectedIdentifier: Error creating new order :: Policy forbids issuing for name
I0222 08:50:58.527113       1 controller.go:183] orders controller: syncing item 'default/amazonaws-com-3751265414'
I0222 08:50:58.527309       1 logger.go:38] Calling CreateOrder
E0222 08:50:58.740609       1 controller.go:185] orders controller: Re-queuing item "default/amazonaws-com-3751265414" due to error processing: error creating new order: acme: urn:ietf:params:acme:error:rejectedIdentifier: Error creating new order :: Policy forbids issuing for name


```

[Policy forbids issuing for name on Amazon EC2 domain](https://community.letsencrypt.org/t/policy-forbids-issuing-for-name-on-amazon-ec2-domain/12692)


[Find A Free Domain Name](http://www.dot.tk)

[Free Domain Name](https://www.freenom.com/en/index.html?lang=en)