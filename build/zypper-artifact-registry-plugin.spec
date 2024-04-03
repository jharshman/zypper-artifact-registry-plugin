%define name zypper-artifact-registry-plugin
%define version 0.0.1
%define release 0

Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2
Packager: Josh Harshman <josh.harshman@bit.ly>
Summary: Zypper Plugin for using GCP Artifact Registry
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Source: zypper-artifact-registry-plugin.tar.gz

%description
GCP Artifact Registry provides a YUM/RPM Repository. In order to authenticate, Google provides a YUM and DNF plugin but lacks
a plugin for Zypper. This Zypp Plugin allows Zypper to authenticate to GCP's Artifact Registry using a Service Account file.

While both the Yum and DNF Plugins provided by Google leverage an external Go binary to fetch the Bearer token, this Plugin
accomplishes the same task without having to invoke an external binary.

Requires: libzypp
Requires: python3
Requires: python3-zypp-plugin
Requires: python3-google-api-python-client

%prep
%setup -qn zypper-artifact-registry-plugin

%install
mkdir -p %{buildroot}/usr/lib/zypp/plugins/urlresolver
cp ./src/ArtifactRegistryPlugin %{buildroot}/usr/lib/zypp/plugins/urlresolver/

%files
%defattr(777, root, root, -)
/usr/lib/zypp/plugins/urlresolver/ArtifactRegistryPlugin

