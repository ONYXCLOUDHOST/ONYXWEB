Name:          onyxweb
Summary:    	  Install nDeploy on centos7 server
Version:    	  4.0.1.3
Release:    	  1%{?dist}
Group:         Development/Libraries
License:       GPLv3
Source0:    	  %{name}-%{version}.tar.gz
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: git
BuildRequires: perl >= 1:v5.10.1
BuildRequires: perl(Module::Build) >= 0.35
BuildRequires: perl(Test::Pod) >= 1.20
Requires:      git
Requires:      git-archive-all
Requires:      rpm-build
Requires:      perl(Getopt::Long)
Requires:      perl(List::Util)
Requires:      perl(IPC::System::Simple) >= 1.17
Requires:      perl(File::Temp)
Requires:      perl(Path::Class)
Requires:      perl(File::Path)
Requires:      perl(File::Copy)
Requires:      perl(File::Basename)
Requires:      perl(Pod::Usage)
BuildArch:	    noarch

%define gitbin %(git --exec-path)
%define gitman %(%{__perl} -E 'my $m = `git --man-path 2> /dev/null`; print $m if $m; ($m = shift) =~ s{libexec\.+}{share/man}; print $m' %{gitbin})

%description
Setup nDeploy on centos7 server
 
%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Build.PL
./Build

%check
./Build test

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%clean
%{__rm} -rf  %{buildroot}

%files
%defattr(-,root,root,-)
%{gitman}/*
%{gitbin}/*

%changelog
* Sun Jun 10 2022 Rick Weston
- Initial configuration of spec file.
