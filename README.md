# opsduty-client

> Python API client generator.

The actual API client is located in the `opsduty-client` folder.

The [openapi-python-client](https://github.com/openapi-generators/openapi-python-client)
tool is used to generate the OpsDuty client.

## Release a new version

1. Make sure the `package_version_override` version in `config.yml` is
   is set correctly.
2. Run `make generate-api-client` to generate a new client based on the
   [OpenAPI schema](https://opsduty.io/api/v1/openapi.json).
3. Make sure all desired changes are in the `main` branch.
4. Tag the release.

   There are multiple ways to tag a release. We recommend using the Github UI as this makes it easy to create a release with a well-written and well-formatted change log. After bumping the package version you navigate to the [new release page](https://github.com/opsduty/opsduty-client/releases/new). Fill in the correct tag version and release title.

   - Tag version: `opsduty-client/v0.1.0`
   - Release title: `opsduty-client v0.1.0`
