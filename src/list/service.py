from flask_api import status

from src.services.interfaces import ServiceAbstract


class ListService(ServiceAbstract):
    """
        List example service.py
    """

    def __init__(self):
        super().__init__("listService", "list intelligent tools", "params??", False)
        pass

    def isParamsValid(self, params) -> bool:
        # if not params:
        #    return False

        return True

    def launch(self, params) -> (str, int):
        output = 'List Service TODO: ' + str(params)
        outputStatus = status.HTTP_400_BAD_REQUEST

        if params['data']:
            max = -1
            output = None
            for el in params['data']:
                if len(el['comments']) > max:
                    max = len(el['comments'])
                    output = 'List max found: ' + str(el['value']) + ' - ' + str(max)

            if output:
                outputStatus = status.HTTP_200_OK
            else:
                outputStatus = status.HTTP_204_NO_CONTENT

        return output, outputStatus
