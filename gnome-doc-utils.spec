%if %mdkversion >= 200600
%define pkgconfigdir %_datadir/pkgconfig
%else
%define pkgconfigdir %_libdir/pkgconfig
%endif
Summary: 		GNOME XML documentation utilities 
Name: 			gnome-doc-utils
Version: 		0.11.1
Release: 		%mkrel 1
Source0: 		http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
# (fc) 0.8.0-1mdv use catalog for dtd validation
Patch0:			gnome-doc-utils-0.8.0-catalog.patch
License: 		LGPL
Group: 			Publishing
Url: 			http://www.gnome.org
BuildRequires: 		libxslt-devel
BuildRequires: 		libxslt-proc
BuildRequires: 		glib-gettextize
BuildRequires: 		scrollkeeper
BuildRequires: 		intltool
Requires:		libxslt-proc
Requires:		libxml2-utils
Requires: 		python-libxml2
Requires(post): 	scrollkeeper
Requires(postun): 	scrollkeeper
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
touch *
cd tools
%patch0 -p1 -b .catalog
cd ..
#needed by patch0
aclocal -I tools
autoconf
automake -a -c

%build

./configure --prefix=%_prefix --mandir=%_mandir --disable-scrollkeeper

%make

%check
#broken ATM
make check

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std pkgconfigdir=%pkgconfigdir
%find_lang gnome-doc-make --with-gnome
%find_lang gnome-doc-xslt --with-gnome
%find_lang %name
cat gnome-doc-xslt.lang gnome-doc-make.lang >> %name.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_scrollkeeper

%postun
%clean_scrollkeeper


%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%_bindir/*
%pkgconfigdir/*.pc
%_datadir/aclocal/*.m4
%_datadir/gnome-doc-utils/
%dir %_datadir/omf/gnome-doc-make/
%_datadir/omf/gnome-doc-make/gnome-doc-make-C.omf
%dir %_datadir/omf/gnome-doc-xslt/
%_datadir/omf/gnome-doc-xslt/gnome-doc-xslt-C.omf
%dir %_datadir/xml/
%_datadir/xml/gnome
%_datadir/xml2po/
%_mandir/man1/xml2po.1*
