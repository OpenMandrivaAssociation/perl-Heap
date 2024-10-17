%define upstream_name	 Heap
%define upstream_version 0.80

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/J/JM/JMM/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The Heap collection of modules provide routines that manage a heap of
elements. A heap is a partially sorted structure that is always able to
easily extract the smallest of the elements in the structure (or the
largest if a reversed compare routine is provided). 

If the collection of elements is changing dynamically, the heap has less
overhead than keeping the collection fully sorted. 

The elements must be objects as described in "Heap::Elem" and all
elements inserted into one heap must be mutually compatible - either the
same class exactly or else classes that differ only in ways unrelated to
the Heap::Elem interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/Heap.pm
%{perl_vendorlib}/Heap
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.800.0-1mdv2010.0
+ Revision: 403238
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.80-3mdv2009.0
+ Revision: 268527
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.80-2mdv2009.0
+ Revision: 210957
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 0.80-1mdv2008.0
+ Revision: 21466
- update to 0.80


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.71-5mdv2007.0
- Rebuild

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.71-4mdk
- spec cleanup
- %%mkrel
- better URL
- rpmbuildupdate aware

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.71-3mdk
- fix buildrequires in a backward compatible way

* Sat Aug 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.71-2mdk 
- make test

* Sat Jun 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.71-1mdk
- 0.71

* Wed Jun 02 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.70-1mdk
- 0.70

