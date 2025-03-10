#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	UK Postcode parser
Summary(pl.UTF-8):	Analizator kodów pocztowych Wielkiej Brytanii
Name:		python-ukpostcodeparser
Version:	1.1.2
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/UkPostcodeParser/
Source0:	https://files.pythonhosted.org/packages/source/U/UkPostcodeParser/UkPostcodeParser-%{version}.tar.gz
# Source0-md5:	763ed9144915f9647fa5bded2f03ae75
Patch0:		UkPostcodeParser-tests.patch
URL:		https://pypi.org/project/UkPostcodeParser/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UK Postcode parser.

%description -l pl.UTF-8
Analizator kodów pocztowych Wielkiej Brytanii.

%package -n python3-ukpostcodeparser
Summary:	UK Postcode parser
Summary(pl.UTF-8):	Analizator kodów pocztowych Wielkiej Brytanii
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-ukpostcodeparser
UK Postcode parser.

%description -n python3-ukpostcodeparser -l pl.UTF-8
Analizator kodów pocztowych Wielkiej Brytanii.

%prep
%setup -q -n UkPostcodeParser-%{version}
%patch -P 0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m unittest ukpostcodeparser.test.parser
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m unittest ukpostcodeparser.test.parser
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/ukpostcodeparser/test
%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/ukpostcodeparser/test
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README
%{py_sitescriptdir}/ukpostcodeparser
%{py_sitescriptdir}/UkPostcodeParser-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-ukpostcodeparser
%defattr(644,root,root,755)
%doc LICENSE README
%{py3_sitescriptdir}/ukpostcodeparser
%{py3_sitescriptdir}/UkPostcodeParser-%{version}-py*.egg-info
%endif
