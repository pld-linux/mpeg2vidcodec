Summary:	MPEG-2 Encoder / Decoder
Summary(pl):	Koder i dekoder plików MPEG-2
Name:		mpeg2vidcodec
Version:	1.2
Release:	7
License:	Freeware
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.mpeg.org/pub/mpeg/mssg/%{name}_v12.tar.gz
# Source0-md5:	4a66565979be0818bd8a41d948943451
URL:		http://www.mpeg.org/MPEG/MSSG/
BuildRequires:	xorg-lib-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains an implementation of an ISO/IEC DIS 13818-2
codec. It converts uncompressed video frames into MPEG-1 and MPEG-2
video coded bitstream sequences, and vice versa.

%description -l pl
Ten pakiet zawiera implementacjê kodowania ISO/IEC DIS 13818-2.
Konwertuje nieskompresowane klatki obrazu na strumieñ MPEG-1 lub
MPEG-2 i odwrotnie.

%prep
%setup -q -n mpeg2

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	USE_DISP=-DDISPLAY \
	LIBS="-lXext -lX11" \
	USE_SHMEM=-DSH_MEM \
	INCLUDEDIR= \
	LIBRARYDIR=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/mpeg2dec/mpeg2decode $RPM_BUILD_ROOT%{_bindir}
install src/mpeg2enc/mpeg2encode $RPM_BUILD_ROOT%{_bindir}

for f in CHANGES TODO ; do
	mv -f src/mpeg2dec/$f{,.mpeg2dec}
	mv -f src/mpeg2enc/$f{,.mpeg2enc}
done
mv -f src/mpeg2dec/README{,.mpeg2dec}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/* src/*/CHANGES* src/*/TODO*
%doc src/mpeg2dec/{EXAMPLES,IEEE1180,README*,SPATIAL.DOC}
%attr(755,root,root) %{_bindir}/*
