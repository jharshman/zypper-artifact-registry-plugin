# Zypper Artifact Registry Plugin

[![build result](https://build.opensuse.org/projects/home:josh.harshman/packages/zypper-artifact-registry-plugin/badge.svg?type=default)](https://build.opensuse.org/package/show/home:josh.harshman/zypper-artifact-registry-plugin)

Loosely inspired by the [artifact-registry-yum-plugin](https://github.com/GoogleCloudPlatform/artifact-registry-yum-plugin/tree/main).
Allows Zypper to use GCP's Artifact Registry RPM Repositories.

### How it Works

Once installed, an Artifact Repo definition in `/etc/zypp/repos.d/` may be configured.
However, the official GCP documentation does not take into account configuration for use with a `libzypp` plugin.

The `baseurl` in the entry must adhere to the following format.
```
baseurl=plugin:<PLUGIN_NAME>?param1=val1&param2=val2
```

This Plugin requies two parameters in the `baseurl` entry.
1. url: The URL of the Artifact Registry Repository
2. token: A GCP Service Account Credentials File located in `/etc/zypp/credentials.d/`

So provided we have:
- An AR Repo url of `https://us-yum.pkg.dev/projects/my-awesome-project/my-rpms`
- A Service Account file named `ar-sa.json`

The `baseurl` would look like:
```
baseurl=plugin:ArtifactRegistryPlugin?url=https://us-yum.pkg.dev/projects/my-awesome-project/my-rpms&token=ar-sa.json
```

> Note: The Plugin looks for the Service Account JSON file in `/etc/zypp/credentials.d`. There is no need to specify the path.

### Quick Start

Copy the following and replace `PROJECT_ID`, `REPO_NAME`, and `SERVICE_ACCOUNT_TOKEN.json`
with the appropriate values for your use case.

```bash
[artifactregistry]
name=artifactregistry
baseurl=plugin:ArtifactRegistryPlugin?url=https://us-yum.pkg.dev/projects/PROJECT_ID/REPO_NAME&token=SERVICE_ACCOUNT_TOKEN.json
enabled=1
autorefresh=0
gpgcheck=0
```
