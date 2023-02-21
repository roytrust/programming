## Overview
### Security Principles
1. least privilege
2. 

## OAuth2, OpenID Connect


### OAuth2
* Allows a user to authorize one application (a client), to send a request to an API (resource server), on the user's behalf to retrieve data at the resource server owned by the user. The application interacts with an authorization server which authenticates a user as part of obtaining their consent for the application to access their resources.

#### Roles
* Resource Server - A service (with an API) storing protected resources to be accessed by an application.
* Resource Owner - A user or other entity that owns protected resources at the resource server.
* Client/application - An application which needs to access resources at the resouce server, on the resource owner's behalf or on its own behalf.
* Authorization Server - A service trusted by the resource server to authorize applications to call the resource server. It authenticates the application or resource owner and requests consent from the resource owner's behalf. With OAuth 2, the resouce server (API) is a relying party to the authorization server. The authorization server and resouce server may be operated by the same entity.

### OpenID Connect (OIDC)
* A layer on top of the OAuth2 to provide information in a standard format to applications about the idenity of an authenticated user. This provided a solution for applications for user authentication as well as API authorization.



### SAML2 - Federated Identity - Security Assertion Markup Language
* IdP (identity provider), identity federation
