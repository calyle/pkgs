#
# spec file for package hyprland-protocols
#
# Copyright (c) 2024 Jo Carllyle
#

# Please submit bugfixes or comments via https://github.com/calyle/pkgs
#

Name:           hyprland-protocols
Version:        VERSION
Release:        1%{?dist}
Summary:        Wayland protocol extensions for Hyprland
BuildArch:      noarch

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-protocols
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson

%description
%{summary}.

%package        devel
Summary:        Wayland protocol extensions for Hyprland

%description    devel
%{summary}.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%files devel
%license LICENSE
%doc README.md
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/


%changelog
* DATE Jo Carllyle <96739684+calyle@users.noreply.github.com>
- See GitHub for full changelog
