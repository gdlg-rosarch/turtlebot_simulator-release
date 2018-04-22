# Script generated with Bloom
pkgdesc="ROS - Gazebo launchers and worlds for TurtleBot simulation"
url='http://ros.org/wiki/turtlebot_gazebo'

pkgname='ros-kinetic-turtlebot-gazebo'
pkgver='2.2.3_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-depthimage-to-laserscan'
'ros-kinetic-diagnostic-aggregator'
'ros-kinetic-gazebo-ros'
'ros-kinetic-kobuki-gazebo-plugins'
'ros-kinetic-robot-pose-ekf'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-turtlebot-bringup'
'ros-kinetic-turtlebot-description'
'ros-kinetic-turtlebot-navigation'
'ros-kinetic-xacro'
'ros-kinetic-yocs-cmd-vel-mux'
)

conflicts=()
replaces=()

_dir=turtlebot_gazebo
source=()
md5sums=()

prepare() {
    cp -R $startdir/turtlebot_gazebo $srcdir/turtlebot_gazebo
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

