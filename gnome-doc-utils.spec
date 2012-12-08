%define pkgconfigdir %{_datadir}/pkgconfig

Summary:	GNOME XML documentation utilities 
Name:		gnome-doc-utils
Version:	0.20.10
Release:	4
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



%changelog
* Fri May 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.20.10-4
+ Revision: 798169
- moved reqs to devel package

* Thu May 10 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.20.10-3
+ Revision: 798128
- rebuild
- split out devel and xml2po pkgs
- python-libxml2 is no longer pulled in by the main pkg

* Mon Apr 23 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.20.10-2
+ Revision: 793050
- rebuild
- cleaned up spec

* Tue Mar 27 2012 Götz Waschk <waschk@mandriva.org> 0.20.10-1
+ Revision: 787409
- new version

* Tue Mar 20 2012 Götz Waschk <waschk@mandriva.org> 0.20.9-1
+ Revision: 785819
- update file list
- update to new version 0.20.9

* Mon Mar 19 2012 Götz Waschk <waschk@mandriva.org> 0.20.8-1
+ Revision: 785491
- new version
- remove scrollkeeper macros

* Sat Mar 03 2012 Götz Waschk <waschk@mandriva.org> 0.20.7-1
+ Revision: 782006
- update file list
- new version
- xz tarball

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 0.20.6-1
+ Revision: 659091
- update to new version 0.20.6

* Tue Mar 22 2011 Götz Waschk <waschk@mandriva.org> 0.20.5-1
+ Revision: 647617
- update to new version 0.20.5

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.20.4-3
+ Revision: 640334
- rebuild to obsolete old packages

* Mon Jan 10 2011 Götz Waschk <waschk@mandriva.org> 0.20.4-1
+ Revision: 630885
- new version

* Mon Dec 20 2010 Götz Waschk <waschk@mandriva.org> 0.20.3-1mdv2011.0
+ Revision: 623330
- update to new version 0.20.3

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.20.2-5mdv2011.0
+ Revision: 591926
- python-devel isn't a BR now that the python Makefile has been moved to the
  python main package

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.20.2-4mdv2011.0
+ Revision: 591270
- rebuild

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.20.2-3mdv2011.0
+ Revision: 590928
- xml2po requires python's Makefile to run

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.20.2-2mdv2011.0
+ Revision: 590734
- rebuild for py2.7
- BR python devel

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 0.20.2-1mdv2011.0
+ Revision: 581803
- update to new version 0.20.2

* Mon Apr 26 2010 Götz Waschk <waschk@mandriva.org> 0.20.1-1mdv2010.1
+ Revision: 539205
- update to new version 0.20.1

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 528901
- update to new version 0.20.0

* Mon Feb 22 2010 Götz Waschk <waschk@mandriva.org> 0.19.5-1mdv2010.1
+ Revision: 509415
- update to new version 0.19.5

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 0.19.4-1mdv2010.1
+ Revision: 502719
- update to new version 0.19.4

* Tue Jan 26 2010 Götz Waschk <waschk@mandriva.org> 0.19.3-1mdv2010.1
+ Revision: 496504
- update to new version 0.19.3

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 0.19.2-1mdv2010.1
+ Revision: 489965
- update to new version 0.19.2

* Wed Jan 06 2010 Götz Waschk <waschk@mandriva.org> 0.19.1-1mdv2010.1
+ Revision: 486562
- update to new version 0.19.1

* Sat Nov 21 2009 Götz Waschk <waschk@mandriva.org> 0.18.1-1mdv2010.1
+ Revision: 467788
- update to new version 0.18.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 0.18.0-1mdv2010.0
+ Revision: 446698
- update to new version 0.18.0

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 0.17.5-1mdv2010.0
+ Revision: 437419
- update to new version 0.17.5

* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 0.17.4-1mdv2010.0
+ Revision: 420778
- disable parallel build
- update to new version 0.17.4

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 0.17.3-1mdv2010.0
+ Revision: 401407
- update to new version 0.17.3

* Sun Jun 28 2009 Götz Waschk <waschk@mandriva.org> 0.17.2-1mdv2010.0
+ Revision: 390427
- update build deps
- new version
- update file list

* Mon Jun 15 2009 Götz Waschk <waschk@mandriva.org> 0.17.1-1mdv2010.0
+ Revision: 385964
- update to new version 0.17.1

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 0.16.1-1mdv2009.1
+ Revision: 367218
- update to new version 0.16.1

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 0.16.0-1mdv2009.1
+ Revision: 356129
- update to new version 0.16.0

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 0.15.2-1mdv2009.1
+ Revision: 346878
- update to new version 0.15.2

* Mon Feb 02 2009 Götz Waschk <waschk@mandriva.org> 0.15.1-1mdv2009.1
+ Revision: 336344
- update to new version 0.15.1

* Sat Jan 10 2009 Götz Waschk <waschk@mandriva.org> 0.14.2-1mdv2009.1
+ Revision: 327957
- update to new version 0.14.2

* Thu Dec 18 2008 Götz Waschk <waschk@mandriva.org> 0.14.1-1mdv2009.1
+ Revision: 315788
- update to new version 0.14.1

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 0.14.0-1mdv2009.0
+ Revision: 287253
- new version
- update license

