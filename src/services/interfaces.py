from flask_api import status


class ServiceParameter:

    def __init__(self, id: str, description: str, value):
        self.id = id
        self.description = description
        self.value = value


class ServiceAbstract(dict):
    """
        A base for your services
    """

    def __init__(self, title: str, description: str, params: [ServiceParameter], use_db: bool = False):
        dict.__init__(self, title=title, description=description, params=params)
        self.title = title
        self.description = description
        self.params = params
        self.useDB = use_db
        from src.services.directory import ServicesDirectoryFactory
        ServicesDirectoryFactory.get().declareMyService(self)

    def __str__(self):
        return "" + str(self.title) + " : " + self.description

    def isParamsValid(self, params) -> bool:
        if not params:
            return False

        return True

    def launch(self, params) -> (str, int):
        output = 'implement it'
        return output, status.HTTP_204_NO_CONTENT
