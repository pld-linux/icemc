Summary:	Graphical menu configuration utility for icewm
Summary(pl):	Graficzne narzêdzie do edycji menu dla icewm'a
Name:		icemc
Version:	0.2.2
Release:	1
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://www.algorithm.at/comp/icemc/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}_16x16.xpm
Source4:	%{name}_32x32.xpm
Patch0:		%{name}-Makefile.patch
Patch1:		http://www.algorithm.at/comp/icemc/%{name}-%{version}.patch.tar.gz
URL:		http://www.algorithm.at/comp/icemc/icemc.html
BuildRequires:	qt-devel
Requires:	icewm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6/

%description
Graphical menu edition utility for icewm. It uses qt-library.

%description -l pl
Graficzne narzêdzie do edycji menu w icewm. Wymaga bybliotek qt w
systemie.

%prep
%setup -q 
%patch0 -p1
tar zxf %{PATCH1}; patch -p1 <%{name}-%{version}.patch/patch.%{name}-%{version}

%build
%{__make} CXXFLAGS="%{rpmcflags} -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/Settings/IceWM} \
	$RPM_BUILD_ROOT{%{_libdir}/X11/icewm/icons,%{_pixmapsdir}}

install icemc $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings/IceWM
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} %{SOURCE4} $RPM_BUILD_ROOT%{_libdir}/X11/icewm/icons

gzip -9nf CHANGELOG.txt README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Settings/IceWM/*
%{_libdir}/X11/icewm/icons/*
%{_pixmapsdir}/*
