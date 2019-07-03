import os

from flask_api import status

from src.services.interfaces import ServiceAbstract

from nuxeo.client import Nuxeo

ENV_NUXEO_PWD = str(os.environ.get("NUXEO_PWD", 'Administrator'))


class NuxeoService(ServiceAbstract):
    """
        Nuxeo example service.py
    """

    def __init__(self):
        super().__init__("nuxeo", "nuxeo intelligent tools", "params??", False)
        pass

    def isParamsValid(self, params) -> bool:
        # if not params:
        #    return False

        return True

    def launch(self, body) -> (str, int):
        output = 'Service TODO: ' + str(body)
        outputStatus = status.HTTP_400_BAD_REQUEST

        # params should looks like :
        # {
        #   "instance":
        #   {
        #       "url": "https://.../nuxeo",
        #       "user": "Administrator",
        #       "pwd":  "xxx"
        #   },
        #   "query": "SELECT * FROM Document WHERE ..."
        #  }

        if body['instance'] and body['instance']['url'] and body['instance']['user'] and body['instance']['pwd'] and \
                body['query']:

            # output = None
            nuxeo = Nuxeo(
                host=body['instance']['url'],
                auth=(body['instance']['user'], body['instance']['pwd'])
            )

            # Make the request
            search = nuxeo.client.query(body['query'])

            # Get results
            entries = search['entries']

            output = 'List entries found: ' + entries

            if output:
                outputStatus = status.HTTP_200_OK
            else:
                outputStatus = status.HTTP_204_NO_CONTENT

        return output, outputStatus
