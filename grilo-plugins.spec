#
# Conditional build:
%bcond_without	libdmapsharing4		# libdmapsharing 4 (3.9.x) instead of 3 (2.9.x)

%if %{with libdmapsharing4}
%define		libdmapsharing_ver	3.9.9
%else
%define		libdmapsharing_ver	2.9.12
%endif
Summary:	Collection of plugins for Grilo
Summary(pl.UTF-8):	Zestaw wtyczek dla Grilo
Name:		grilo-plugins
Version:	0.3.13
Release:	1
License:	LGPL v2.1+
Group:		Applications/Multimedia
Source0:	https://download.gnome.org/sources/grilo-plugins/0.3/%{name}-%{version}.tar.xz
# Source0-md5:	4c33227c77a821b704a003e4a374a380
URL:		https://wiki.gnome.org/Projects/Grilo
BuildRequires:	avahi-glib-devel
BuildRequires:	avahi-gobject-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	gnome-online-accounts-devel >= 3.18.0
BuildRequires:	gom-devel >= 0.4
BuildRequires:	gperf
BuildRequires:	grilo-devel >= 0.3.8
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	json-glib-devel
BuildRequires:	libarchive-devel
BuildRequires:	libdmapsharing-devel >= %{libdmapsharing_ver}
%if %{with libdmapsharing4}
BuildRequires:	libdmapsharing-devel < 4.9
%else
BuildRequires:	libdmapsharing-devel < 3.9
%endif
BuildRequires:	libgdata-devel >= 0.9.1
BuildRequires:	libmediaart2-devel >= 1.9
BuildRequires:	liboauth-devel
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	lua53-devel >= 5.3.0
BuildRequires:	meson >= 0.44.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	totem-pl-parser-devel >= 3.4.1
BuildRequires:	tracker3-devel >= 3.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	glib2 >= 1:2.44
Requires:	gnome-online-accounts-libs >= 3.18.0
Requires:	gom >= 0.4
Requires:	grilo >= 0.3.8
Requires:	libdmapsharing >= %{libdmapsharing_ver}
Requires:	libgdata >= 0.9.1
Requires:	totem-pl-parser >= 3.4.1
Requires:	tracker3 >= 3.0
Suggests:	dleyna-server
Obsoletes:	totem-tracker < 3.2
Obsoletes:	totem-upnp < 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of plugins for Grilo implementing Grilo's API for various
multimedia content providers.

%description -l pl.UTF-8
Zestaw wtyczek dla Grilo, zawierających implementuje API Grilo dla
różnych dostawców treści multimedialnych.

%prep
%setup -q

%build
%meson build \
	-Denable-tracker=no

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%dir %{_libdir}/grilo-0.3
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlbookmarks.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlchromaprint.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrldaap.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrldleyna.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrldpap.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlfilesystem.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlflickr.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlfreebox.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlgravatar.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrllocalmetadata.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlluafactory.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlmagnatune.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlmetadatastore.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlopensubtitles.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlopticalmedia.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlpodcasts.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlraitv.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlshoutcast.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlthetvdb.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrltmdb.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrltracker3.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlyoutube.so
%dir %{_datadir}/grilo-plugins
%dir %{_datadir}/grilo-plugins/grl-lua-factory
%{_datadir}/grilo-plugins/grl-lua-factory/grl-acoustid.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-appletrailers.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-appletrailers.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-euronews.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-euronews.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-guardianvideos.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-guardianvideos.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-itunes-podcast.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-itunes-podcast.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-lastfm-cover.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-musicbrainz-coverart.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-radiofrance.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-radiofrance.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-steam-store.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-theaudiodb-cover.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-thegamesdb.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-video-title-parsing.lua

%dir %{_datadir}/help/C/examples
%{_datadir}/help/C/examples/example-tmdb.c
%lang(cs) %dir %{_datadir}/help/cs/examples
%lang(cs) %{_datadir}/help/cs/examples/example-tmdb.c
%lang(da) %dir %{_datadir}/help/da/examples
%lang(da) %{_datadir}/help/da/examples/example-tmdb.c
%lang(de) %dir %{_datadir}/help/de/examples
%lang(de) %{_datadir}/help/de/examples/example-tmdb.c
%lang(es) %dir %{_datadir}/help/es/examples
%lang(es) %{_datadir}/help/es/examples/example-tmdb.c
%lang(pl) %dir %{_datadir}/help/pl/examples
%lang(pl) %{_datadir}/help/pl/examples/example-tmdb.c
%lang(pt_BR) %dir %{_datadir}/help/pt_BR/examples
%lang(pt_BR) %{_datadir}/help/pt_BR/examples/example-tmdb.c
%lang(sv) %dir %{_datadir}/help/sv/examples
%lang(sv) %{_datadir}/help/sv/examples/example-tmdb.c
%lang(uk) %dir %{_datadir}/help/uk/examples
%lang(uk) %{_datadir}/help/uk/examples/example-tmdb.c
%{_pkgconfigdir}/grilo-plugins-0.3.pc
