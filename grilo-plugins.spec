Summary:	Collection of plugins for Grilo
Summary(pl.UTF-8):	Zestaw wtyczek dla Grilo
Name:		grilo-plugins
Version:	0.2.9
Release:	3
License:	LGPL v2.1+
Group:		Applications/Multimedia
Source0:	http://ftp.gnome.org/pub/GNOME/sources/grilo-plugins/0.2/%{name}-%{version}.tar.xz
# Source0-md5:	cdf6d3d410526bcd2abdec28830175c4
URL:		http://live.gnome.org/Grilo
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gmime-devel >= 2.6.0
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils >= 0.9.0
BuildRequires:	gnome-online-accounts-devel >= 3.7.1
BuildRequires:	grilo-devel >= 0.2.6
BuildRequires:	gssdp-devel
BuildRequires:	gupnp-av-devel >= 0.5
BuildRequires:	gupnp-devel >= 0.13
BuildRequires:	intltool >= 0.40.0
BuildRequires:	json-glib-devel
BuildRequires:	libdmapsharing-devel >= 2.9.12
BuildRequires:	libgcrypt-devel
BuildRequires:	libgdata-devel >= 0.9.1
BuildRequires:	liboauth-devel
BuildRequires:	libquvi-devel >= 0.4.0
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	rest-devel >= 0.7
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	totem-pl-parser-devel >= 3.4.1
BuildRequires:	tracker-devel >= 0.12
BuildRequires:	xz
Requires:	glib2 >= 1:2.28.0
Requires:	grilo >= 0.2.6
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
%{_libdir}/grilo-0.2/grl-apple-trailers.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlappletrailers.so

%{_libdir}/grilo-0.2/grl-bliptv.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlbliptv.so

%{_libdir}/grilo-0.2/grl-bookmarks.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlbookmarks.so

%{_libdir}/grilo-0.2/grl-dmap.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrldmap.so

%{_libdir}/grilo-0.2/grl-filesystem.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlfilesystem.so

%{_libdir}/grilo-0.2/grl-flickr.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlflickr.so

%{_libdir}/grilo-0.2/grl-gravatar.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlgravatar.so

%{_libdir}/grilo-0.2/grl-jamendo.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrljamendo.so

%{_libdir}/grilo-0.2/grl-lastfm-albumart.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrllastfm-albumart.so

%{_libdir}/grilo-0.2/grl-local-metadata.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrllocalmetadata.so

%{_libdir}/grilo-0.2/grl-magnatune.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlmagnatune.so

%{_libdir}/grilo-0.2/grl-metadata-store.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlmetadatastore.so

%{_libdir}/grilo-0.2/grl-optical-media.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrloptical-media.so

%{_libdir}/grilo-0.2/grl-podcasts.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlpodcasts.so

%{_libdir}/grilo-0.2/grl-raitv.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlraitv.so

%{_libdir}/grilo-0.2/grl-shoutcast.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlshoutcast.so

%{_libdir}/grilo-0.2/grl-vimeo.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlvimeo.so

%{_libdir}/grilo-0.2/grl-upnp.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlupnp.so

%{_libdir}/grilo-0.2/grl-tmdb.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrltmdb.so

%{_libdir}/grilo-0.2/grl-tracker.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrltracker.so

%{_libdir}/grilo-0.2/grl-youtube.xml
%attr(755,root,root) %{_libdir}/grilo-0.2/libgrlyoutube.so
