Name:           python-box
Version:        3.4.1
Release:        1%{?dist}
Summary:        Python dictionaries with advanced dot notation access

License:        MIT
URL:            https://github.com/cdgriffith/Box
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/cdgriffith/Box/%{version}/LICENSE
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
# The license file is not included in the source tarballs
# https://github.com/cdgriffith/Box/issues/92
cp -p %{SOURCE1} .

# Make sure we don't have ambiguous python shebangs
# https://fedoraproject.org/wiki/Changes/Make_ambiguous_python_shebangs_error
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" .

%build
%py3_build

%install
%py3_install

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
