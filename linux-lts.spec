#
# This is a special configuration of the Linux kernel, based on linux package
# for long-term support
#

Name:           linux-lts
Version:        4.4.15
# Sync Version  4.6.4  # Latest version syncted with linux (-native) package
Release:        10
# Sync Release  245    # Latest release syncted with linux (-native) package
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v4.x/linux-4.4.15.tar.xz
Source1:        config
Source2:        cmdline

%define kversion %{version}-%{release}.lts

BuildRequires:  bash >= 2.03
BuildRequires:  bc
BuildRequires:  binutils-dev
BuildRequires:  elfutils-dev
BuildRequires:  kmod
BuildRequires:  make >= 3.78
BuildRequires:  openssl-dev
BuildRequires:  flex
BuildRequires:  bison

# don't srip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

# Serie    00XX: mainline, CVE, bugfixes patches
Patch0001: 0001-crypto-testmgr-Add-a-flag-allowing-the-self-tests-to.patch
Patch0002: cve-2016-4440.patch
Patch0003: cve-2016-4470.patch
Patch0004: cve-2016-5829.patch
Patch0005: cve-2016-5828.nopatch
Patch0006: cve-2016-5243.patch
Patch0007: cve-2016-5244.patch
Patch0008: cve-2016-1237_requires.patch
Patch0009: cve-2016-1237.patch

# Serie    01XX: Clear Linux patches
#Patch0101: 0101-init-don-t-wait-for-PS-2-at-boot.patch
#Patch0102: 0102-sched-tweak-the-scheduler-to-favor-CPU-0.patch
Patch0103: 0103-kvm-silence-kvm-unhandled-rdmsr.patch
Patch0104: 0104-i8042-decrease-debug-message-level-to-info.patch
Patch0105: 0105-net-tcp-reduce-minimal-ack-time-down-from-40-msec.patch
Patch0106: 0106-init-do_mounts-recreate-dev-root.patch
Patch0107: 0107-Increase-the-ext4-default-commit-age.patch
Patch0108: 0108-silence-rapl.patch
Patch0109: 0109-pci-pme-wakeups.patch
Patch0110: 0110-ksm-wakeups.patch
Patch0111: 0111-intel_idle-tweak-cpuidle-cstates.patch
Patch0112: 0112-xattr-allow-setting-user.-attributes-on-symlinks-by-.patch
Patch0113: 0113-init_task-faster-timerslack.patch
Patch0114: 0114-KVM-x86-Add-hypercall-KVM_HC_RETURN_MEM.patch
Patch0115: 0115-fs-ext4-fsync-optimize-double-fsync-a-bunch.patch
Patch0116: 0116-overload-on-wakeup.patch
Patch0117: 0117-bootstats-add-printk-s-to-measure-boot-time-in-more-.patch
Patch0118: 0118-fix-initcall-timestamps.patch
Patch0119: 0119-smpboot-reuse-timer-calibration.patch
Patch0120: 0120-raid6-add-Kconfig-option-to-skip-raid6-benchmarking.patch
Patch0121: 0121-Initialize-ata-before-graphics.patch
Patch0122: 0122-reduce-e1000e-boot-time-by-tightening-sleep-ranges.patch
Patch0123: 0123-xor-skip-benchmark-allocations-for-short-circuit-pat.patch
Patch0124: 0124-input-i8042-Fix-console-keyboard-support-on-Gen2-Hyp.patch

# Serie    XYYY: Extra features modules
# AUFS
Patch1001: 1001-aufs-kbuild.patch
Patch1002: 1002-aufs-base.patch
Patch1003: 1003-aufs-mmap.patch
Patch1004: 1004-aufs-standalone.patch
Patch1005: 1005-aufs-driver-and-docs.patch

# DPDK 16.04 integration
Patch2001: 2001-dpdk-add-source-files.patch
Patch2002: 2002-dpdk-Integrate-Kconfig-and-Makefiles.patch

# virtualbox modules
Patch3001: 3001-virtualbox-add-module-sources.patch
Patch3002: 3002-virtualbox-add-Kconfs-and-Makefiles.patch

# 4.6 sata backports
Patch4001: 4001-libata-support-AHCI-on-OCTEON-platform.patch
Patch4002: 4002-libata-fix-unbalanced-spin_lock_irqsave-spin_unlock_.patch
Patch4003: 4003-ata-ahci_mvebu-add-support-for-Armada-3700-variant.patch
Patch4004: 4004-block-Add-blk_set_runtime_active.patch
Patch4005: 4005-scsi-Set-request-queue-runtime-PM-status-back-to-act.patch
Patch4006: 4006-scsi-Drop-runtime-PM-usage-count-after-host-is-added.patch
Patch4007: 4007-ahci-Cache-host-controller-version.patch
Patch4008: 4008-ahci-Convert-driver-to-use-modern-PM-hooks.patch
Patch4009: 4009-ahci-Add-functions-to-manage-runtime-PM-of-AHCI-port.patch
Patch4010: 4010-ahci-Add-runtime-PM-support-for-the-host-controller.patch

