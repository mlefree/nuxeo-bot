
import os

from flask_api import status

from src.services.interfaces import ServiceAbstract

from nuxeo.client import Nuxeo

ENV_NUXEO_PWD = str(os.environ.get("NUXEO_PWD", ''))


class NuxeoService(ServiceAbstract):
    """
        Nuxeo example service.py
    """

    def __init__(self):
        super().__init__("nuxeoService", "nuxeo intelligent tools", "params??", False)
        pass

    def isParamsValid(self, params) -> bool:
        # if not params:
        #    return False

        return True

    def launch(self, params) -> (str, int):
        output = 'List Service TODO: ' + str(params)
        outputStatus = status.HTTP_400_BAD_REQUEST

        nuxeo = Nuxeo(
            host='https://mleprevost.cloud.nuxeo.com/nuxeo/',
            auth=('Administrator', ENV_NUXEO_PWD)
        )

        # Build a query using its UID
        nxql = ("SELECT * FROM Document WHERE ecm:ancestorId = '{uid}'"
                "   AND ecm:primaryType IN ('File', 'Picture')"
                "   AND ecm:currentLifeCycleState != 'deleted'")
        query = nxql.format(uid=ws.uid)

        # Make the request
        search = nuxeo.client.query(query, params={'properties': '*'})

        # Get results
        entries = search['entries']

        if params['data']:
            max = -1
            output = None
            for el in params['data']:
                if len(el['comments']) > max:
                    max = len(el['comments'])
                    output = 'List entries found: ' + entries

            if output:
                outputStatus = status.HTTP_200_OK
            else:
                outputStatus = status.HTTP_204_NO_CONTENT

        return output, outputStatus
