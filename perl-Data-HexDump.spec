%define module	Data-HexDump
%define name	perl-%{module}
%define version 0.02
%define release %mkrel 7

Summary:	A Simple Hexadecimal Dumper	
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Requires:	perl
URL:		http://www.cpan.org
Source:		http://www.cpan.org/authors/id/F/FT/FTASSIN/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-root
BuildArch:	noarch

%description
Dump in hexadecimal the content of a scalar. The result is returned 
in a string. Each line of the result consists of the offset in the
source in the leftmost column of each line, followed by one or more
columns of data from the source in hexadecimal. The rightmost column
of each line shows the printable characters (all others are shown
as single dots)

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
make OPTIMIZE="$RPM_OPT_FLAGS" 
make test

%install
rm -rf $RPM_BUILD_ROOT 
%makeinstall_std 

# (sb) conflicts with util-linux
mv $RPM_BUILD_ROOT%{_bindir}/hexdump $RPM_BUILD_ROOT%{_bindir}/perl-hexdump

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%{_mandir}/man3/Data::HexDump.3pm*
%dir %{perl_vendorlib}/Data
%{perl_vendorlib}/Data/HexDump.pm
%{_bindir}/perl-hexdump


