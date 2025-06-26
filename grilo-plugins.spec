#
# Conditional build:
%bcond_without	libdmapsharing4	# libdmapsharing 4 (3.9.x) instead of 3 (2.9.x) for libsoup 2.4
%bcond_without	libgdata	# libgdata based youtube support (libsoup 2.4 only)

%define		soup_api	%(pkg-config --variable=soupapiversion grilo-net-0.3 2>/dev/null || echo 2.4)

%if "%{soup_api}" == "2.4"
%if %{with libdmapsharing4}
%define		libdmapsharing_ver	3.9.9
%define		libdmapsharing_ver_lt	3.9.11
%else
%define		libdmapsharing_ver	2.9.12
%define		libdmapsharing_ver_lt	3.9
%endif
%else
%undefine	with_libgdata
%define		libdmapsharing_ver	3.9.11
%define		libdmapsharing_ver_lt	4.9
%endif

Summary:	Collection of plugins for Grilo
Summary(pl.UTF-8):	Zestaw wtyczek dla Grilo
Name:		grilo-plugins
Version:	0.3.18
Release:	1
License:	LGPL v2.1+
Group:		Applications/Multimedia
Source0:	https://download.gnome.org/sources/grilo-plugins/0.3/%{name}-%{version}.tar.xz
# Source0-md5:	4ff2feaf4da5a00e02efd471f23c9d18
Patch0:		%{name}-libdmapsharing4.patch
URL:		https://wiki.gnome.org/Projects/Grilo
BuildRequires:	avahi-glib-devel
BuildRequires:	avahi-gobject-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.66
BuildRequires:	gnome-online-accounts-devel >= 3.18.0
BuildRequires:	gom-devel >= 0.4
BuildRequires:	gperf
BuildRequires:	grilo-devel >= 0.3.8
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	json-glib-devel
BuildRequires:	libarchive-devel
BuildRequires:	libdmapsharing-devel >= %{libdmapsharing_ver}
BuildRequires:	libdmapsharing-devel < %{libdmapsharing_ver_lt}
%{?with_libgdata:BuildRequires:	libgdata-devel >= 0.17.0}
BuildRequires:	libmediaart2-devel >= 1.9
BuildRequires:	liboauth-devel
%if "%{soup_api}" == "2.4"
BuildRequires:	libsoup-devel >= 2.4
%else
BuildRequires:	libsoup3-devel >= 3.0
%endif
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	lua53-devel >= 5.3.0
BuildRequires:	meson >= 0.47.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	totem-pl-parser-devel >= 3.4.1
BuildRequires:	tracker3-devel >= 3.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	glib2 >= 1:2.66
Requires:	gnome-online-accounts-libs >= 3.18.0
Requires:	gom >= 0.4
Requires:	grilo >= 0.3.8
Requires:	libdmapsharing >= %{libdmapsharing_ver}
%{?with_libgdata:Requires:	libgdata >= 0.17.0}
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
%patch -P0 -p1

# disable localsearch tests
%{__sed} -i -e "/subdir('tracker3')/d" tests/meson.build

%build
%meson \
	-Denable-tracker=no \
	%{!?with_libgdata:-Denable-youtube=no} \
	-Dgoa=enabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
%if "%{soup_api}" == "2.4"
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlopensubtitles.so
%endif
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlopticalmedia.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlpodcasts.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlshoutcast.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlthetvdb.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrltmdb.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrltracker3.so
%if %{with libgdata}
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlyoutube.so
%endif
%dir %{_datadir}/grilo-plugins
%dir %{_datadir}/grilo-plugins/grl-lua-factory
%{_datadir}/grilo-plugins/grl-lua-factory/grl-acoustid.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-guardianvideos.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-guardianvideos.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-iptv.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-iptv.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-itunes-podcast.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-itunes-podcast.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-lastfm-cover.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-musicbrainz-coverart.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-opensubtitles.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-radiofrance.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-radiofrance.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-steam-store.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-theaudiodb-cover.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-thegamesdb.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-video-title-parsing.lua

%dir %{_datadir}/help/C/examples
%{_datadir}/help/C/examples/example-tmdb.c
%lang(ca) %dir %{_datadir}/help/ca/examples
%lang(ca) %{_datadir}/help/ca/examples/example-tmdb.c
%lang(cs) %dir %{_datadir}/help/cs/examples
%lang(cs) %{_datadir}/help/cs/examples/example-tmdb.c
%lang(da) %dir %{_datadir}/help/da/examples
%lang(da) %{_datadir}/help/da/examples/example-tmdb.c
%lang(de) %dir %{_datadir}/help/de/examples
%lang(de) %{_datadir}/help/de/examples/example-tmdb.c
%lang(es) %dir %{_datadir}/help/es/examples
%lang(es) %{_datadir}/help/es/examples/example-tmdb.c
%lang(eu) %dir %{_datadir}/help/eu/examples
%lang(eu) %{_datadir}/help/eu/examples/example-tmdb.c
%lang(fr) %dir %{_datadir}/help/fr/examples
%lang(fr) %{_datadir}/help/fr/examples/example-tmdb.c
%lang(gl) %dir %{_datadir}/help/gl/examples
%lang(gl) %{_datadir}/help/gl/examples/example-tmdb.c
%lang(hu) %dir %{_datadir}/help/hu/examples
%lang(hu) %{_datadir}/help/hu/examples/example-tmdb.c
%lang(nl) %dir %{_datadir}/help/nl/examples
%lang(nl) %{_datadir}/help/nl/examples/example-tmdb.c
%lang(pl) %dir %{_datadir}/help/pl/examples
%lang(pl) %{_datadir}/help/pl/examples/example-tmdb.c
%lang(pt_BR) %dir %{_datadir}/help/pt_BR/examples
%lang(pt_BR) %{_datadir}/help/pt_BR/examples/example-tmdb.c
%lang(ru) %dir %{_datadir}/help/ru/examples
%lang(ru) %{_datadir}/help/ru/examples/example-tmdb.c
%lang(sv) %dir %{_datadir}/help/sv/examples
%lang(sv) %{_datadir}/help/sv/examples/example-tmdb.c
%lang(uk) %dir %{_datadir}/help/uk/examples
%lang(uk) %{_datadir}/help/uk/examples/example-tmdb.c
%{_pkgconfigdir}/grilo-plugins-0.3.pc
