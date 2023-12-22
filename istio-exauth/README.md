# Istio Egress Policy

This Helm chart installs Istio egress policy into an Istio
service mesh. Egress policy is most commonly needed when
`meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY` is set.

## Installation

The installation namespace is important when installing this helm chart. It's
value sets the Kubernetes namespace for all settings in this chart.

```sh
> helm template --namespace=[namespace] [chartname] | kubectl apply -f -
```

## Mediated vs Passthrough TLS

TLS traffic leaving the Istio mesh has two paths: mediated and passthrough.

On the mediated path services make unencrypted http calls in code, which are
immediately upgraded to https by the service's client Istio proxy. This allows
the client Istio proxy to enforce request policies like timeouts and retries.

On the passthrough path, services originate the TLS call in code by making an
https call. The service's client Istio proxy passes through the request to the
destination, but cannot modify the request because it is an already encrypted
stream of bytes.

## Values.yaml

All configuration for this policy is managed in `values.yaml`. Configuration
values can be overriden individually at installation using Helm's `--set` command
line option.

## Mediated TLS Values

This section contains a list of destinations and policy for mediated egress routes.
Due to limitations in Istio proxy, these routes _cannot_ be for wildcard hostnames.

* `mediatedTls.[host].externalHost` - The fully qualified domain name of the remote
  host. _No wildcard hostnames._
* `mediatedTls.[host].tlsMode` - The TLS mode Istio proxy should use when opening
  a connection to `externalHost`. Typically `SIMPLE`.
* `mediatedTls.[host].timeout` - The "top-level" timeout enforced when clients call
  `externalHost`. This timeout is inclusive of retries.
* `mediatedTls.[host].retries.*` - Istio configuration for client retry policy. See
  [Istio retry documentation](https://istio.io/latest/docs/reference/config/networking/virtual-service/#HTTPRetry) for values. Note: if retries are configured,
  a `timeout` greater than the sum of all retries must be used.
* `mediatedTls.[host].trafficPolicy.*` - Istio configuration for client traffic
  policy. See [Istio traffic policy documentation](https://istio.io/latest/docs/reference/config/networking/destination-rule/#TrafficPolicy-PortTrafficPolicy) for values.

## Passthrough TLS Values

This section contains a list of destinations and policy for passthrough egress routes.
These routes _can_ be for wildcard hostnames.

* `passthroughTls.[host].externalHost` - The fully qualified domain name of the remote
  host. _Wildcard hostnames allowed._


------

Integrating Istio with SecureAuth as the authentication server involves configuring Istio's authentication policies to enforce authentication using JWT tokens issued by SecureAuth. Below are the general steps to implement this setup:

Set Up SecureAuth:

First, you need to set up SecureAuth as your identity provider (IDP) and configure it to issue JWT tokens to authenticated users.
SecureAuth should be configured to generate JWT tokens with the necessary claims (e.g., user ID, roles) that your services rely on for authorization.
Deploy Your Services on Istio:

Deploy your microservices or APIs on Istio, either in Kubernetes or another environment.
Configure Istio Authentication:

Define Istio authentication policies to secure your services.
Configure Istio to validate JWT tokens issued by SecureAuth. This involves specifying the issuer, audience, and public key for token verification.
You can configure authentication policies at the service or ingress gateway level, depending on your architecture.
Define Virtual Services and Gateways:

Create Istio Virtual Services and Gateways to route traffic to your services and control which paths require authentication.
Define routing rules to specify when to apply authentication policies.
Secure Paths with Authentication Policies:

Apply authentication policies to specific paths or services by configuring the AuthorizationPolicy resource in Istio.

Specify the JWT issuer, audience, and public key to verify JWT tokens from SecureAuth.


Test and Monitor:

Test your setup by making API requests to your services and ensuring that Istio enforces authentication based on the JWT tokens issued by SecureAuth.
Monitor Istio's authentication and authorization logs to detect any issues or unauthorized access attempts.
Handle Token Renewal and Expiry:

Consider how token renewal and token expiry are handled in your architecture. SecureAuth may provide mechanisms for token renewal, and you should ensure that your services can handle token expiry gracefully.
Scale and Secure:

As your application scales, ensure that Istio and SecureAuth can handle increased traffic and load. Monitor and adjust your policies and configurations accordingly.