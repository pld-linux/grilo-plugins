Summary:	Collection of plugins for Grilo
Summary(pl.UTF-8):	Zestaw wtyczek dla Grilo
Name:		grilo-plugins
Version:	0.3.8
Release:	3
License:	LGPL v2.1+
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/grilo-plugins/0.3/%{name}-%{version}.tar.xz
# Source0-md5:	e1a2c6c59610fce5799466dcd6507602
# https://gitlab.gnome.org/GNOME/grilo-plugins/merge_requests/49.patch
Patch0:		%{name}-libdmapsharing4.patch
URL:		https://wiki.gnome.org/Projects/Grilo
BuildRequires:	avahi-glib-devel
BuildRequires:	avahi-gobject-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	gmime-devel >= 2.6.0
BuildRequires:	gnome-online-accounts-devel >= 3.18.0
BuildRequires:	gom-devel >= 0.3.2
BuildRequires:	gperf
BuildRequires:	grilo-devel >= 0.3.6
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	json-glib-devel
BuildRequires:	libarchive-devel
BuildRequires:	libdmapsharing-devel >= 2.9.12
BuildRequires:	libgcrypt-devel
BuildRequires:	libgdata-devel >= 0.9.1
BuildRequires:	libmediaart2-devel >= 1.9
BuildRequires:	liboauth-devel
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	lua53-devel >= 5.3.0
BuildRequires:	meson >= 0.37.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	totem-pl-parser-devel >= 3.4.1
BuildRequires:	tracker-devel >= 2.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	glib2 >= 1:2.44
Requires:	gmime >= 2.6.0
Requires:	gnome-online-accounts-libs >= 3.18.0
Requires:	gom >= 0.3.2
Requires:	grilo >= 0.3.6
Requires:	libdmapsharing >= 2.9.12
Requires:	libgdata >= 0.9.1
Requires:	totem-pl-parser >= 3.4.1
Suggests:	dleyna-server
Obsoletes:	totem-jamendo
Obsoletes:	totem-tracker
Obsoletes:	totem-upnp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of plugins for Grilo implementing Grilo's API for various
multimedia content providers.

%description -l pl.UTF-8
Zestaw wtyczek dla Grilo, zawierających implementuje API Grilo dla
różnych dostawców treści multimedialnych.

%prep
%setup -q
%patch0 -p1

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
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
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrljamendo.so
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
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrltracker.so
%attr(755,root,root) %{_libdir}/grilo-0.3/libgrlvimeo.so
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
%{_datadir}/grilo-plugins/grl-lua-factory/grl-metrolyrics.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-musicbrainz.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-pocket.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-pocket.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-radiofrance.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-radiofrance.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-spotify-cover.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-theaudiodb-cover.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-thegamesdb.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-video-title-parsing.lua

%dir %{_datadir}/help/C/examples
%dir %{_datadir}/help/cs/examples
%dir %{_datadir}/help/de/examples
%dir %{_datadir}/help/es/examples
%dir %{_datadir}/help/pl/examples
%dir %{_datadir}/help/pt_BR/examples
%dir %{_datadir}/help/sv/examples
%{_datadir}/help/*/examples/example-tmdb.c
%{_pkgconfigdir}/grilo-plugins-0.3.pc
