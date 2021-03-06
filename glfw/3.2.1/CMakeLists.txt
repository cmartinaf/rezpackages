CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(glfw_version $ENV{REZ_BUILD_PROJECT_VERSION})

rez_set_archive(
    url_glfw glfw/glfw-${glfw_version}.tar.gz
    https://github.com/glfw/glfw/archive/${glfw_version}.tar.gz
    
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT} VERBOSE=1)

if(${REZ_BUILD_INSTALL})
    set(install_cmd make install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    glfw
    URL ${url_glfw}
    PREFIX glfw        
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX} 
               -DCMAKE_POSITION_INDEPENDENT_CODE=ON
               -DBUILD_SHARED_LIBS=OFF
               -DBUILD_TESTS=OFF
               -DBUILD_DOCS=OFF
)

