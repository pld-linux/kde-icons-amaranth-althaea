#$Revision: 1.2 $, $Date: 2004-04-16 21:24:20 $

%define         _name	amaranth-althaea
%define		_ver	.4

Summary:	KDE icons - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	0%{_ver}
Release:	1
License:	GPL
Group:		Themes
Source0:	http://download.freshmeat.net/themes/amaranth/%{_name}-%{_ver}.tar.gz
# Source0-md5:	d2394689c9aa911d7b7b4d5d11a87cd2
URL:		http://www.kde-look.org/content/show.php?content=9781
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
amaranth-althaea is a lighter version of Amaranth with more shadows.
This has a lower contrast and is softer on eyers.

%description -l pl
amaranth-althaea to l¿ejsza wersja wersja motywu Amaranth z dodaniem
cieni. Szczególny nacisk po³o¿ono na ni¿szy kontrast oraz
przystosowanie do d³ugotrwa³ego ogl±dania.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xjf %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*
