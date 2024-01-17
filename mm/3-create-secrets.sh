
## Create secret of type tls. The secret will be referred by the Istio Ingress Gateway.
#kubectl create -n istio-system secret tls deopsschool-credential --key=secure.deopsschool.com.key --cert=secure.deopsschool.com.crt;

## Create secret for Mutual Authentication. This is generic type secret.
kubectl create -n istio-system secret generic mutual-credential --from-file=tls.key=certs/secure.istio.com.key --from-file=tls.crt=certs/secure.istio.com.crt --from-file=ca.crt=certs/istio.com.crt;
