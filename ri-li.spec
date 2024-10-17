%define	oname	Ri-li
%define	name	ri-li
%define	version	2.0.1
%define release	7
%define	Summary	a toy wood train kit game

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://surfnet.dl.sourceforge.net/sourceforge/ri-li/%{oname}-%{version}.tar.bz2
Patch0:		ri-li_makefile.in.patch
Patch1:		ri-li_makefile.am.patch
Patch2:		ri-li-2.0.1-gcc43.patch
License:	GPLv2 or GPLv3
Group:		Games/Arcade
URL:		https://www.ri-li.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dos2unix
Provides:	Ri-li
Obsoletes:	Ri-li

%description
You drive a toy wood engine in many levels and you must
collect all the coaches to win. Full-featured, 8 languages: Arabic,
Chinese, English, French, German, Japanese, Russian, Spanish.
Colorful animated wood engine, 40 levels in this first version and 3 beautiful
musics and many sound effects. 

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p0
dos2unix README COPYING AUTHORS NEWS COPYING.Music

%build
autoreconf
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}%{_gamesdatadir}/%{oname}/COPYING.Music


install -m644 data/Ri-li-icon-16x16.png -D %{buildroot}%{_miconsdir}/%{oname}.png
install -m644 data/Ri-li-icon-32x32.png -D %{buildroot}%{_iconsdir}/%{oname}.png
install -m644 data/Ri-li-icon-48x48.png -D %{buildroot}%{_liconsdir}/%{oname}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Ri-li
Comment=Ri-li arcade game
Exec=%{_gamesbindir}/Ri_li
Icon=%{_gamesdatadir}/%{oname}/%{oname}-icon-48x48.png
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%clean
rm -rf $%{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-, root, root)
%doc README COPYING AUTHORS NEWS COPYING.Music
%{_gamesbindir}/Ri_li
%{_gamesdatadir}/%{oname}/levels.dat
%{_gamesdatadir}/%{oname}/sprites.dat
%{_gamesdatadir}/%{oname}/Ri-li-icon-*.png
%{_gamesdatadir}/%{oname}/*.ico
%{_gamesdatadir}/%{oname}/Sounds/*
#%{_gamesdatadir}/%{oname}/*.ebuild
%{_gamesdatadir}/%{oname}/language.*
%{_iconsdir}/%{oname}*.png
%{_miconsdir}/%{oname}*.png
%{_liconsdir}/%{oname}*.png
%{_datadir}/applications/*





%changelog
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.0.1-6mdv2010.0
+ Revision: 442731
- rebuild

* Thu Oct 16 2008 Funda Wang <fundawang@mandriva.org> 2.0.1-5mdv2009.1
+ Revision: 294319
- add gcc 43 patch to get it built

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Mar 13 2008 Antoine Ginies <aginies@mandriva.com> 2.0.1-2mdv2008.1
+ Revision: 187467
- fix path to icon

* Mon Mar 10 2008 Antoine Ginies <aginies@mandriva.com> 2.0.1-1mdv2008.1
+ Revision: 183318
- remove gentto ebuild
- patch to remove gentoo
- new release
- release 2.0.1

  + Thierry Vignaud <tvignaud@mandriva.com>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jun 21 2007 Erwan Velu <erwan@mandriva.org> 2.0.0-2mdv2008.0
+ Revision: 42028
- Fixing description


* Thu Oct 26 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 2.0.0-1mdv2007.0
+ Revision: 72709
- New version 2.0.0
- import ri-li-1.2.0-2mdv2007.0

* Tue Aug 29 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2.0-2mdv2007.0
- fix summary macro used in menu
- fix categories in xdg menu
- fix wrong-file-end-of-line-encoding
- cosmetics

* Tue Aug 01 2006 Jerome Soyer <saispo@mandriva.org> 1.2.0-1mdv2007.0
- New release 1.2.0

* Thu Jul 13 2006 Lenny Cartier <lenny@mandriva.com> 1.0.3-1mdv2007.0
- add xdg menu
- move to gamesbindir and gamesdatadir

* Tue Jul 04 2006 Velu Erwan <erwan@seanodes.com> 1.0.2-1
- Initial rpm for mandriva
- Using ri-li package name to match Mandriva's naming policy

* Fri Jun 30 2006 Dominique Roux-Serret <roux-serret@ifrance.com> 1.0.2-1
- first RPM pakage.

