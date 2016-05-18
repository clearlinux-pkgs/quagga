#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : quagga
Version  : 1.0.20160315
Release  : 5
URL      : http://download.savannah.gnu.org/releases/quagga/quagga-1.0.20160315.tar.gz
Source0  : http://download.savannah.gnu.org/releases/quagga/quagga-1.0.20160315.tar.gz
Summary  : Routing daemon
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.0
Requires: quagga-bin
Requires: quagga-lib
Requires: quagga-doc
BuildRequires : libcap-dev
BuildRequires : ncurses-dev
BuildRequires : readline-dev
BuildRequires : sed
BuildRequires : texinfo

%description
Quagga is a free software that manages TCP/IP based routing
protocol. It takes multi-server and multi-thread approach to resolve
the current complexity of the Internet.

Quagga supports BGP4, OSPFv2, OSPFv3, ISIS, RIP, RIPng and PIM.

Quagga is intended to be used as a Route Server and a Route Reflector. It is
not a toolkit, it provides full routing power under a new architecture.
Quagga by design has a process for each protocol.

Quagga is a fork of GNU Zebra.

%package bin
Summary: bin components for the quagga package.
Group: Binaries

%description bin
bin components for the quagga package.


%package dev
Summary: dev components for the quagga package.
Group: Development
Requires: quagga-lib
Requires: quagga-bin
Provides: quagga-devel

%description dev
dev components for the quagga package.


%package doc
Summary: doc components for the quagga package.
Group: Documentation

%description doc
doc components for the quagga package.


%package lib
Summary: lib components for the quagga package.
Group: Libraries

%description lib
lib components for the quagga package.


%prep
%setup -q -n quagga-1.0.20160315

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bgp_btoa
/usr/bin/bgpd
/usr/bin/isisd
/usr/bin/ospf6d
/usr/bin/ospfclient
/usr/bin/ospfd
/usr/bin/pimd
/usr/bin/ripd
/usr/bin/ripngd
/usr/bin/test_igmpv3_join
/usr/bin/vtysh
/usr/bin/watchquagga
/usr/bin/zebra

%files dev
%defattr(-,root,root,-)
/usr/include/quagga/buffer.h
/usr/include/quagga/checksum.h
/usr/include/quagga/command.h
/usr/include/quagga/distribute.h
/usr/include/quagga/fifo.h
/usr/include/quagga/filter.h
/usr/include/quagga/getopt.h
/usr/include/quagga/hash.h
/usr/include/quagga/if.h
/usr/include/quagga/if_rmap.h
/usr/include/quagga/jhash.h
/usr/include/quagga/keychain.h
/usr/include/quagga/libospf.h
/usr/include/quagga/linklist.h
/usr/include/quagga/log.h
/usr/include/quagga/md5.h
/usr/include/quagga/memory.h
/usr/include/quagga/memtypes.h
/usr/include/quagga/network.h
/usr/include/quagga/ospfapi/ospf_apiclient.h
/usr/include/quagga/ospfd/ospf_api.h
/usr/include/quagga/ospfd/ospf_asbr.h
/usr/include/quagga/ospfd/ospf_dump.h
/usr/include/quagga/ospfd/ospf_ism.h
/usr/include/quagga/ospfd/ospf_lsa.h
/usr/include/quagga/ospfd/ospf_lsdb.h
/usr/include/quagga/ospfd/ospf_nsm.h
/usr/include/quagga/ospfd/ospf_opaque.h
/usr/include/quagga/ospfd/ospfd.h
/usr/include/quagga/plist.h
/usr/include/quagga/pqueue.h
/usr/include/quagga/prefix.h
/usr/include/quagga/privs.h
/usr/include/quagga/route_types.h
/usr/include/quagga/routemap.h
/usr/include/quagga/sigevent.h
/usr/include/quagga/smux.h
/usr/include/quagga/sockopt.h
/usr/include/quagga/sockunion.h
/usr/include/quagga/str.h
/usr/include/quagga/stream.h
/usr/include/quagga/table.h
/usr/include/quagga/thread.h
/usr/include/quagga/vector.h
/usr/include/quagga/version.h
/usr/include/quagga/vrf.h
/usr/include/quagga/vty.h
/usr/include/quagga/workqueue.h
/usr/include/quagga/zassert.h
/usr/include/quagga/zclient.h
/usr/include/quagga/zebra.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
