from conans import ConanFile, AutoToolsBuildEnvironment, tools
from conans.errors import ConanInvalidConfiguration
import os


class JerasureCompleteConan(ConanFile):
    name = "jerasure"
    description = "Erasure Coding for storage applications"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/ceph/jerasure"
    license = "BSD-3-Clause"
    topics = ("math", "algorithms")

    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "sse": [True, False],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "sse": True,
    }

    _source_subfolder = "source_subfolder"
    _autotools = None

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        os.rename(self.name + "-" + self.version, self._source_subfolder)

    def config_options(self):
        if self.settings.os == 'Windows':
            del self.options.fPIC

    def requirements(self):
        self.requires("gf-complete/1.03")

    def configure(self):
        #if tools.os_info.is_windows and not self.settings.compiler == "gcc":
        #    # Building on Windows is currently only supported using the MSYS2
        #    # subsystem.
        #    #
        #    # A suitable profile for MSYS2 can be found in the documentation:
        #    # https://github.com/conan-io/docs/blob/b712aa7c0dc99607c46c57585787ced2ae66ac33/systems_cross_building/windows_subsystems.rst
        #    raise ConanInvalidConfiguration(
        #        "Windows is only supported using the MSYS2 subsystem")

        del self.settings.compiler.libcxx
        del self.settings.compiler.cppstd

    def _configure_autotools(self):
        if self._autotools:
            return self._autotools

        self._autotools = AutoToolsBuildEnvironment(
            self, win_bash=tools.os_info.is_windows)

        with tools.environment_append(self._autotools.vars):
            self.run("autoreconf --force --install", win_bash=tools.os_info.is_windows)

        if "x86" in self.settings.arch:
            self._autotools.flags.append('-mstackrealign')

        if "fPIC" in self.options:
            self._autotools.fpic = self.options.fPIC

        configure_args = [
            "--enable-shared=%s" % ("yes" if self.options.shared else "no"),
            "--enable-static=%s" % ("no" if self.options.shared else "yes")
        ]

        if not self.options.sse:
            configure_args.append("--disable-sse")

        self._autotools.configure(args=configure_args)

        return self._autotools

    def build(self):
        with tools.chdir(self._source_subfolder):
            autotools = self._configure_autotools()
            autotools.make()

    def package(self):
        self.copy("COPYING", dst="licenses", src=self._source_subfolder)
        with tools.chdir(self._source_subfolder):
            autotools = self._configure_autotools()
            autotools.install()

        # don't package la file
        la_file = os.path.join(self.package_folder, "lib", "libJerasure.la")
        if os.path.isfile(la_file):
            os.unlink(la_file)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.includedirs.append(os.path.join("include"))
