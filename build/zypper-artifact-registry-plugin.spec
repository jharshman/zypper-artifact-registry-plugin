%define name libzypp-artifact-registry-plugin
%define version 0.0.1
%define release 0

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL-2.0
Summary:        libzypp extension to access GCP Artifact Registry
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
URL:            https://github.com/jharshman/zypper-artifact-registry-plugin
Source:         zypper-artifact-registry-plugin.tar.gz
BuildRequires:  libzypp
BuildRequires:  python3-zypp-plugin
Requires:       python3-google-api-python-client
Group:          System/Packages
BuildArch:      noarch

%description
GCP Artifact Registry provides a YUM/RPM Repository. In order to authenticate, 
Google provides a YUM and DNF plugin but lacks a plugin for libzypp. This Zypp 
Plugin allows Zypper to authenticate to GCP's Artifact Registry using a Service
Account file.

While both the Yum and DNF Plugins provided by Google leverage an external Go
binary to fetch the Bearer token, this plugin accomplishes the same task 
without having to invoke an external binary.


%prep
%setup -qn zypper-artifact-registry-plugin

%check

%build 

%install
install -D -m 755 ./src/ArtifactRegistryPlugin %{buildroot}/usr/lib/zypp/plugins/urlresolver/ArtifactRegistryPlugin

%files
%attr(755, root, root) /usr/lib/zypp/plugins/urlresolver/ArtifactRegistryPlugin

%changelog


