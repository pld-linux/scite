Summary:	-
Summary(pl):	-
Name:		scite
Version:	1.53
Release:	1
License:	BSD-like
Group:		X11/Applications
Source0:	http://scintilla.org/scite153.tgz
# Source0-md5:	156275ae6318c323b308f403033663cd
URL:		http://scintilla.org/SciTE.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -c

%build
%{__make} -C scite/gtk

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
