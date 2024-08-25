%define debug_package %{nil}

%global gh_user charmbracelet

Name:           glow
Version:        2.0.0
Release:        1%{?dist}
Summary:        Render markdown on the CLI, with pizzazz!
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
Glow is a terminal based markdown reader designed from the ground
up to bring out the beauty—and power—of the CLI.

Use it to discover markdown files, read documentation directly on
the command line and stash markdown files to your own private
collection so you can read them anywhere. Glow will find local
markdown files in subdirectories or a local Git repository.

%prep
%setup -q -n %{name}-%{version}

%build
go build -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon Aug 26 2024 Jamie Curnow <jc@jc21.com> 2.0.0-1
- https://github.com/charmbracelet/glow/releases/tag/v2.0.0

* Wed May 10 2023 Jamie Curnow <jc@jc21.com> 1.5.1-1
- https://github.com/charmbracelet/glow/releases/tag/v1.5.1

* Fri Feb 3 2023 Jamie Curnow <jc@jc21.com> 1.5.0-1
- https://github.com/charmbracelet/glow/releases/tag/v1.5.0

* Fri Apr 9 2021 Jamie Curnow <jc@jc21.com> 1.4.1-1
- https://github.com/charmbracelet/glow/releases/tag/v1.4.1

* Sun Mar 14 2021 Jamie Curnow <jc@jc21.com> 1.4.0-1
- https://github.com/charmbracelet/glow/releases/tag/v1.4.0

* Sat Dec 26 2020 Jamie Curnow <jc@jc21.com> 1.3.0-1
- https://github.com/charmbracelet/glow/releases/tag/v1.3.0

* Wed Nov 25 2020 Jamie Curnow <jc@jc21.com> 1.2.1-1
- https://github.com/charmbracelet/glow/releases/tag/v1.2.1

* Sun Nov 22 2020 Jamie Curnow <jc@jc21.com> 1.2.0-1
- https://github.com/charmbracelet/glow/releases/tag/v1.2.0

* Wed Oct 28 2020 Jamie Curnow <jc@jc21.com> 1.1.0-1
- https://github.com/charmbracelet/glow/releases/tag/v1.1.0

* Tue Oct 20 2020 Jamie Curnow <jc@jc21.com> 1.0.2-1
- https://github.com/charmbracelet/glow/releases/tag/v1.0.2

