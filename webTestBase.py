class WebTestBase(metaclass=ABCMeta):
	@abstractmethod
	def connectWebBrowser(self):
		pass

	@abstractmethod
	def clickButton(self):
		pass