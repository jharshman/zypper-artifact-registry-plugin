FROM --platform=arm64 opensuse/leap:15.5

RUN zypper in -y rpm-build rpmdevtools
RUN rpmdev-setuptree /root/

WORKDIR /root/
COPY . ./zypper-artifact-registry-plugin/


RUN tar -czv --exclude-vcs -f zypper-artifact-registry-plugin.tar.gz zypper-artifact-registry-plugin \
  && mv zypper-artifact-registry-plugin.tar.gz ./rpmbuild/SOURCES/ \
  && cp zypper-artifact-registry-plugin/build/artifact-registry-plugin.spec ./rpmbuild/SPECS/

RUN rpmbuild -bb ./rpmbuild/SPECS/artifact-registry-plugin.spec

