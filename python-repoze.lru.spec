#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	repoze.lru
Summary:	A tiny LRU cache implementation and decorator
Summary(pl.UTF-8):	Mała implementacja pamięci podręcznej LRU z dekoratorem
Name:		python-%{module}
Version:	0.7
Release:	3
License:	BSD-derived (http://www.repoze.org/LICENSE.txt)
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/r/repoze.lru/repoze.lru-%{version}.tar.gz
# Source0-md5:	c08cc030387e0b1fc53c5c7d964b35e2
URL:		https://pypi.org/project/repoze.lru/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-coverage
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-coverage
BuildRequires:	python3-nose
%endif
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

%package -n python3-%{module}
Summary:	A tiny LRU cache implementation and decorator
Summary(pl.UTF-8):	Mała implementacja pamięci podręcznej LRU z dekoratorem
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
repoze.lru is a LRU (least recently used) cache implementation. Keys
and values that are not used frequently will be evicted from the cache
faster than keys and values that are used frequently.

%description -n python3-%{module} -l pl.UTF-8
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
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/repoze/lru/tests.py*
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/repoze/lru/tests.py
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/repoze/lru/__pycache__/tests.*.py*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc COPYRIGHT.txt LICENSE.txt README.rst
# XXX: shared with repoze.*
%dir %{py_sitescriptdir}/repoze
%{py_sitescriptdir}/repoze/lru
%{py_sitescriptdir}/repoze.lru-%{version}-py*-nspkg.pth
%{py_sitescriptdir}/repoze.lru-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc COPYRIGHT.txt LICENSE.txt README.rst
# XXX: shared with repoze.*
%dir %{py3_sitescriptdir}/repoze
%{py3_sitescriptdir}/repoze/lru
%{py3_sitescriptdir}/repoze.lru-%{version}-py*-nspkg.pth
%{py3_sitescriptdir}/repoze.lru-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
