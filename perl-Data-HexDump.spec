%define upstream_name	 Data-HexDump
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	A Simple Hexadecimal Dumper	
License:	GPL
Group:		Development/Perl
Requires:	perl
Url:		http://www.cpan.org/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/F/FT/FTASSIN/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

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
%__perl Makefile.PL INSTALLDIRS=vendor 
make OPTIMIZE="%{optflags}"
make test

%install
%makeinstall_std 

# (sb) conflicts with util-linux
mv %{buildroot}%{_bindir}/hexdump %{buildroot}%{_bindir}/perl-hexdump

%files
%{_mandir}/man3/Data::HexDump.3pm*
%dir %{perl_vendorlib}/Data
%{perl_vendorlib}/Data/HexDump.pm
%{_bindir}/perl-hexdump


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-4mdv2012.0
+ Revision: 765145
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-3
+ Revision: 763659
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.20.0-2
+ Revision: 667075
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 403043
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.02-7mdv2009.1
+ Revision: 351701
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.02-6mdv2009.0
+ Revision: 223594
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.02-5mdv2008.1
+ Revision: 122447
- kill re-definition of %%buildroot on Pixel's request
- do not hardcode bz2 extension


* Sat Mar 03 2007 Stew Benedict <sbenedict@mandriva.com> 0.02-5mdv2007.0
+ Revision: 131784
- rebuild, %%mkrel, fix typo in summary

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Data-HexDump

* Mon Feb 06 2006 Stew Benedict <sbenedict@mandriva.com> 0.02-4mdk
- annual rebuild

* Fri Jan 07 2005 Stew Benedict <sbenedict@mandrakesoft.com> 0.02-3mdk
- birthday rebuild, URL

