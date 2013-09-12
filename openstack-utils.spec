%global rel 8

Name:           openstack-utils
Version:        2013.1
Release:        %{rel}%{?dist}.1
Summary:        Helper utilities for OpenStack services
URL:            https://github.com/redhat-openstack/openstack-utils
Source0:        https://github.com/redhat-openstack/%{name}/archive/%{version}-%{rel}.tar.gz#/%{name}-%{version}-%{rel}.tar.gz
License:        ASL 2.0
BuildArch:      noarch

Requires:       crudini

%description
Utilities to aid the setup and configuration of OpenStack packages.

%prep
%setup -q -n %{name}-%{version}-%{rel}

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
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.1-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 24 2013 Pádraig Brady <P@draigBrady.com> 2013.1-8
- Display quantum services correctly

* Wed Apr 24 2013 Pádraig Brady <P@draigBrady.com> 2013.1-7
- Fix detection of nova installation in openstack-status

* Tue Apr  9 2013 Pádraig Brady <P@draigBrady.com> 2013.1-6
- Grizzly keystone sample credentials adjustments
- Support systems with SELinux disabled
- Improve handling of users in openstack-db --drop
- Fix handling of cgroup service
- Fix handling of passwords with mariadb

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec  7 2012 Pádraig Brady <P@draigBrady.com> 2013.1-1
- Support grizzly installs
- Install novnc
- Fix setup issues on RHEL based systems

* Thu Nov 22 2012 Pádraig Brady <P@draigBrady.com> 2012.2-7
- Fix Essex installs

* Thu Nov 08 2012 Alan Pevec <apevec@redhat.com> 2012.2-6
- Disable Quantum rhbz#873823

* Wed Oct 10 2012 Pádraig Brady <P@draigBrady.com> 2012.2-5
- Update from upstream to support folsom packages

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.1-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Pádraig Brady <P@draigBrady.com> 2012.1-2
- Improve validation done by openstack-config and openstack-db
- Fix openstack-demo-install

* Mon May 21 2012 Alan Pevec <apevec@redhat.com> 2012.1-1.1
- add missing dependency for openstack-config

* Wed Apr 11 2012 Pádraig Brady <P@draigBrady.com> 2012.1-1
- Initial release supporting the Essex OpenStack release
