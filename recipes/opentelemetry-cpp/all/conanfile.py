from conans import ConanFile, CMake, tools
import os


class OpentelemetryCppConan(ConanFile):
    name = "opentelemetry-cpp"
    version = "0.0.1"
    license = "Apache-2.0 License"
    author = "Ben-A. Altendorf" "b.altendorf@tritime.org"
    url = "https://github.com/baltendorf/conan-center-index"
    description = "Cpp implementation of OpenTelemetry"
    topics = ("opentelemetry", "metrics", "tracing")
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
        self.run("git clone -b test/cmake_install https://github.com/baltendorf/opentelemetry-cpp.git")
        os.rename(self.name, self._source_subfolder)

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake

        self._cmake = CMake(self)
        self._cmake.definitions["WITH_TESTS"] = False
        self._cmake.definitions["WITH_EXAMPLES"] = False

        self._cmake.configure(source_folder=self._source_subfolder)
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

