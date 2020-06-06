from conans import ConanFile, CMake

class HelloworldQtConan(ConanFile):
	name = "helloworldqtconan"
	version = "0.1"
	description = """Hello world example using a Qt conan package"""
	homepage = "https://github.com/rkibria"
	url = "https://github.com/rkibria/helloworld-qt-conan"
	license = "MIT"
	author = "Raihan Kibria"

	settings = "os", "compiler", "build_type", "arch"
	requires = "qt/5.15.0@bincrafters/stable"
	generators = "cmake"
	default_options = {"qt:commercial": False,}

	def imports(self):
		self.copy("*.dll", dst="bin", src="bin")
		self.copy("*", dst="bin/plugins", src="plugins")

	def build(self):
		cmake = CMake(self, generator="Ninja")
		cmake.configure()
		cmake.build()
