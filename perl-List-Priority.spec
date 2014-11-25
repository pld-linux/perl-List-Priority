#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	List
%define		pnam	Priority
%include	/usr/lib/rpm/macros.perl
Summary:	List::Priority - a list that manipulates objects by their priority
Summary(pl.UTF-8):	List::Priority - manipulowanie elementami listy zgodnie z ich priorytetem
Name:		perl-List-Priority
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	10ecdf78556486c232af3f02c6e6c085
URL:		http://search.cpan.org/dist/List-Priority/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you want to handle multiple data bits by their order of importance
- this one's for you.

%description -l pl.UTF-8
Jeśli chcesz obsługiwać wiele kawałków danych w porządku ich ważności
- ten moduł jest dla Ciebie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
