#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module	repoze.lru
Summary:	A tiny LRU cache implementation and decorator
Name:		python-%{module}
Version:	0.6
Release:	2
License:	BSD-derived (http://www.repoze.org/LICENSE.txt)
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/r/repoze.lru/repoze.lru-%{version}.tar.gz
# Source0-md5:	2c3b64b17a8e18b405f55d46173e14dd
URL:		http://pypi.python.org/pypi/repoze.lru
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
repoze.lru is a LRU (least recently used) cache implementation. Keys
and values that are not used frequently will be evicted from the cache
faster than keys and values that are used frequently.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/repoze/lru/tests.py*

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt
%dir %{py_sitescriptdir}/repoze/
%dir %{py_sitescriptdir}/repoze/lru
%{py_sitescriptdir}/repoze/lru/*.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*-nspkg.pth
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
