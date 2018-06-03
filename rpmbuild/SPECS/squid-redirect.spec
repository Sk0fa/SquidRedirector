%define _unpackaged_files_terminate_build 0
Name:		squid-redirect
Version:	1.0.0
Release:	1
Summary:	Tool for squid that redirect incoming requests

License:	GPL
URL:		http://github.com/TAB0R
Source0:	squid-redirect-1.0.0.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

Requires:	logrotate
Requires:	rsyslog	

%description
Tool for squid that redirect incoming requests.
You shuld add this line in /etc/squid/squid.conf:
url_rewrite_program /path/to/python3 /etc/squid-redirect/squid_redirector.py

%prep
%setup -q

%install
mkdir -p "$RPM_BUILD_ROOT"
cp -R * "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root,-)
/etc/squid-redirect/squid_redirector.py
%config(noreplace) /etc/squid-redirect/squid_redirector.json
/etc/rsyslog.d/squid-redirector.conf
/etc/logrotate.d/squid-redirector

%clean
rm -rf $RPM_BUILD_ROOT
