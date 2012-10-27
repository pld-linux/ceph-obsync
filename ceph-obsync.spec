Summary:	Synchronize bucket data between object storage APIs like S3, Swift
Summary(pl.UTF-8):	Synchronizacja danych między API przechowywania obiektów, takimi jak S3 czy Swift
Name:		ceph-obsync
Version:	0.53
%define	snap	20120927
Release:	0.%{snap}.1
License:	LGPL v2.1
Group:		Applications/Networking
# git clone git://github.com/ceph/obsync.git
Source0:	obsync.tar.xz
# Source0-md5:	601e3528539f7d23e77aa4316d012c64
URL:		http://ceph.newdream.net/
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	python
Requires:	python-boto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
obsync is a tool to synchronize objects between cloud object storage
providers, such as Amazon S3 (or compatible services), a Ceph RADOS
cluster, or a local directory.

%description -l pl.UTF-8
obsync to narzędzie do synchronizacji obiektów między systemami
przechowującymi obiekty w chmurze, takimi jak Amazon S3 (lub serwisy
kompatybilne) a klastrem Ceph RADOS lub katalogiem lokalnym.

%prep
%setup -q -n obsync

%{__sed} -i -e '1s,/usr/bin/env python,/usr/bin/python,' obsync

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install boto_tool obsync $RPM_BUILD_ROOT%{_bindir}
install boto_del.py $RPM_BUILD_ROOT%{_bindir}/boto_del
cp -p obsync.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/boto_del
%attr(755,root,root) %{_bindir}/boto_tool
%attr(755,root,root) %{_bindir}/obsync
%{_mandir}/man1/obsync.1*
