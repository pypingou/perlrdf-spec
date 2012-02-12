Name:           perl-RDF-Query
Version:        2.908
Release:        1%{?dist}
Summary:        SPARQL 1.1 Query implementation for use with RDF::Trine
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/RDF-Query/
Source0:        http://www.cpan.org/modules/by-module/RDF/RDF-Query-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Bloom::Filter) >= 1
BuildRequires:  perl(Crypt::GPG)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(DateTime::Format::W3CDTF)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Error)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Geo::Distance) >= 0.09
BuildRequires:  perl(Getopt::Simple)
BuildRequires:  perl(JSON) >= 2
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(RDF::Redland) >= 1
BuildRequires:  perl(RDF::Trine) >= 0.138
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Set::Scalar)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::JSON)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI) >= 1.52
BuildRequires:  perl(YAML)
Requires:       perl(Bloom::Filter) >= 1
Requires:       perl(Crypt::GPG)
Requires:       perl(Data::UUID)
Requires:       perl(DateTime::Format::W3CDTF)
Requires:       perl(Digest::SHA)
Requires:       perl(Error)
Requires:       perl(File::Spec)
Requires:       perl(Geo::Distance) >= 0.09
Requires:       perl(Getopt::Simple)
Requires:       perl(JSON) >= 2
Requires:       perl(LWP::Simple)
Requires:       perl(Module::Pluggable)
Requires:       perl(Parse::RecDescent)
Requires:       perl(RDF::Redland) >= 1
Requires:       perl(RDF::Trine) >= 0.138
Requires:       perl(Scalar::Util)
Requires:       perl(Set::Scalar)
Requires:       perl(URI) >= 1.52
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
RDF::Query allows SPARQL and RDQL queries to be run against an RDF model,
returning rows of matching results.

%prep
%setup -q -n RDF-Query-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes.ttl doap.rdf README README.html
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/rqsh

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon 2.908-1
- Specfile autogenerated by cpanspec 1.78.
