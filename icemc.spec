Summary:	Graphical menu configuration utility for IceWM
Summary(pl):	Graficzne narzêdzie do edycji menu dla IceWM-a
Name:		icemc
Version:	0.2.2
Release:	3
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://www.algorithm.at/comp/icemc/%{name}-%{version}.tar.gz
# Source0-md5:	6ba3d647139f7574fa83aaa1b36b5e56
Source1:	%{name}.desktop
Source2:	%{name}.png
Source3:	%{name}_16x16.xpm
Source4:	%{name}_32x32.xpm
Source5:	http://www.algorithm.at/comp/icemc/%{name}-%{version}.patch.tar.gz
# Source5-md5:	ff938b1156a11960ccceb73d49f10a04
Patch0:		%{name}-Makefile.patch
URL:		http://www.algorithm.at/comp/icemc/icemc.html
BuildRequires:	qt-devel >= 3.0.5
Requires:	icewm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	iceMC


%description
Graphical menu edition utility for IceWM. It uses qt-library.

%description -l pl
Graficzne narzêdzie do edycji menu w IceWM. U¿ywa biblioteki qt.

%prep
%setup -q 
%patch0 -p1
tar zxf %{SOURCE5}; patch -p1 <%{name}-%{version}.patch/patch.%{name}-%{version}

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt README
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Settings/IceWM/*
%{_libdir}/X11/icewm/icons/*
%{_pixmapsdir}/*
