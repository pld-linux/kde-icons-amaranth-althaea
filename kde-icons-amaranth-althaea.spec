
%define         _name	amaranth-althaea
%define		_ver	.4

Summary:	KDE icons - %{_name}
Summary(pl.UTF-8):	Motyw ikon do KDE - %{_name}
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
BuildArch:	noarch


%description
amaranth-althaea is a lighter version of Amaranth with more shadows.
This has a lower contrast and is softer on eyers.

%description -l pl.UTF-8
amaranth-althaea to lżejsza wersja wersja motywu Amaranth z dodaniem
cieni. Szczególny nacisk położono na niższy kontrast oraz
przystosowanie do długotrwałego oglądania.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xzf %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*
