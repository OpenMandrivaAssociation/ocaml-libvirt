%define name	ocaml-libvirt
%define version	0.6.1.0
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	OCaml bindings for libvirt
License:	LGPL
Group:		Development/Other
URL:		http://libvirt.org/ocaml/
Source:	    http://libvirt.org/sources/ocaml/%{name}-%{version}.tar.gz	
BuildRequires:	ocaml
BuildRequires:  ocaml-findlib
BuildRequires:	libvirt-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
ocaml-libvirt are OCaml bindings for libvirt, allowing you to write OCaml
programs and scripts which control virtualisation features. Some things which
you might want to do with ocaml-libvirt:

* Monitor performance of virtual machines
* Pause and resume virtual machines according to demand
* Provision new virtual machines automatically for customers
* Configure how virtual machines are networked together

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	libvirt-devel
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q

%build
%configure2_5x
%make all
%make opt

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/stublibs
make install-opt \
    OCAMLFIND_DESTDIR="%{buildroot}/%{_libdir}/ocaml" \
    DESTDIR=%{buildroot}
rm -f  %{buildroot}/%{_libdir}/ocaml/stublibs/*.owner

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO.libvirt ChangeLog COPYING COPYING.LIB
/usr/bin/mlvirsh
%dir %{_libdir}/ocaml/libvirt
%{_libdir}/ocaml/libvirt/*.cmi
%{_libdir}/ocaml/libvirt/*.cma
%{_libdir}/ocaml/libvirt/META
%{_libdir}/ocaml/stublibs/*.so

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/libvirt/*.a
%{_libdir}/ocaml/libvirt/*.cmx
%{_libdir}/ocaml/libvirt/*.cmxa
%{_libdir}/ocaml/libvirt/*.mli

