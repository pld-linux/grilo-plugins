Summary:	Collection of plugins for Grilo
Summary(pl.UTF-8):	Zestaw wtyczek dla Grilo
Name:		grilo-plugins
Version:	0.2.17
Release:	1
License:	LGPL v2.1+
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/grilo-plugins/0.2/%{name}-%{version}.tar.xz
# Source0-md5:	691621488045512ff002591631fc7c59
Patch0:		%{name}-sh.patch
URL:		http://live.gnome.org/Grilo
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	avahi-glib-devel
BuildRequires:	avahi-gobject-devel
BuildRequires:	glib2-devel >= 1:2.36
BuildRequires:	gmime-devel >= 2.6.0
BuildRequires:	gnome-common
BuildRequires:	gnome-online-accounts-devel >= 3.18.0
BuildRequires:	gom-devel >= 0.3.0
BuildRequires:	grilo-devel >= 0.2.12
BuildRequires:	intltool >= 0.40.0
BuildRequires:	json-glib-devel
BuildRequires:	libdmapsharing-devel >= 2.9.12
BuildRequires:	libgcrypt-devel
BuildRequires:	libgdata-devel >= 0.9.1
BuildRequires:	libmediaart2-devel >= 1.9
BuildRequires:	liboauth-devel
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	lua53-devel >= 5.3.0
BuildRequires:	pkgconfig
BuildRequires:	rest-devel >= 0.7.90
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	totem-pl-parser-devel >= 3.4.1
BuildRequires:	tracker-devel >= 0.12
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	glib2 >= 1:2.36
Requires:	gmime >= 2.6.0
Requires:	gnome-online-accounts-libs >= 3.18.0
Requires:	gom >= 0.3.0
Requires:	grilo >= 0.2.12
Requires:	libdmapsharing >= 2.9.12
Requires:	libgdata >= 0.9.1
Requires:	rest >= 0.7.90
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
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%{__rm} $RPM_BUILD_ROOT%{_libdir}/grilo-0.2/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README

%{_libdir}/grilo-0.2/grl-bookmarks.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlbookmarks.so

%{_libdir}/grilo-0.2/grl-dleyna.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrldleyna.so

%{_libdir}/grilo-0.2/grl-daap.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrldaap.so
%{_libdir}/grilo-0.2/grl-dpap.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrldpap.so

%{_libdir}/grilo-0.2/grl-filesystem.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlfilesystem.so

%{_libdir}/grilo-0.2/grl-flickr.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlflickr.so

%{_libdir}/grilo-0.2/grl-freebox.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlfreebox.so

%{_libdir}/grilo-0.2/grl-gravatar.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlgravatar.so

%{_libdir}/grilo-0.2/grl-jamendo.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrljamendo.so

%{_libdir}/grilo-0.2/grl-local-metadata.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrllocalmetadata.so

%{_libdir}/grilo-0.2/grl-lua-factory.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlluafactory.so
%dir %{_datadir}/grilo-plugins
%dir %{_datadir}/grilo-plugins/grl-lua-factory
%{_datadir}/grilo-plugins/grl-lua-factory/grl-appletrailers.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-appletrailers.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-euronews.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-euronews.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-guardianvideos.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-guardianvideos.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-lastfm-cover.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-metrolyrics.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-musicbrainz.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-pocket.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-pocket.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-radiofrance.gresource
%{_datadir}/grilo-plugins/grl-lua-factory/grl-radiofrance.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-spotify-cover.lua
%{_datadir}/grilo-plugins/grl-lua-factory/grl-video-title-parsing.lua

%{_libdir}/grilo-0.2/grl-magnatune.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlmagnatune.so

%{_libdir}/grilo-0.2/grl-metadata-store.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlmetadatastore.so

%{_libdir}/grilo-0.2/grl-opensubtitles.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlopensubtitles.so

%{_libdir}/grilo-0.2/grl-optical-media.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrloptical-media.so

%{_libdir}/grilo-0.2/grl-podcasts.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlpodcasts.so

%{_libdir}/grilo-0.2/grl-raitv.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlraitv.so

%{_libdir}/grilo-0.2/grl-shoutcast.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlshoutcast.so

%{_libdir}/grilo-0.2/grl-thetvdb.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlthetvdb.so

%{_libdir}/grilo-0.2/grl-vimeo.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlvimeo.so

%{_libdir}/grilo-0.2/grl-tmdb.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrltmdb.so
%dir %{_datadir}/help/C/examples
%{_datadir}/help/C/examples/example-tmdb.c

%{_libdir}/grilo-0.2/grl-tracker.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrltracker.so

%{_libdir}/grilo-0.2/grl-youtube.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlyoutube.so
