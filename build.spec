Name:           zopen-release
Version:        1.0
Release:        %(date "+%s")%{?dist}
Summary:        zopen repository and DNF configuration for /opt/pkg
License:        Apache-2.0
BuildArch:      noarch

Source0:        zopen.repo
Source1:        dnf.conf

%define         _prefix /opt/pkg
%define         _sysconfdir /opt/pkg/etc

%description
Provides repository definitions, DNF configurations, and creates the required 
filesystem directory tree under /opt/pkg.

%prep
# Nothing to compile

%build
# Nothing to build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/pkg/bin
mkdir -p %{buildroot}/opt/pkg/sbin
mkdir -p %{buildroot}/opt/pkg/lib
mkdir -p %{buildroot}/opt/pkg/share
mkdir -p %{buildroot}/opt/pkg/include
mkdir -p %{buildroot}/opt/pkg/etc/yum.repos.d
mkdir -p %{buildroot}/opt/pkg/etc/dnf/vars
mkdir -p %{buildroot}/opt/pkg/etc/rpm
mkdir -p %{buildroot}/opt/pkg/var/lib/rpm
mkdir -p %{buildroot}/opt/pkg/var/cache/libdnf5
mkdir -p %{buildroot}/opt/pkg/var/log

install -m 0644 %{SOURCE0} %{buildroot}/opt/pkg/etc/yum.repos.d/zopen.repo
install -m 0644 %{SOURCE1} %{buildroot}/opt/pkg/etc/dnf/dnf.conf

%files
%config(noreplace) /opt/pkg/etc/yum.repos.d/zopen.repo
%config(noreplace) /opt/pkg/etc/dnf/dnf.conf
%dir /opt/pkg
%dir /opt/pkg/bin
%dir /opt/pkg/sbin
%dir /opt/pkg/lib
%dir /opt/pkg/share
%dir /opt/pkg/include
%dir /opt/pkg/etc
%dir /opt/pkg/etc/yum.repos.d
%dir /opt/pkg/etc/dnf
%dir /opt/pkg/etc/dnf/vars
%dir /opt/pkg/etc/rpm
%dir /opt/pkg/var
%dir /opt/pkg/var/lib
%dir /opt/pkg/var/lib/rpm
%dir /opt/pkg/var/cache
%dir /opt/pkg/var/cache/libdnf5
%dir /opt/pkg/var/log

