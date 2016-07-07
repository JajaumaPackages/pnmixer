Name:           pnmixer
Version:        0.6.1
Release:        1%{?dist}
Summary:        Lightweight mixer applet

License:        GPLv3
URL:            https://github.com/nicklan/pnmixer
Source0:        https://github.com/nicklan/pnmixer/archive/v%{version}.tar.gz

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  intltool
BuildRequires:  gettext
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils

%description
PNMixer is a simple mixer application designed to run in your system tray. It
integrates nicely into desktop environments that don't have a panel that
supports applets and therefore can't run a mixer applet. In particular it's
been used quite a lot with fbpanel and tint2, but should run fine in any system
tray.


%prep
%setup -q
NOCONFIGURE=yes ./autogen.sh


%build
%configure \
    --enable-minimal-flags \
    --with-gtk3 \
    --with-libnotify
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
%find_lang %{name}


%post
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ]; then
    touch --no-create %{_datadir}/icons/hicolor &> /dev/null ||:
    gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :


%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README.md
%{_bindir}/*
%{_datadir}/pnmixer/
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/applications/*


%changelog
* Thu Jul 07 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.6.1-1
- Public release
