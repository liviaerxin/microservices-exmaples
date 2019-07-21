# Consul

Start a single-node server for testing purposes like so:

```sh
docker run --rm --name consul -p 8500:8500 consul agent -server -bootstrap -ui -client=0.0.0.0 -bind=0.0.0.0

docker run --rm --name consul -p 8500:8500 consul agent -dev -ui -client=0.0.0.0 -bind=0.0.0.0
```


Register service

```sh


#IP=`ip addr | grep -E 'eth0.*state UP' -A2 | tail -n 1 | awk '{print $2}' | cut -f1 -d '/'`
#NAME="$2-service"

IP="127.0.0.1"
NAME="test-service"
PORT=9090

# TODO: use $variable
read -d '' MSG <<-"_EOF_"
{
  "Name": "test-service",
  "address": "127.0.0.10",
  "port": 9090,
  "Check": {
     "http": "http://127.0.0.1:9090",
     "interval": "5s"
  }
}
_EOF_


curl -v -XPUT -d "$MSG" http://127.0.0.1:8500/v1/agent/service/register
```

TODO: Delete service

[Health Checks](https://www.consul.io/docs/agent/checks.html)
