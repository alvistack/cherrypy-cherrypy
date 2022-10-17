# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-cherrypy
Epoch: 100
Version: 18.7.0
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
CherryPy allows developers to build web applications in much the same
way they would build any other object-oriented Python program. This
usually results in smaller source code developed in less time.

%files -n python3-cherrypy
%license LICENSE.md
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
