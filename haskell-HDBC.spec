%global debug_package %{nil}
%define _cabal_setup Setup.lhs
#% define _no_haddock 1
%define module HDBC
Name:           haskell-%{module}
Version:        2.3.1.1
Release:        1
Summary:        Haskell Database Connectivity
Group:          Development/Other
License:        BSD
URL:            http://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz

BuildRequires:  ghc, ghc-devel, haskell-macros, haddock
buildrequires:  haskell(mtl) haskell(convertible) haskell(text) haskell(utf8-string)
Requires(pre):  ghc
requires(pre):  haskell(mtl) haskell(convertible) haskell(text) haskell(utf8-string)

%description
HDBC provides an abstraction layer between Haskell programs and SQL relational
databases. This lets you write database code once, in Haskell, and have it work
with any number of backend SQL databases (MySQL, Oracle, PostgreSQL,
ODBC-compliant databases, etc.)

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

%files
%defattr(-,root,root,-)
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%_cabal_haddoc_files



