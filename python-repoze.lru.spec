#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define 	module	repoze.lru
Summary:	A tiny LRU cache implementation and decorator
Summary(pl.UTF-8):	Mała implementacja pamięci podręcznej LRU z dekoratorem
Name:		python-%{module}
Version:	0.7
Release:	1
License:	BSD-derived (http://www.repoze.org/LICENSE.txt)
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/r/repoze.lru/repoze.lru-%{version}.tar.gz
# Source0-md5:	c08cc030387e0b1fc53c5c7d964b35e2
URL:		https://pypi.org/project/repoze.lru/
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-coverage
BuildRequires:	python-nose
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
repoze.lru is a LRU (least recently used) cache implementation. Keys
and values that are not used frequently will be evicted from the cache
faster than keys and values that are used frequently.

%description -l pl.UTF-8
repoze.lru to implementacja pamięci podręcznej LRU (least recently
used - z zastępowaniem najdawniej używanych elementów). Klucze i
wartości rzadziej używane będą usuwane z pamięci podręcznej szybciej,
niż klucze i wartości używane częściej.

%package apidocs
Summary:	API documentation for Python repoze.lru module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona repoze.lru
Group:		Documentation

%description apidocs
API documentation for Python repoze.lru module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona repoze.lru.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build %{?with_tests:test}

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/repoze/lru/tests.py*

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT.txt LICENSE.txt README.rst
# XXX: shared with repoze.*
%dir %{py_sitescriptdir}/repoze
%dir %{py_sitescriptdir}/repoze/lru
%{py_sitescriptdir}/repoze/lru/*.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*-nspkg.pth
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
