from conans import ConanFile, CMake, tools
import os


class OpentracingCppConan(ConanFile):
    name = "opentracing-cpp"
<<<<<<< HEAD
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
=======
    description = "C++ implementation of the OpenTracing API"
    url = "https://github.com/baltendorf/conan-center-index"
    homepage = "https://opentracing.io"
    exports_sources = ["CMakeLists.txt"]
    license = "Apache-2.0"
    topics = ("opentracing", "metrics", "tracing")
    generators = "cmake"
    
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "static": [True, False],
        "build_mocktracer": [True, False],
        "build_dynamic_loading": [True, False],
        "build_testing": [True, False]
        }
    default_options = {
        "shared": False,
        "static": True,
        "build_mocktracer": False,
        "build_dynamic_loading": False,
        "build_testing": False
        }
>>>>>>> 9c1208497de912c7055aea148626aabf1e7552d2

    _cmake = None

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def source(self):
<<<<<<< HEAD
        self.run("git clone -b v1.6.0 https://github.com/opentracing/opentracing-cpp.git")
        os.rename(self.name, self._source_subfolder)
=======
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)
>>>>>>> 9c1208497de912c7055aea148626aabf1e7552d2

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake

        self._cmake = CMake(self)
<<<<<<< HEAD
        self._cmake.definitions["BUILD_SHARED_LIBS"] = False
        self._cmake.definitions["BUILD_STATIC_LIBS"] = True
        self._cmake.definitions["BUILD_MOCKTRACER"] = False
        self._cmake.definitions["BUILD_DYNAMIC_LOADING"] = False
        self._cmake.definitions["BUILD_TESTING"] = False

=======
        self._cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        self._cmake.definitions["BUILD_STATIC_LIBS"] = self.options.static
        self._cmake.definitions["BUILD_MOCKTRACER"] = self.options.build_mocktracer
        self._cmake.definitions["BUILD_DYNAMIC_LOADING"] = self.options.build_dynamic_loading
        self._cmake.definitions["BUILD_TESTING"] = self.options.build_testing
>>>>>>> 9c1208497de912c7055aea148626aabf1e7552d2

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

<<<<<<< HEAD
=======
        if (self.options.static):
            self.cpp_info.defines.append("OPENTRACING_STATIC")

            if (self.options.build_mocktracer):
                self.cpp_info.defines.append("OPENTRACING_MOCK_TRACER_STATIC")
            


>>>>>>> 9c1208497de912c7055aea148626aabf1e7552d2