# Extra backported features
Patch5001: 5001-uvc-driver-Add-support-for-F200-color-formats.patch
Patch5002: 5002-uvc-driver-Add-support-for-R200-color-formats.patch

%description
The Linux kernel.

%package extra
License:        GPL-2.0
Summary:        The Linux kernel extra files
Group:          kernel

%description extra
Linux kernel extra files

%package vboxguest-modules
License:        GPL-2.0
Summary:        Oracle VirtualBox guest additions modules
Group:          kernel

%description vboxguest-modules
Oracle VirtualBox guest additions modules

%prep
%setup -q -n linux-4.4.15

# Serie    00XX: mainline, CVE, bugfixes patches
%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
#%patch0005 -p1 # # No x86 arch
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1

# Serie    01XX: Clear Linux patches
#%patch0101 -p1
#%patch0102 -p1
%patch0103 -p1
%patch0104 -p1
%patch0105 -p1
%patch0106 -p1
%patch0107 -p1
%patch0108 -p1
%patch0109 -p1
%patch0110 -p1
%patch0111 -p1
%patch0112 -p1
%patch0113 -p1
%patch0114 -p1
%patch0115 -p1
%patch0116 -p1
%patch0117 -p1
%patch0118 -p1
%patch0119 -p1
%patch0120 -p1
%patch0121 -p1
%patch0122 -p1
%patch0123 -p1
%patch0124 -p1

# Serie    XYYY: Extra features modules
# AUFS
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1

# DPDK 16.04 integration
%patch2001 -p1
%patch2002 -p1

# virtualbox modules
%patch3001 -p1
%patch3002 -p1

# sata PM backports
%patch4001 -p1
%patch4002 -p1
%patch4003 -p1
%patch4004 -p1
%patch4005 -p1
%patch4006 -p1
%patch4007 -p1
%patch4008 -p1
%patch4009 -p1
%patch4010 -p1

# Extra backported features
%patch5001 -p1
%patch5002 -p1

cp %{SOURCE1} .

%build
BuildKernel() {
    MakeTarget=$1

    Arch=x86_64
    ExtraVer="-%{release}.lts"

    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = ${ExtraVer}/" Makefile

    make -s mrproper
    cp config .config

    make -s ARCH=$Arch oldconfig > /dev/null
    make -s CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} ARCH=$Arch $MakeTarget %{?sparse_mflags}
    make -s CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} ARCH=$Arch modules %{?sparse_mflags} || exit 1
}

BuildKernel bzImage

%install

InstallKernel() {
    KernelImage=$1

    Arch=x86_64
    KernelVer=%{kversion}
    KernelDir=%{buildroot}/usr/lib/kernel

    mkdir   -p ${KernelDir}
    install -m 644 .config    ${KernelDir}/config-${KernelVer}
    install -m 644 System.map ${KernelDir}/System.map-${KernelVer}
    install -m 644 %{SOURCE2} ${KernelDir}/cmdline-${KernelVer}
    cp  $KernelImage ${KernelDir}/org.clearlinux.lts.%{version}-%{release}
    chmod 755 ${KernelDir}/org.clearlinux.lts.%{version}-%{release}

    mkdir -p %{buildroot}/usr/lib/modules/$KernelVer
    make -s ARCH=$Arch INSTALL_MOD_PATH=%{buildroot}/usr modules_install KERNELRELEASE=$KernelVer

    rm -f %{buildroot}/usr/lib/modules/$KernelVer/build
    rm -f %{buildroot}/usr/lib/modules/$KernelVer/source
}

InstallKernel arch/x86/boot/bzImage

rm -rf %{buildroot}/usr/lib/firmware

# Erase some modules index and then re-crate them
for i in alias ccwmap dep ieee1394map inputmap isapnpmap ofmap pcimap seriomap symbols usbmap softdep devname
do
    rm -f %{buildroot}/usr/lib/modules/%{kversion}/modules.${i}*
done
rm -f %{buildroot}/usr/lib/modules/%{kversion}/modules.*.bin

# Recreate modules indices
depmod -a -b %{buildroot}/usr %{kversion}

ln -s org.clearlinux.lts.%{version}-%{release} %{buildroot}/usr/lib/kernel/default-lts

%files
%dir /usr/lib/kernel
%exclude  /usr/lib/modules/%{kversion}/kernel/arch/x86/virtualbox/
%dir /usr/lib/modules/%{kversion}
/usr/lib/kernel/config-%{kversion}
/usr/lib/kernel/cmdline-%{kversion}
/usr/lib/kernel/org.clearlinux.lts.%{version}-%{release}
/usr/lib/kernel/default-lts
/usr/lib/modules/%{kversion}/kernel
/usr/lib/modules/%{kversion}/modules.*

%files extra
%dir /usr/lib/kernel
/usr/lib/kernel/System.map-%{kversion}

%files vboxguest-modules
/usr/lib/modules/%{kversion}/kernel/arch/x86/virtualbox/
