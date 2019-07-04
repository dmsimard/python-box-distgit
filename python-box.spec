%global srcname python-box

Name:           %{srcname}
Version:        3.4.1
Release:        1%{?dist}
Summary:        Python dictionaries with advanced dot notation access.

License:        MIT
URL:            https://github.com/cdgriffith/Box
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/cdgriffith/Box/master/LICENSE

BuildArch:      noarch

%description
%{summary}

%package -n python3-box
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest-runner
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-box
%{summary}

%prep
%autosetup -n %{srcname}-%{version}
# The license file is not included in the source tarballs
cp -p %{SOURCE1} .

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