* Thu Aug 28 2008 Götz Waschk <waschk@mandriva.org> 0.13.1-1mdv2009.0
+ Revision: 276871
- new version
- fix build

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.12.2-2mdv2009.0
+ Revision: 221086
- rebuild

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 0.12.2-1mdv2008.1
+ Revision: 183223
- new version

* Tue Feb 12 2008 Götz Waschk <waschk@mandriva.org> 0.12.1-1mdv2008.1
+ Revision: 166379
- new version
- rediff the patch

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.12.0-2mdv2008.1
+ Revision: 150139
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 0.12.0-1mdv2008.0
+ Revision: 89360
- new version

* Sun Aug 19 2007 Götz Waschk <waschk@mandriva.org> 0.11.2-1mdv2008.0
+ Revision: 67038
- new version
- fix build

* Wed Aug 01 2007 Götz Waschk <waschk@mandriva.org> 0.11.1-2mdv2008.0
+ Revision: 57362
- depend on docbook DTDs

* Mon Jul 30 2007 Götz Waschk <waschk@mandriva.org> 0.11.1-1mdv2008.0
+ Revision: 56702
- fix buildrequires
- new version
- fix aclocal call

* Tue Apr 17 2007 Götz Waschk <waschk@mandriva.org> 0.10.3-1mdv2008.0
+ Revision: 14134
- new version


* Thu Mar 15 2007 Götz Waschk <waschk@mandriva.org> 0.10.1-2mdv2007.1
+ Revision: 144422
- fix deps

* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdv2007.1
+ Revision: 142119
- new version

* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 0.10.0-1mdv2007.1
+ Revision: 142087
- fix build
- new version

* Mon Jan 29 2007 Götz Waschk <waschk@mandriva.org> 0.9.2-1mdv2007.1
+ Revision: 115208
- new version

* Fri Jan 26 2007 Götz Waschk <waschk@mandriva.org> 0.9.1-1mdv2007.1
+ Revision: 114007
- Import gnome-doc-utils

* Fri Jan 26 2007 G�tz Waschk <waschk@mandriva.org> 0.9.1-1mdv2007.1
- fix build
- unpack patch 
- new version

* Fri Sep 08 2006 G�tz Waschk <waschk@mandriva.org> 0.8.0-2mdv2007.0
- fix buildrequires
- fix build

* Wed Sep 06 2006 Götz Waschk <waschk@mandriva.org> 0.8.0-1mdv2007.0
- New release 0.8.0
- Patch0: use catalog for DTD validation (fcrozat)
- disable make check for now

* Wed Aug 09 2006 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdv2007.0
- New release 0.7.2

* Tue Jun 13 2006 Götz Waschk <waschk@mandriva.org> 0.7.1-1mdv2007.0
- New release 0.7.1

* Thu Apr 13 2006 Frederic Crozat <fcrozat@mandriva.com> 0.6.0-1mdk
- Release 0.6.0

* Wed Feb 22 2006 Eskild Hustvedt <eskild@mandriva.org> 0.4.4-3mdk
- Drop old text from the description

* Wed Feb 22 2006 Frederic Crozat <fcrozat@mandriva.com> 0.4.4-2mdk
- Use mkrel

* Mon Nov 28 2005 Götz Waschk <waschk@mandriva.org> 0.4.4-1mdk
- New release 0.4.4

* Thu Oct 13 2005 G�tz Waschk <waschk@mandriva.org> 0.4.3-1mdk
- drop patch
- New release 0.4.3

* Thu Oct 06 2005 Frederic Crozat <fcrozat@mandriva.com> 0.4.2-2mdk
- Patch0: fix scrollkeeper-update when using DESTDIR

* Thu Oct 06 2005 Frederic Crozat <fcrozat@mandriva.com> 0.4.2-1mdk
- Release 0.4.2
- remove patch0 (merged upstream)

* Sun Aug 28 2005 G�tz Waschk <waschk@mandriva.org> 0.2.1-2mdk
- replace prereq
- encoding fix

* Wed Jul 13 2005 G�tz Waschk <waschk@mandriva.org> 0.2.1-1mdk
- New release 0.2.1

* Fri Apr 29 2005 G�tz Waschk <waschk@mandriva.org> 0.2.0-2mdk
- fix pkgconfig file location

* Tue Apr 05 2005 Götz Waschk <waschk@linux-mandrake.com> 0.2.0-1mdk
- New release 0.2.0

* Mon Mar 07 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.1.3-1mdk
- update file list
- New release 0.1.3

* Fri Jan 14 2005 Goetz Waschk <waschk@linux-mandrake.com> 0.1.2-1mdk
- New release 0.1.2

* Mon Jan 03 2005 Goetz Waschk <waschk@linux-mandrake.com> 0.1.1-1mdk
- New release 0.1.1

* Wed Nov 03 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.1-3mdk
- buildrequires fix

* Mon Nov 01 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.1-2mdk
- add scrollkeeper scripts
- fix deps

* Mon Nov 01 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.1-1mdk
- initial package

