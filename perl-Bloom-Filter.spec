Name:           perl-Bloom-Filter
Version:        1.0
Release:        1%{?dist}
Summary:        Sample Perl Bloom filter implementation
License:        CHECK(GPL+ or Artistic)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Bloom-Filter/
Source0:        http://www.cpan.org/modules/by-module/Bloom/Bloom-Filter-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A Bloom filter is a probabilistic algorithm for doing existence tests in
less memory than a full list of keys would require. The tradeoff to using
Bloom filters is a certain configurable risk of false positives. This
module implements a simple Bloom filter with configurable capacity and
false positive rate. Bloom filters were first described in a 1970 paper by
Burton Bloom, see
http://portal.acm.org/citation.cfm?id=362692&dl=ACM&coll=portal.

%prep
%setup -q -n Bloom-Filter-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

#%check
#make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon 1.0-1
- Specfile autogenerated by cpanspec 1.78.
