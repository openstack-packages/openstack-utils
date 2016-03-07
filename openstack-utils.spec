%global rel 1
%milestone -%{rel}

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           openstack-utils
Version:        XXX
Release:        XXX
Summary:        Helper utilities for OpenStack services
URL:            https://github.com/redhat-openstack/openstack-utils
Source0:        https://github.com/redhat-openstack/%{name}/archive/master.tar.gz#/%{name}-master.tar.gz
License:        ASL 2.0
BuildArch:      noarch

Requires:       crudini
Requires:       curl

%description
Utilities to aid the setup and configuration of OpenStack packages.

%prep
%setup -q -n %{name}-%{upstream_version}

%build

%install
mkdir -p %{buildroot}%{_bindir}/
install -p -m 755 -t %{buildroot}%{_bindir}/ utils/*
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m 644 man/*.1 %{buildroot}%{_mandir}/man1/

%files
%doc LICENSE NEWS
%{_bindir}/*
%{_mandir}/man1/*.1.gz

%changelog
