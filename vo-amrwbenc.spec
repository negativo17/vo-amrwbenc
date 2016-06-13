Name:       vo-amrwbenc
Version:    0.1.2
Release:    1%{?dist}
Summary:    VisualOn AMR-WB encoder library
License:    ASL 2.0
URL:        http://opencore-amr.sourceforge.net/

Source0:    http://sourceforge.net/projects/opencore-amr/files/%{name}/%{name}-%{version}.tar.gz

%description
This library contains an encoder implementation of the Adaptive Multi Rate
Wideband (AMR-WB) audio codec. The library is based on a codec implementation by
VisualOn as part of the Stagefright framework from the Google Android project.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name "*.la" -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README NOTICE
%{_libdir}/libvo-amrwbenc.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/libvo-amrwbenc.so
%{_libdir}/pkgconfig/vo-amrwbenc.pc

%changelog
* Mon Jun 13 2016 Simone Caronni <negativo17@gmail.com> - 0.1.3-2
- Update to 0.1.3.
- SPEC file cleanup

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
