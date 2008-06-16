%define module HDBC
%define cabal_setup Setup.lhs

Name: haskell-%{module}
Version: 1.0.1
Release: %mkrel 3
Summary: Haskell Database access 
Group: Development/Other
License: LGPL
# darcs repos, nothing better
Url: http://darcs.complete.org/hdbc-odbc/
Source: %{module}-1.0.1.tar.gz
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: haskell(base)
BuildRequires: haskell(mtl)
BuildRequires: ghc
BuildRequires: haskell-macros

%description
Haskell Database access

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%check
%_cabal_check

%install
%_cabal_install

%_cabal_genscripts

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%_cabal_rpm_files
%_libdir/%module-%version
%_datadir/%module-%version
%doc dist/doc/html

%clean
rm -fr %buildroot


