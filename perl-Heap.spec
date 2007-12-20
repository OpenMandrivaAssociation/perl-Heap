%define module	Heap
%define name	perl-%{module}
%define version 0.80
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/J/JM/JMM/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Heap.pm
%{perl_vendorlib}/Heap
%{_mandir}/*/*

