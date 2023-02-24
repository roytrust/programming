## Overview
### Security Principles
1. least privilege
2. 

### OAuth2
* Allows a user to authorize one application (a client), to send a request to an API (resource server), on the user's behalf to retrieve data at the resource server owned by the user. The application interacts with an authorization server which authenticates a user as part of obtaining their consent for the application to access their resources.
* Eliminates the requirement for users to share their credentials with the application.
* Authorization grant type: **authorization code** + PKCE, client credentials, refresh token.
* The **client credentials grant type** is for API calls where the application owns the requested resource.
* The **Device Authorization Grant type** is an extension defined to enable flows involving client devices that lack the capability needed for user interaction to authenticate and authorize requests.

#### Roles
* Resource Server - A service (with an API) storing protected resources to be accessed by an application.
* Resource Owner - A user or other entity that owns protected resources at the resource server.
* Client/application - An application which needs to access resources at the resouce server, on the resource owner's behalf or on its own behalf.
* Authorization Server - A service trusted by the resource server to authorize applications to call the resource server. It authenticates the application or resource owner and requests consent from the resource owner's behalf. With OAuth 2, the resouce server (API) is a relying party to the authorization server. The authorization server and resouce server may be operated by the same entity.

### Termnologies
* **Confidential Client** - An application that can securely store confidential secrets with which to authenticate itself to an authorization server or use another secure authentication mechanism for that purpose. Typically execute primarily on a protected server.
* **Public Client** - Typically execute primarily on the user's client device or in the client browser.
* **Client Profiles**: Web application, browser-based applicaiton, native applicaiton
* **Authorization Code** - An intermediary, opaque code returned to an application and used to obtain tokens. Used once.
* **Access Token** - A token used by an application to access an API. It represents the application's authorization to call an API and has an expiration.
* **Refresh Token** - An optional token that can be used by an application to request a new access token when a prior access token has expired.
* 

#### Best practices
* **Scope** should typically be used to model the coarse-grained privileges that an application can request of an API on a user's behalf, rather than granular privileges involving specific resources.
* Application should request access tokens restricted to a particular resource server via a "resource" or "audience" parameter.
* 

### OpenID Connect (OIDC)
* A layer on top of the OAuth2 to provide information in a standard format to applications about the idenity of an authenticated user. This provided a solution for applications for user authentication as well as API authorization.
* Enable SSO, obtain user profile info, claims
* **ID Token** - A token used to convey claims about an authentication event and an authenticated user to a relying party.
* **UserInfo Endpoint** - Returns claims about an authenticated user. Calling the endpoint requires an access token, and the claims returned are governed by the access token.
* **OIDC Flows**: Authorization, implicit, hybrid
* **CIBA** flow allows an application used by a third party to send a request to an OpenID Provider to authenticate a user via a device in the user's possession such as their cellphone.

#### Roles
* **End User** - A subject to be authenticated.
* **OpenID Provider (OP)** - An OAuth 2 authorization server that implements OIDC and can authenticate a user and return claims about the anthenticated user and the authentication event to a relying party (application).
* **Relying Party (RP)** - An OAuth 2 client which delegates user authentication to an OpenID Provider and requests claims about the user from the OpenID Provider. Generally application.




### SAML2 - Federated Identity - Security Assertion Markup Language
* Fetures: Cross-demain single sign-on (SSO), identity federation.
* IdP (identity provider), identity federation
