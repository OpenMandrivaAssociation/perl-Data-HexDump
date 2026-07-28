%define modname Data-HexDump
%define modver 0.04

Summary:	A Simple Hexadecimal Dumper	
Name:		perl-%{modname}
Version:	%{modver}
Release:	3
License:	GPLv2
Group:		Development/Perl
Url:		https://github.com/neilb/Data-HexDump
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/Data-HexDump-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
Requires:	perl

%description
Dump in hexadecimal the content of a scalar. The result is returned 
in a string. Each line of the result consists of the offset in the
source in the leftmost column of each line, followed by one or more
columns of data from the source in hexadecimal. The rightmost column
of each line shows the printable characters (all others are shown
as single dots)

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor 
%make OPTIMIZE="%{optflags}"

%check
%make test

%install
%makeinstall_std
install -D -m 755 eg/hexdump %{buildroot}%{_bindir}/perl-hexdump 

# (sb) conflicts with util-linux

%files
%dir %{perl_vendorlib}/Data
%{perl_vendorlib}/Data/HexDump.pm
%{_bindir}/perl-hexdump
%{_mandir}/man3/Data::HexDump.3pm*

