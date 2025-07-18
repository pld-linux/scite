Summary:	SciTE - a programmers text editor
Summary(pl.UTF-8):	SciTE - edytor tekstu dla programistów
Name:		scite
Version:	3.7.5
Release:	1
License:	BSD-like
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/scintilla/scite%(echo %{version} | tr -d .).tgz
# Source0-md5:	41c63550857e489166991f44f0cd0efe
Patch0:		%{name}-make.patch
Patch1:		%{name}-desktop.patch
URL:		http://scintilla.org/SciTE.html
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	libstdc++-devel >= 6:4.8
BuildRequires:	lua51-devel
BuildRequires:	pkgconfig
BuildRequires:	scintilla-devel >= %{version}
Requires:	scintilla >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SciTE is a graphical GTK+ based editor. It has support for indenting,
highlighting, and shortcuts in a myriad of languages and can be
extended by editing object-oriented configuration files. Support is
included for Java, C, C++, C#, Shell, Apache.

%description -l pl.UTF-8
SciTE to graficzny edytor oparty o GTK+. Obsługuje wcięcia,
podświetlanie składni oraz skróty klawiszowe dla wielu języków,
ponadto może być rozszerzany poprzez edycję zorientowanych obiektowo
plików konfiguracyjnych. Zawiera wsparcie dla Javy, C, C++, C#,
powłoki uniksowej i Apache'a.

%prep
%setup -q -c
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} -C scite/gtk \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcflags}" \
	%{?debug:DEBUG=1} \
	GTK3=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C scite/gtk install \
	DESTDIR=$RPM_BUILD_ROOT \
	datadir=%{_datadir} \
	pixmapdir=%{_pixmapsdir}

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install scite/doc/scite.1 $RPM_BUILD_ROOT%{_mandir}/man1/SciTE.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc scite/License.txt scite/doc/*.{html,jpg,png}
%attr(755,root,root) %{_bindir}/SciTE
%{_datadir}/scite
%{_mandir}/man1/SciTE.1*
%{_desktopdir}/SciTE.desktop
%{_pixmapsdir}/Sci48M.png
