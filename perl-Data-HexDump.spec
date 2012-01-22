%define upstream_name	 Data-HexDump
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	A Simple Hexadecimal Dumper	
License:	GPL
Group:		Development/Perl
Requires:	perl
Url:		http://www.cpan.org/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/F/FT/FTASSIN/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Dump in hexadecimal the content of a scalar. The result is returned 
in a string. Each line of the result consists of the offset in the
source in the leftmost column of each line, followed by one or more
columns of data from the source in hexadecimal. The rightmost column
of each line shows the printable characters (all others are shown
as single dots)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
make OPTIMIZE="$RPM_OPT_FLAGS" 
make test

%install
rm -rf %{buildroot} 
%makeinstall_std 

# (sb) conflicts with util-linux
mv %{buildroot}%{_bindir}/hexdump %{buildroot}%{_bindir}/perl-hexdump

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%{_mandir}/man3/Data::HexDump.3pm*
%dir %{perl_vendorlib}/Data
%{perl_vendorlib}/Data/HexDump.pm
%{_bindir}/perl-hexdump
