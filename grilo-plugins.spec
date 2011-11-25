Summary:	Grilo plugins
Name:		grilo-plugins
Version:	0.1.17
Release:	2
License:	LGPL v2.1+
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/grilo-plugins/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	4553c823b3434a2b8187d1f95b5e61cc
URL:		http://live.gnome.org/Grilo
Patch0:		tracker.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gmime-devel >= 2.4
BuildRequires:	gnome-common
BuildRequires:	grilo-devel >= 0.1.17
BuildRequires:	gupnp-av-devel >= 0.5
BuildRequires:	gupnp-devel >= 0.13
BuildRequires:	libgcrypt-devel
BuildRequires:	libgdata-devel >= 0.9.1
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool >= 2.2.6
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRequires:	quvi-devel >= 0.2.15
BuildRequires:	rest-devel >= 0.7
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 0.12
BuildRequires:	xz
Requires:	grilo >= 0.1.17
Obsoletes:	totem-jamendo
Obsoletes:	totem-tracker
Obsoletes:	totem-upnp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of plugins for Grilo implementing Grilo's API for various
multimedia content providers.

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/grilo-0.1/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/grilo-0.1/grl-apple-trailers.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrlappletrailers.so

%{_libdir}/grilo-0.1/grl-bliptv.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrlbliptv.so

%{_libdir}/grilo-0.1/grl-bookmarks.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrlbookmarks.so

%{_libdir}/grilo-0.1/grl-filesystem.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrlfilesystem.so

%{_libdir}/grilo-0.1/grl-flickr.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrlflickr.so

%{_libdir}/grilo-0.1/grl-gravatar.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrlgravatar.so

%{_libdir}/grilo-0.1/grl-jamendo.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrljamendo.so

%{_libdir}/grilo-0.1/grl-lastfm-albumart.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrllastfm-albumart.so

%{_libdir}/grilo-0.1/grl-local-metadata.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrllocalmetadata.so

%{_libdir}/grilo-0.1/grl-metadata-store.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrlmetadatastore.so

%{_libdir}/grilo-0.1/grl-podcasts.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrlpodcasts.so

%{_libdir}/grilo-0.1/grl-vimeo.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrlvimeo.so

%{_libdir}/grilo-0.1/grl-upnp.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrlupnp.so

%{_libdir}/grilo-0.1/grl-tracker.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrltracker.so

%{_libdir}/grilo-0.1/grl-youtube.xml
%attr(755,root,root) %{_libdir}/grilo-0.1/libgrlyoutube.so
