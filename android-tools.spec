# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       android-tools

# >> macros
# << macros

Summary:    Minimal set of android tools
Version:    4.2.2_git20130218
Release:    3
Group:      Tools
License:    Apache 2.0
Source0:    android-tools-4.2.2_git20130218.tar.gz
Source1:    adb.mk
Source2:    fastboot.mk
Source100:  android-tools.yaml
Patch0:     0001-Ignore-selinux-android.h.patch
Patch1:     0002-Original-split_bootimg.pl-from-http-www.enck.org-too.patch
Patch2:     0003-Provide-command-line-to-use-mkbootimg-to-recreate-th.patch
Patch3:     0004-Add-mer-android-chroot-to-enter-the-ubu-chroot-from-.patch
BuildRequires:  pkgconfig(openssl)
BuildRequires:  libselinux-devel
BuildRequires:  python
BuildRequires:  zlib

%description
android-tools for Mer

The upstream tarball is based of these upstream Android git repos:
  git clone https://android.googlesource.com/platform/system/core
  git clone https://android.googlesource.com/platform/system/extras

with unneeded files removed.

Based on Debian android-tools package


%prep
%setup -q -n src

# 0001-Ignore-selinux-android.h.patch
%patch0 -p1
# 0002-Original-split_bootimg.pl-from-http-www.enck.org-too.patch
%patch1 -p1
# 0003-Provide-command-line-to-use-mkbootimg-to-recreate-th.patch
%patch2 -p1
# 0004-Add-mer-android-chroot-to-enter-the-ubu-chroot-from-.patch
%patch3 -p1
# >> setup
cp %{SOURCE1} .
cp %{SOURCE2} .
# << setup

%build
# >> build pre
make -f `pwd`/adb.mk -C core/adb
make -f `pwd`/fastboot.mk -C core/fastboot
#make -f `pwd`/ext4_utils.mk -C extras/ext4_utils
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
install -D -m 755  core/adb/adb %{buildroot}%{_bindir}/adb
install -D -m 755  core/fastboot/fastboot %{buildroot}%{_bindir}/fastboot
install -D -m 755  split_bootimg.pl %{buildroot}%{_bindir}/split_bootimg
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_bindir}/adb
%{_bindir}/fastboot
%{_bindir}/split_bootimg
# >> files
# << files
