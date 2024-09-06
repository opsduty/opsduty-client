# How to get an access token

1. Install [oauth2c](https://github.com/cloudentity/oauth2c)

```bash
brew install cloudentity/tap/oauth2c
```

2. Create a new [oAuth2 application](https://opsduty.io/app/organization/developer-settings) in OpsDuty

Use the redirect url `http://localhost:9876/callback`

3. Copy the new client secret to clipboard

4. Get an access token

```bash
oauth2c https://opsduty.io \
  --client-id <client-id> \
  --client-secret <client-secret> \
  --authorization-endpoint https://opsduty.io/oauth2/authorize/ \
  --token-endpoint https://opsduty.io/oauth2/token/ \
  --response-types code \
  --response-mode query \
  --grant-type authorization_code \
  --auth-method client_secret_basic \
  --pkce
```
