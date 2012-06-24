%include	/usr/lib/rpm/macros.perl
%define	pdir	Regexp
%define	pnam	Match-Any
Summary:	Regexp::Match::Any Perl module - match many regexes against a variable
Summary(pl):	Modu� Perla Regexp::Match::Any - dopasowanie wielu wyra�e� regularnych do zmiennej
Name:		perl-Regexp-Match-Any
Version:	0.03
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}_%{version}.tar.gz
# Source0-md5:	f9baccc05916ac0a0c1cf1853579311a
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to pass the match_any() function a reference to
an array of regexes which will then return a full regex for the the
variable to be matched against. Note: this module may be very handy
for use with Mail::Audit.

%description -l pl
Ten podu� pozwala na przekazanie funkcji match_any() odwo�ania do
tablicy wyra�e� regularnych, na podstawie kt�rych funkcja zwraca pe�ne
wyra�enie regularne dla zmiennej, kt�ra mia�a by� dopasowana. Ten
modu� mo�e by� przydatny szczeg�lnie do u�ywania z Mail::Audit.

%prep
%setup -q -n %{pnam}_%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme
%{perl_vendorlib}/Regexp/Match
%{_mandir}/man3/*
