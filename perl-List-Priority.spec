%include	/usr/lib/rpm/macros.perl
%define		pdir	List
%define		pnam	Priority
Summary:	List::Priority - A list that manipulates objects by their priority
Summary(pl):	List::Priority - manipulowanie elementami listy zgodnie z ich priorytetem
Name:		perl-List-Priority
Version:	0.02
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you want to handle multiple data bits by their order of importance
- this one's for you.

%description -l pl
Je¶li chcesz obs³ugiwaæ wiele kawa³ków danych w porz±dku ich wa¿no¶ci
- ten modu³ jest dla Ciebie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
