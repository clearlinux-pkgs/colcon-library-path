#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-library-path
Version  : 0.2.1
Release  : 10
URL      : https://files.pythonhosted.org/packages/7a/72/1427af79ac1265103b58ff6fbacd75d325f590ec0e3c1c98027ebd1fff12/colcon-library-path-0.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/7a/72/1427af79ac1265103b58ff6fbacd75d325f590ec0e3c1c98027ebd1fff12/colcon-library-path-0.2.1.tar.gz
Summary  : Extension for colcon adding an environment variable to find libraries.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-library-path-python = %{version}-%{release}
Requires: colcon-library-path-python3 = %{version}-%{release}
Requires: colcon-core
BuildRequires : buildreq-distutils3
BuildRequires : colcon-core

%description
===================

%package python
Summary: python components for the colcon-library-path package.
Group: Default
Requires: colcon-library-path-python3 = %{version}-%{release}

%description python
python components for the colcon-library-path package.


%package python3
Summary: python3 components for the colcon-library-path package.
Group: Default
Requires: python3-core
Provides: pypi(colcon_library_path)
Requires: pypi(colcon_core)

%description python3
python3 components for the colcon-library-path package.


%prep
%setup -q -n colcon-library-path-0.2.1
cd %{_builddir}/colcon-library-path-0.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583527815
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
