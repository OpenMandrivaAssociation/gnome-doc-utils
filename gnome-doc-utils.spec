%define pkgconfigdir %{_datadir}/pkgconfig

Summary:	GNOME XML documentation utilities 
Name:		gnome-doc-utils
Version:	0.20.10
Release:	9
License:	LGPLv2+ and GPLv2+
Group:		Publishing
Url:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
# (fc) 0.8.0-1mdv use catalog for dtd validation (GNOME bug #497055)
Patch0:		gnome-doc-utils-0.12.1-catalog.patch
BuildArch:	noarch

BuildRequires:	docbook-dtd44-xml
BuildRequires:	glib-gettextize
BuildRequires:	intltool
BuildRequires:	python-libxml2
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(libxslt)

Requires:	xsltproc

%description
gnome-doc-utils is a collection of documentation utilities for the Gnome
project.  Notably, it contains utilities for building documentation and
all auxiliary files in your source tree, and it contains the DocBook
XSLT stylesheets that were once distributed with Yelp.

%package -n xml2po
Summary:	Tool to extract translatable content from XML documents
Requires:	python-libxml2

%description -n xml2po
xml2po is a simple Python program which extracts translatable
content from free-form XML documents and outputs gettext compatible
POT files.

%package devel
Summary:	A Collection of Documentation Utilities for GNOME
Group:		Development/GNOME and GTK+ 
Requires:	%{name} = %{version}
Requires:	docbook-dtd44-xml
Requires:	docbook-dtd412-xml
Requires:	libxml2-utils
Requires:	xml2po

%description devel
This package contains the development files for %{name}.

%prep
%setup -q
%apply_patches

intltoolize --force
#needed by patch0
aclocal -I tools -I m4
autoconf
automake -a -c

%build
%configure2_5x \
	--build=%{_build} \
	--disable-scrollkeeper \
	--enable-documentation

%make

%check
%make check

%install
%makeinstall_std pkgconfigdir=%{pkgconfigdir}
%find_lang gnome-doc-make --with-gnome
%find_lang gnome-doc-xslt --with-gnome
%find_lang %{name}
cat gnome-doc-xslt.lang gnome-doc-make.lang >> %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%{_bindir}/gnome-doc-tool
%dir %{_datadir}/gnome-doc-utils
%{_datadir}/gnome-doc-utils/icons
%{_datadir}/gnome-doc-utils/watermarks
%dir %{_datadir}/xml/
%{_datadir}/xml/gnome
%{_datadir}/xml/mallard

%files -n xml2po
%doc xml2po/AUTHORS xml2po/ChangeLog xml2po/COPYING xml2po/NEWS xml2po/README
%{_bindir}/xml2po
%{py_puresitedir}/xml2po/
%{_mandir}/man1/xml2po.1*

%files devel
%{_bindir}/gnome-doc-prepare
%{pkgconfigdir}/*.pc
%{_datadir}/aclocal/*.m4
%{_datadir}/gnome-doc-utils/gnome-doc-utils.make
%{_datadir}/gnome-doc-utils/templates
%{_datadir}/gnome-doc-utils/template*.*

