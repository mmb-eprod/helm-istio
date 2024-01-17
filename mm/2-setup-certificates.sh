## Create signer certificate
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -subj '/O=istio/CN=istio.demo' -keyout certs/istio.com.key -out certs/istio.com.crt;

## Create CSR 
openssl req -out certs/secure.istio.com.csr -newkey rsa:2048 -nodes -keyout certs/secure.istio.com.key -subj "/CN=istio.demo/O=istio";

## Produce signed cert
openssl x509 -req -days 365 -CA certs/istio.com.crt -CAkey certs/istio.com.key -set_serial 0 -in certs/secure.istio.com.csr -out certs/secure.istio.com.crt;
