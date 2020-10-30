from conans import ConanFile, CMake, tools
import os


class OpentracingCppConan(ConanFile):
    name = "opentracing-cpp"
    version = "1.6.0"
    license = "Apache-2.0"
    author = "Ben-A. Altendorf" "b.altendorf@tritime.org"
    url = "https://github.com/baltendorf/conan-center-index"
    description = "Cpp implementation of Opentracing"
    topics = ("opentracing", "metrics", "tracing")
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = ["CMakeLists.txt"]
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    _cmake = None

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
        self.run("git clone -b v1.6.0 https://github.com/opentracing/opentracing-cpp.git")
        os.rename(self.name, self._source_subfolder)

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake

        self._cmake = CMake(self)
        self._cmake.definitions["BUILD_SHARED_LIBS"] = False
        self._cmake.definitions["BUILD_STATIC_LIBS"] = True
        self._cmake.definitions["BUILD_MOCKTRACER"] = False
        self._cmake.definitions["BUILD_DYNAMIC_LOADING"] = False
        self._cmake.definitions["BUILD_TESTING"] = False


        self._cmake.configure(source_folder=self._source_subfolder)
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy("LICENSE", src=self._source_subfolder, dst="licenses")
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

