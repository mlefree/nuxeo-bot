from flask_api import status

from src.services.interfaces import ServiceAbstract


class ServicesDirectory:
    """
        Main services directory : add your modules registration here
    """

    def __init__(self):
        self.services: [ServiceAbstract] = []
        pass

    def declareMyService(self, service: ServiceAbstract):
        self.services.append(service)

    def launchAllServices(self) -> [ServiceAbstract]:
        # for service in self.services:
        #    service.launch()

        return self.services

    def getAllServices(self) -> [ServiceAbstract]:
        return self.services

    def getService(self, title) -> ServiceAbstract:
        serviceFound = None
        for service in self.services:
            if service.title == title:
                serviceFound = service
                break

        return serviceFound

    def launchService(self, title, params) -> (str, int):
        output = 'not found'
        outputStatus = status.HTTP_404_NOT_FOUND

        serviceFound = self.getService(title)
        if serviceFound:
            output = 'needs valid params'
            outputStatus = status.HTTP_400_BAD_REQUEST
            if serviceFound.isParamsValid(params):
                output, outputStatus = serviceFound.launch(params)

        return output, outputStatus


class ServicesDirectoryFactory:
    singleton: ServicesDirectory = None

    def __init__(self):
        pass

    @staticmethod
    def get() -> ServicesDirectory:
        if ServicesDirectoryFactory.singleton is None:
            ServicesDirectoryFactory.singleton = ServicesDirectory()

        return ServicesDirectoryFactory.singleton
