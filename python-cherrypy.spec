%global debug_package %{nil}

Name: python-cherrypy
Epoch: 100
Version: 18.6.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Object-Oriented HTTP framework
License: BSD-3-Clause
URL: https://github.com/cherrypy/cherrypy/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
CherryPy allows developers to build web applications in much the same
way they would build any other object-oriented Python program. This
usually results in smaller source code developed in less time.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-CherryPy
Summary: Object-Oriented HTTP framework
Requires: python3
Requires: python3-cheroot >= 8.2.1
Requires: python3-jaraco.collections
Requires: python3-more-itertools
Requires: python3-portend >= 2.1.1
Requires: python3-zc.lockfile
Provides: python3-cherrypy = %{epoch}:%{version}-%{release}
Provides: python3dist(cherrypy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cherrypy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cherrypy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cherrypy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cherrypy) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-CherryPy
CherryPy allows developers to build web applications in much the same
way they would build any other object-oriented Python program. This
usually results in smaller source code developed in less time.

%files -n python%{python3_version_nodots}-CherryPy
%license LICENSE.md
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-CherryPy
Summary: Object-Oriented HTTP framework
Requires: python3
Requires: python3-cheroot >= 8.2.1
Requires: python3-jaraco.collections
Requires: python3-more-itertools
Requires: python3-portend >= 2.1.1
Requires: python3-zc.lockfile
Provides: python3-cherrypy = %{epoch}:%{version}-%{release}
Provides: python3dist(cherrypy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cherrypy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cherrypy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cherrypy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cherrypy) = %{epoch}:%{version}-%{release}

%description -n python3-CherryPy
CherryPy allows developers to build web applications in much the same
way they would build any other object-oriented Python program. This
usually results in smaller source code developed in less time.

%files -n python3-CherryPy
%license LICENSE.md
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-cherrypy
Summary: Object-Oriented HTTP framework
Requires: python3
Requires: python3-cheroot >= 8.2.1
Requires: python3-jaraco-collections
Requires: python3-more-itertools
Requires: python3-portend >= 2.1.1
Requires: python3-zc-lockfile
Provides: python3-cherrypy = %{epoch}:%{version}-%{release}
Provides: python3dist(cherrypy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-cherrypy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(cherrypy) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-cherrypy = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(cherrypy) = %{epoch}:%{version}-%{release}

%description -n python3-cherrypy
Click is a Python package for creating command line interfaces in a
composable way with as little code as necessary. It's the "Command Line
Interface Creation Kit". It is configurable, and comes with defaults out
of the box.

%files -n python3-cherrypy
%license LICENSE.md
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
