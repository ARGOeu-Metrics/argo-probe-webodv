%global __python ${python3}
%define underscore() %(echo %1 | sed 's/-/_/g')

Summary:       ARGO probe that sends a POST request to webODV and checks that it is successful
Name:          argo-probe-webodv
Version:       0.1.1
Release:       2%{?dist}
Source0:       %{name}-%{version}.tar.gz
License:       ASL 2.0
Group:         Development/System
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:        %{_prefix}
BuildArch:     noarch

BuildRequires: python3-devel
Requires: python36-requests

%description
ARGO probe that sends a POST request to webODV and checks that it is successful

%prep
%setup -q

%build
%{py3_build}

%install
%{py3_install "--record=INSTALLED_FILES" }

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%dir %{python3_sitelib}/%{underscore %{name}}/
%{python3_sitelib}/%{underscore %{name}}/*.py
%{_libexecdir}/argo/probes/webodv/*.py

%changelog
* Thu Jan 14 2023 Katarina Zailac <kzailac@srce.hr> - 0.1.1-2
- Added comments in code
* Wed Dec 14 2022 Katarina Zailac <kzailac@srce.hr> - 0.1.1-1
- ARGO-4138 Include log file for webODV probe
* Thu Oct 27 2022 Katarina Zailac <kzailac@srce.hr> - 0.1.0-1
- ARGO-4045 Create webODV probe
