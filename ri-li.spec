%define	oname	Ri-li
%define	name	ri-li
%define	version	2.0.1
%define	release	%mkrel 1
%define	Summary	a toy wood train kit game

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://surfnet.dl.sourceforge.net/sourceforge/ri-li/%{oname}-%{version}.tar.bz2
License:	GPL
Group:		Games/Arcade
URL:		http://www.ri-li.org
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
dos2unix README COPYING AUTHORS NEWS COPYING.Music

%build
%configure	--bindir=%{_gamesbindir} \
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
Icon=%{oname} 
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%clean
rm -rf $%{buildroot}

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-, root, root)
%doc README COPYING AUTHORS NEWS COPYING.Music
%{_gamesbindir}/Ri_li
%{_gamesdatadir}/%{oname}/levels.dat
%{_gamesdatadir}/%{oname}/sprites.dat
%{_gamesdatadir}/%{oname}/Ri-li-icon-*.png
%{_gamesdatadir}/%{oname}/*.ico
%{_gamesdatadir}/%{oname}/Sounds/*
%{_gamesdatadir}/%{oname}/*.ebuild
%{_gamesdatadir}/%{oname}/language.*
%{_iconsdir}/%{oname}*.png
%{_miconsdir}/%{oname}*.png
%{_liconsdir}/%{oname}*.png
%{_datadir}/applications/*



