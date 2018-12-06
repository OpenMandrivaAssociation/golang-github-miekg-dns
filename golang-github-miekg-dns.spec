# Run tests in check section
# Disabled because it needs network access
%bcond_with check

# http://github.com/miekg/dns
%global goipath         github.com/miekg/dns
Version:                1.0.5

%global common_description %{expand:
Complete and usable DNS library. All widely used Resource Records are 
supported, including the DNSSEC types. It follows a lean and mean philosophy. 
If there is stuff you should know as a DNS programmer there isn't a 
convenience function for it. Server side and client side programming is 
supported, i.e. you can build servers and resolvers with it.}

%gometa

Name:           %{goname}
Release:        2%{?dist}
Summary:        DNS library in Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(golang.org/x/crypto/ed25519)
BuildRequires: golang(golang.org/x/net/ipv4)
BuildRequires: golang(golang.org/x/net/ipv6)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%gosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md AUTHORS CONTRIBUTORS


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.5-1
- Bump to upstream 1.0.5

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.20151102gitd274557
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitd274557
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gitd274557
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitd274557
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitd274557
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.gitd274557
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.9.gitd274557
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitd274557
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.7.gitd274557
- Bump to upstream d27455715200c7d3e321a1e5cadb27c9ee0b0f02
  related: #1250494

* Tue Oct 27 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.git034c247
- Bump to upstream 034c2472297c31e47588e50cac6979a9f54bda79
  related: #1250494

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gitbb1103f
- Update to spec-2.1
  related: #1250494

* Fri Aug 07 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.4.gitbb1103f
- Update spec file to spec-2.0
  resolves: #1250494

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.gitbb1103f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 09 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.gitbb1103f
- Bump to upstream bb1103f648f811d2018d4bedcb2d4b2bce34a0f1
  related: #1181105

* Mon Jan 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gita07be6b
- First package for Fedora
  resolves: #1181105

