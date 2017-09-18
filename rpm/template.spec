Name:           ros-indigo-turtlebot-simulator
Version:        2.2.3
Release:        0%{?dist}
Summary:        ROS turtlebot_simulator package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/turtlebot_simulator
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-turtlebot-gazebo
Requires:       ros-indigo-turtlebot-stage
Requires:       ros-indigo-turtlebot-stdr
BuildRequires:  ros-indigo-catkin

%description
Catkin metapackage for the turtlebot_simulator stack

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Sep 18 2017 OSRF <turtlebot@osrfoundation.com> - 2.2.3-0
- Autogenerated by Bloom

* Wed Sep 16 2015 OSRF <turtlebot@osrfoundation.com> - 2.2.2-0
- Autogenerated by Bloom

* Wed Sep 16 2015 OSRF <turtlebot@osrfoundation.com> - 2.2.1-1
- Autogenerated by Bloom

* Fri Aug 07 2015 OSRF <turtlebot@osrfoundation.com> - 2.2.1-0
- Autogenerated by Bloom

* Tue Dec 30 2014 OSRF <turtlebot@osrfoundation.com> - 2.2.0-0
- Autogenerated by Bloom

