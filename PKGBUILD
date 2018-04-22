# Script generated with Bloom
pkgdesc="ROS - Stdr version of turtlebot simulation. Convenient to test 2D-navigation related stuffs"
url='http://wiki.ros.org/turtlebot_stdr'

pkgname='ros-kinetic-turtlebot-stdr'
pkgver='2.2.3_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-navigation'
'ros-kinetic-stdr-gui'
'ros-kinetic-stdr-resources'
'ros-kinetic-stdr-robot'
'ros-kinetic-stdr-server'
'ros-kinetic-turtlebot-bringup'
'ros-kinetic-turtlebot-navigation'
'ros-kinetic-yocs-velocity-smoother'
'ros-kinetic-yocs-virtual-sensor'
)

conflicts=()
replaces=()

_dir=turtlebot_stdr
source=()
md5sums=()

prepare() {
    cp -R $startdir/turtlebot_stdr $srcdir/turtlebot_stdr
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

