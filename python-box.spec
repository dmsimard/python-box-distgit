Name:           python-box
Version:        3.4.2
Release:        1%{?dist}
Summary:        Python dictionaries with advanced dot notation access

License:        MIT
URL:            https://github.com/cdgriffith/Box
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires: /usr/bin/pathfix.py

%description
%{summary}

%package -n python3-box
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest-runner
%{?python_provide:%python_provide python3-box}

%description -n python3-box
%{summary}

%prep
%autosetup -n python-box-%{version}

%build
%py3_build

%install
%py3_install

# Make sure we don't have ambiguous python shebangs in bindir
# https://fedoraproject.org/wiki/Changes/Make_ambiguous_python_shebangs_error
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_bindir}/box.py

# Otherwise remove the shebang from site-packages
sed -i "\%#!/usr/bin/env python%d" %{buildroot}%{python3_sitelib}/box.py

%files -n python3-box
%license LICENSE
%doc README.rst
%{_bindir}/box.py
%{python3_sitelib}/box.py
%{python3_sitelib}/python_box-*.egg-info/
%{python3_sitelib}/__pycache__/*

%changelog
* Fri Jul 5 2019 David Moreau Simard <dmsimard@redhat.com> - 3.4.1-1
- First version of the package
