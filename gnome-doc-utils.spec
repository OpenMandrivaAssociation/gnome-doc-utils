%define pkgconfigdir %_datadir/pkgconfig
Summary: 		GNOME XML documentation utilities 
Name: 			gnome-doc-utils
Version: 		0.20.9
Release: 		%mkrel 1
Source0: 		http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.xz
# (fc) 0.8.0-1mdv use catalog for dtd validation (GNOME bug #497055)
Patch0:			gnome-doc-utils-0.12.1-catalog.patch
License: 		LGPLv2+ and GPLv2+
Group: 			Publishing
Url: 			http://www.gnome.org
BuildRequires: 		libxslt-devel
BuildRequires: 		libxslt-proc
BuildRequires: 		python-libxml2
BuildRequires: 		glib-gettextize
BuildRequires: 		scrollkeeper
BuildRequires:		docbook-dtd44-xml
BuildRequires: 		intltool
Requires:		libxslt-proc
Requires:		libxml2-utils
Requires: 		python-libxml2
Requires:		docbook-dtd44-xml docbook-dtd412-xml
BuildRoot: 		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 		noarch
%define _requires_exceptions pkgconfig.libxml-2.0

%description
gnome-doc-utils is a collection of documentation utilities for the Gnome
project.  Notably, it contains utilities for building documentation and
all auxiliary files in your source tree, and it contains the DocBook
XSLT stylesheets that were once distributed with Yelp.

%prep
%setup -q
%patch0 -p1 -b .catalog
intltoolize --force
#needed by patch0
aclocal -I tools -I m4
autoconf
automake -a -c

%build

./configure --prefix=%_prefix --mandir=%_mandir --disable-scrollkeeper

#gw parallel make broken in 0.17.4
make

%check
#broken ATM
make check

%install
rm -rf %{buildroot} *.lang
%makeinstall_std pkgconfigdir=%pkgconfigdir
%find_lang gnome-doc-make --with-gnome
#%find_lang gnome-doc-mallard-spec --with-gnome
%find_lang gnome-doc-xslt --with-gnome
%find_lang %name
cat gnome-doc-xslt.lang gnome-doc-make.lang >> %name.lang

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%_bindir/*
%pkgconfigdir/*.pc
%_datadir/aclocal/*.m4
%_datadir/gnome-doc-utils/
%dir %_datadir/xml/
%_datadir/xml/gnome
%_mandir/man1/xml2po.1*
%py_puresitedir/xml2po/
