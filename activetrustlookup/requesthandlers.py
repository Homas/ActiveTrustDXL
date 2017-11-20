import logging
# Requests library
import requests

from dxlclient.callbacks import RequestCallback
from dxlclient.message import Response, ErrorResponse
from dxlbootstrap.util import MessageUtils


# Configure local logger
logger = logging.getLogger(__name__)

def get_ioc_type(data,req):
    import re
    if re.search("://", data):
        dtype="url"
    elif re.search("^[a-zA-Z0-9]{32,}$", data) and req=="dossier":
        dtype="hash"
    elif re.search("^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", data):
        dtype="ip"
    elif re.search(":.*:", data):
        dtype="ip"
    elif re.search("@", data) and req=="dossier":
        dtype="email"
    else: dtype="host"
    return dtype

class TIDECallback(RequestCallback):
    """
    'tide_req' request handler registered with topic '/infoblox/activetrust/tide'
    """

    def __init__(self, app):
        """
        Constructor parameters:

        :param app: The application this handler is associated with
        """
        super(TIDECallback, self).__init__()
        self._app = app

    def on_request(self, request):
        """
        Invoked when a request message is received.

        :param request: The request message
        """
        # Handle request
        logger.info("Request received on topic: '{0}' with payload: '{1}'".format(
            request.destination_topic, MessageUtils.decode_payload(request)))

        try:
            # Create response
            res = Response(request)

            # Read DXL request payload into dictionary
            params = MessageUtils.json_payload_to_dict(request)

            # Invoke API call
            http_res = requests.get("https://api.activetrust.net:8000/api/data/threats", params=params, auth=(self._app.api_key, ''))
            content=unicode(http_res.content, "utf-8")

            # Add web service response to DXL response payload
            MessageUtils.encode_payload(res, content, enc='utf-8')

            # Send response
            self._app.client.send_response(res)

        except Exception as ex:
            logger.exception("Error handling request")
            err_res = ErrorResponse(request, error_code=0, error_message=MessageUtils.encode(str(ex)))
            self._app.client.send_response(err_res)


class TIDELookupCallback(RequestCallback):
    """
    'tide_lookup_req' request handler registered with topic '/infoblox/activetrust/tide_lookup'
    """

    def __init__(self, app):
        """
        Constructor parameters:

        :param app: The application this handler is associated with
        """
        super(TIDELookupCallback, self).__init__()
        self._app = app

    def on_request(self, request):
        """
        Invoked when a request message is received.

        :param request: The request message
        """
        # Handle request
        logger.info("Request received on topic: '{0}' with payload: '{1}'".format(
            request.destination_topic, MessageUtils.decode_payload(request)))

        try:
            # Create response
            res = Response(request)

            # Read DXL request payload into dictionary
            params = MessageUtils.json_payload_to_dict(request)


            # Invoke API call
            if 'data' in params.keys() and params['data']!="":
                tide_data=params['data']
                if 'type' in params.keys(): tide_type=params['type']
                else: tide_type=get_ioc_type(tide_data,'tide')
                if 'rlimit' in params.keys() and params['max_rec']<self._app.tide_max_rec : tide_max_rec=params['max_rec']
                else: tide_max_rec=self._app.tide_max_rec #Error data is required

                if 'format' in params.keys(): tide_format=params['format']
                else: tide_format=self._app.tide_format #Error data is required
                http_res = requests.get("https://api.activetrust.net:8000/api/data/threats", params={"type":tide_type, tide_type:tide_data, "data_format":tide_format, "rlimit":tide_max_rec}, auth=(self._app.api_key, ''))
                content=unicode(http_res.content, "utf-8")
            else: content="{'status':'error','errorMessage':'The data field is required'}" #Error data is required

            # Add web service response to DXL response payload
            MessageUtils.encode_payload(res, content, enc='utf-8')

            # Send response
            self._app.client.send_response(res)

        except Exception as ex:
            logger.exception("Error handling request")
            err_res = ErrorResponse(request, error_code=0, error_message=MessageUtils.encode(str(ex)))
            self._app.client.send_response(err_res)


class DossierCallback(RequestCallback):
    """
    'dossier_req' request handler registered with topic '/infoblox/activetrust/dossier'
    """

    def __init__(self, app):
        """
        Constructor parameters:

        :param app: The application this handler is associated with
        """
        super(DossierCallback, self).__init__()
        self._app = app

    def on_request(self, request):
        """
        Invoked when a request message is received.

        :param request: The request message
        """
        # Handle request
        logger.info("Request received on topic: '{0}' with payload: '{1}'".format(
            request.destination_topic, MessageUtils.decode_payload(request)))

        try:
            # Create response
            res = Response(request)

            # Read DXL request payload into dictionary
            params = MessageUtils.decode_payload(request)
            headers = {'Content-Type': 'application/json'}
            #print(params)

            # Invoke API call
            http_res = requests.post("https://api.activetrust.net:8000/api/services/intel/lookup/jobs?wait=true", headers=headers, data=params, auth=(self._app.api_key, ''))
            content=unicode(http_res.content, "utf-8")

            # Add web service response to DXL response payload
            MessageUtils.encode_payload(res, content, enc='utf-8')

            # Send response
            self._app.client.send_response(res)

        except Exception as ex:
            logger.exception("Error handling request")
            err_res = ErrorResponse(request, error_code=0, error_message=MessageUtils.encode(str(ex)))
            self._app.client.send_response(err_res)


class DossierLookupCallback(RequestCallback):
    """
    'dossier_lookup_req' request handler registered with topic '/infoblox/activetrust/dossier_lookup'
    """

    def __init__(self, app):
        """
        Constructor parameters:

        :param app: The application this handler is associated with
        """
        super(DossierLookupCallback, self).__init__()
        self._app = app

    def on_request(self, request):
        """
        Invoked when a request message is received.

        :param request: The request message
        """
        # Handle request
        logger.info("Request received on topic: '{0}' with payload: '{1}'".format(
            request.destination_topic, MessageUtils.decode_payload(request)))

        try:
            # Create response
            res = Response(request)

            # Read DXL request payload into dictionary
            params = MessageUtils.json_payload_to_dict(request)

            # Invoke API call
            if 'data' in params.keys() and params['data'] != "":
                dossier_data=params['data']
                if 'type' in params.keys(): dossier_type=params['type']
                else: dossier_type=get_ioc_type(dossier_data,'dossier')
                if 'sources' in params.keys(): payload={"target":{"one":{"type":dossier_type,"target": dossier_data,"sources":params['sources']}}}
                else: payload={"target":{"one":{"type":dossier_type,"target": dossier_data}}}
                headers = {'Content-Type': 'application/json'}
                http_res = requests.post("https://api.activetrust.net:8000/api/services/intel/lookup/jobs?wait=true", json=payload, auth=(self._app.api_key, ''))
                content=unicode(http_res.content, "utf-8")
            else: content="{'status':'error','errorMessage':'The data field is required'}" #Error data is required

            # Add web service response to DXL response payload
            MessageUtils.encode_payload(res, content, enc='utf-8')

            # Send response
            self._app.client.send_response(res)

        except Exception as ex:
            logger.exception("Error handling request")
            err_res = ErrorResponse(request, error_code=0, error_message=MessageUtils.encode(str(ex)))
            self._app.client.send_response(err_res)
