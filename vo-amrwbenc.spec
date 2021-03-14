Name:       vo-amrwbenc
Version:    0.1.3
Release:    4%{?dist}
Summary:    VisualOn AMR-WB encoder library
License:    ASL 2.0
URL:        http://opencore-amr.sourceforge.net/

Source0:    http://sourceforge.net/projects/opencore-amr/files/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc

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
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING
%doc README NOTICE
%{_libdir}/libvo-amrwbenc.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/libvo-amrwbenc.so
%{_libdir}/pkgconfig/vo-amrwbenc.pc

%changelog
* Thu Sep 20 2018 Simone Caronni <negativo17@gmail.com> - 0.1.3-4
- Add GCC build requirement.

* Mon Jun 13 2016 Simone Caronni <negativo17@gmail.com> - 0.1.3-2
- Update to 0.1.3.
- SPEC file cleanup

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
