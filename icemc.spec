Summary:	Graphical menu configuration utility for IceWM
Summary(pl.UTF-8):   Graficzne narzędzie do edycji menu dla IceWM-a
Name:		icemc
Version:	0.2.4
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://www.algorithm.at/comp/icemc/%{name}-%{version}.tar.gz
# Source0-md5:	1df8dd3c4e485db980a3f1b63d6f28bb
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}_16x16.xpm
Source4:	%{name}_32x32.xpm
Patch0:		%{name}-gcc3.patch
URL:		http://www.algorithm.at/comp/icemc/icemc.html
BuildRequires:	qt-devel >= 3.0.5
Requires:	icewm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	iceMC

%description
Graphical menu edition utility for IceWM. It uses Qt-library.

%description -l pl.UTF-8
Graficzne narzędzie do edycji menu w IceWM. Używa biblioteki Qt.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} -fno-exceptions -I/usr/include/qt %{!?debug:-DNO_DEBUG}" \
	QTDIR="/usr" \
	LIBS="-lqt-mt"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}} \
	$RPM_BUILD_ROOT{%{_datadir}/icewm/icons,%{_pixmapsdir}}

install icemc $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/icewm/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/icewm/icons/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
