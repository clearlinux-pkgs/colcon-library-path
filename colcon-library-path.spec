#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-library-path
Version  : 0.2.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/5e/3d/b9778bdb0150e4202a476f707db740adf7d080010fceeb66235bf9ad4acf/colcon-library-path-0.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5e/3d/b9778bdb0150e4202a476f707db740adf7d080010fceeb66235bf9ad4acf/colcon-library-path-0.2.0.tar.gz
Summary  : Extension for colcon adding an environment variable to find libraries.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-library-path-python3
Requires: colcon-library-path-python
Requires: colcon-core
BuildRequires : buildreq-distutils3

%description
===================

%package python
Summary: python components for the colcon-library-path package.
Group: Default
Requires: colcon-library-path-python3

%description python
python components for the colcon-library-path package.


%package python3
Summary: python3 components for the colcon-library-path package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-library-path package.


%prep
%setup -q -n colcon-library-path-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533002514
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
