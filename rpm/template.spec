Name:           ros-indigo-turtlebot-stage
Version:        2.2.1
Release:        1%{?dist}
Summary:        ROS turtlebot_stage package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/turtlebot_stage
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-navigation
Requires:       ros-indigo-stage-ros
Requires:       ros-indigo-turtlebot-bringup
Requires:       ros-indigo-turtlebot-navigation
Requires:       ros-indigo-yocs-velocity-smoother
Requires:       ros-indigo-yocs-virtual-sensor
BuildRequires:  ros-indigo-catkin

%description
Stage version of turtlebot simulation. Convenient to test 2D-navigation related
stuffs

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
* Wed Sep 16 2015 Jihoon Lee <jihoonl@yujinrobot.com> - 2.2.1-1
- Autogenerated by Bloom

* Fri Aug 07 2015 Jihoon Lee <jihoonl@yujinrobot.com> - 2.2.1-0
- Autogenerated by Bloom

* Tue Dec 30 2014 Jihoon Lee <jihoonl@yujinrobot.com> - 2.2.0-0
- Autogenerated by Bloom

