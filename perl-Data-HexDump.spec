%define modname	Data-HexDump
%define modver	0.02

Summary:	A Simple Hexadecimal Dumper	
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPLv2
Group:		Development/Perl
Url:		http://www.cpan.org/%{modname}
Source0:	http://www.cpan.org/authors/id/F/FT/FTASSIN/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
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

# (sb) conflicts with util-linux
mv %{buildroot}%{_bindir}/hexdump %{buildroot}%{_bindir}/perl-hexdump

%files
%dir %{perl_vendorlib}/Data
%{perl_vendorlib}/Data/HexDump.pm
%{_bindir}/perl-hexdump
%{_mandir}/man3/Data::HexDump.3pm*

