sh```
curl -X GET \
  http://127.0.0.1:8888 \
  -H 'Authorization: AWS4-HMAC-SHA256 Credential=AKIAJP6YFKLWX2HYIV7Q/20181006/ap-northeast-2/s3/aws4_request, SignedHeaders=host;range;x-amz-content-sha256;x-amz-date, Signature=dff35955de71aab7d324ce1a9ecf12214c594d42958ec54f292d55d76693b531' \
  -H 'Postman-Token: bf43db3d-6aa8-4ae9-bfd3-98c88d198c98' \
  -H 'cache-control: no-cache' \
  -H 'range: bytes=0-9999999999' \
  -H 'x-amz-content-sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' \
  -H 'x-amz-date: 20181006T090356Z'
```

sh```
curl -X POST \
  http://127.0.0.1:8888 \
  -H 'Authorization: AWS4-HMAC-SHA256 Credential=AKIAJP6YFKLWX2HYIV7Q/20181006/ap-northeast-2/s3/aws4_request, SignedHeaders=host;range;x-amz-content-sha256;x-amz-date, Signature=dff35955de71aab7d324ce1a9ecf12214c594d42958ec54f292d55d76693b531' \
  -H 'Postman-Token: bf43db3d-6aa8-4ae9-bfd3-98c88d198c98' \
  -H 'cache-control: no-cache' \
  -H 'range: bytes=0-9999999999' \
  -H 'x-amz-content-sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' \
  -H 'x-amz-date: 20181006T090356Z' \
  -H 'Content-Length: 10' \
  -d 'xxxxxxxxxx'
```