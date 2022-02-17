Name:		zram-init
Version:	11.1
Release:	1

Summary:	Init and set up swap device in /dev/zram0
License:	GPL
Group:		System/Base
BuildArch:	noarch
Source0:	https://github.com/vaeth/zram-init/archive/v%{version}.zip


%description
A wrapper script for the zram kernel module with interactive and init support

%prep
%autosetup -p1

%install
%make_install \
	PREFIX=%{_prefix} \
	SYSCONFDIR=%{_sysconfdir} \
	BINDIR=%{buildroot}/sbin \
	SYSTEMDDIR=%{buildroot}%{_unitdir}

rm -fv %{buildroot}/etc/conf.d/zram-init
rm -fv %{buildroot}/etc/init.d/zram-init

%find_lang %{name}

%files -f %{name}.lang
/etc/modprobe.d/zram.conf
%{_unitdir}/zram_btrfs.service
%{_unitdir}/zram_swap.service
%{_unitdir}/zram_tmp.service
%{_unitdir}/zram_var_tmp.service
/sbin/zram-init
%{_mandir}/de/man8/zram-init.8.*
%{_mandir}/man8/zram-init.8.*
%{_datadir}/zsh/site-functions/_zram-init
