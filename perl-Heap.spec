%define upstream_name	 Heap
%define upstream_version 0.80
Name:		perl-%{upstream_name}
Version:	0.80
Release:	1

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Heap
Source0:	https://cpan.metacpan.org/authors/id/J/JM/JMM/Heap-0.80.tar.gz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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


