Name:           wlcreator
Version:        1.0.3
Release:        3%{?dist}.R
BuildArch:      noarch
Summary:        Creating Linux desktop launchers for Windows programs

License:        GPLv3+
URL:            http://code.google.com/p/wine-launcher-creator/
Source0:        http://wine-launcher-creator.googlecode.com/files/wine-launcher-creator-%{version}.tar.gz 
Source1:        wlcreator.desktop

# WLCreator works only with ascii path. This patch fix it.
Patch0:         wlcreator-utf-8-support.patch

# For converting ico to png is used ImageMagic. I use icoutils.
Patch1:         wlcreator-icotool.patch

BuildRequires:  desktop-file-utils
Requires:       icoutils, PyQt4

%description
WLCreator is a Python program (script) that creates Linux desktop launchers 
for Windows programs (using Wine).

%prep
%setup -q -n wine-launcher-creator
%patch0 -p1
%patch1 -p1

%build

%install
%{__install} -D wlcreator.py $RPM_BUILD_ROOT%{_bindir}/wlcreator
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications/ %{SOURCE1}

%files
%defattr(-,root,root,-)
%doc NoInternet.txt Readme.txt gpl.txt
%{_bindir}/wlcreator
%{_datadir}/applications/wlcreator.desktop

%changelog
* Fri Nov 04 2011 Romanov Ivan <drizt@land.ru> 1.0.3-3
- Dropped useless docs installing

* Thu Nov 03 2011 Romanov Ivan <drizt@land.ru> 1.0.3-2
- Added wlcreator-utf-8-support patch
- Added wlcreator-icotool patch

* Tue Nov 01 2011 Romanov Ivan <drizt@land.ru> 1.0.3-1
- Initial version
