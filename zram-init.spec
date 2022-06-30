Summary:	Init and set up swap device in /dev/zram0
Name:		zram-init
Version:	11.1
Release:	3
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
	BINDIR=%{buildroot}%{_bindir} \
	MODPROBEDIR=%{buildroot}%{_modprobedir} \
	SYSTEMDDIR=%{buildroot}%{_unitdir}

rm -fv %{buildroot}/etc/conf.d/zram-init
rm -fv %{buildroot}/etc/init.d/zram-init

%find_lang %{name}

%files -f %{name}.lang
%{_modprobedir}/zram.conf
%{_unitdir}/*.service
%{_bindir}/zram-init
%doc %{_mandir}/de/man8/zram-init.8.*
%doc %{_mandir}/man8/zram-init.8.*
%{_datadir}/zsh/site-functions/_zram-init
