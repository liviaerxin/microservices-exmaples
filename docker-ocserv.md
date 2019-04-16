docker run --name ocserv --privileged -e NO_TEST_USER=1 -p 23:443 -p 23:443/udp -d tommylau/ocserv

docker exec -ti ocserv ocpasswd -c /etc/ocserv/ocpasswd -g "Route,All" frank

docker run --name

[](https://www.linuxbabe.com/ubuntu/certificate-authentication-openconnect-vpn-server-ocserv)


`--pkcs-cipher 3des-pkcs12 ` for ios



export user=frank

docker run --name ocserv --privileged -e NO_TEST_USER=1 -p 443:443 -p 443:443/udp -d tommylau/ocserv

docker exec -it ocserv ocpasswd -c /etc/ocserv/ocpasswd -g "Route,All" $user

docker exec -ti ocserv ocpasswd -c /etc/ocserv/ocpasswd -d test

docker exec -it ocserv /bin/sh -c "cd /etc/ocserv/certs && certtool --generate-privkey --outfile client-key.pem"

cat > client.tmpl <<EOF
organization = "My Org"
cn = "John Doe"
uid = "$user"
expiration_days = 3650
tls_www_client
signing_key
encryption_key
EOF

docker cp client.tmpl ocserv:/etc/ocserv/certs/

docker exec -it ocserv /bin/sh -c "cd /etc/ocserv/certs && certtool --generate-certificate --load-privkey client-key.pem --load-ca-certificate ca.pem --load-ca-privkey ca-key.pem --template client.tmpl --outfile client-cert.pem"

docker exec -it ocserv /bin/sh -c "cd /etc/ocserv/certs && certtool --to-p12 --load-privkey client-key.pem --load-certificate client-cert.pem --pkcs-cipher 3des-pkcs12 --outfile client.p12 --outder"

docker cp ocserv:/etc/ocserv/certs/client.p12 ./



`client.tmpl`
```sh
# X.509 Certificate options
# The organization of the subject.
organization = "My Org"

# The common name of the certificate owner.
cn = "John Doe"

# A user id of the certificate owner.
uid = "username"

# In how many days, counting from today, this certificate will expire. Use -1 if there is no expiration date.
expiration_days = 3650

# Whether this certificate will be used for a TLS server
tls_www_client

# Whether this certificate will be used to sign data
signing_key

# Whether this certificate will be used to encrypt data (needed
# in TLS RSA ciphersuites). Note that it is preferred to use different
# keys for encryption and signing.
encryption_key
```