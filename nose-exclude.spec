#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nose-exclude
Version  : 0.4.1
Release  : 10
URL      : https://github.com/kgrandis/nose-exclude/archive/0.4.1.tar.gz
Source0  : https://github.com/kgrandis/nose-exclude/archive/0.4.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: nose-exclude-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
Overview
========
nose-exclude is a `Nose`_ plugin that allows you to easily specify
directories to be excluded from testing.

%package python
Summary: python components for the nose-exclude package.
Group: Default

%description python
python components for the nose-exclude package.


%prep
%setup -q -n nose-exclude-0.4.1

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
