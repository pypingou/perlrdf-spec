Name:           perl-XML-CommonNS
Version:        0.06
Release:        1%{?dist}
Summary:        List of commonly used namespaces
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-CommonNS/
Source0:        http://www.cpan.org/modules/by-module/XML/XML-CommonNS-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version)
BuildRequires:  perl(XML::NamespaceFactory)
Requires:       perl(Test::More)
Requires:       perl(version)
Requires:       perl(XML::NamespaceFactory)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
All you need do to use this module is import the namespaces you

%prep
%setup -q -n XML-CommonNS-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon 0.06-1
- Specfile autogenerated by cpanspec 1.78.