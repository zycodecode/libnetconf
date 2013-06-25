Summary: toaster - callback module for libnetconf transapi
Name: toaster
Version: %(cut -f1 ./VERSION | tr -d '\n')
Release: 1
URL: http://www.liberouter.org/
Source: https://www.liberouter.org/repo/SOURCES/%{name}-%{version}-%{release}.tar.gz
Group: Liberouter
License: BSD
Vendor: CESNET, z.s.p.o.
Packager: @USERNAME@ <@USERMAIL@>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires: gcc make doxygen pkgconfig
BuildRequires: , libxml2-devel
Requires: , libnetconf, libxml2

%description
@Project name@ - Callbacks module providing function for reflectiong configuration changes.

%prep
%setup

%build
%configure
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%{_libdir}/toaster.so

