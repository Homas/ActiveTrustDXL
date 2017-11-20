import logging

from dxlbootstrap.app import Application
from dxlclient.service import ServiceRegistrationInfo
from requesthandlers import *


# Configure local logger
logger = logging.getLogger(__name__)


class DXLATLookup(Application):
    """
    The "ActiveTrust Dossier and TIDE Lookup Service" application class.
    """
    CONFIG_SECTION = "General"
    APIKEY_PROP = "apikey"
    TIDE_FORMAT_PROP="tide_format"
    TIDE_MAX_REC_PROP="tide_max_rec"


    def __init__(self, config_dir):
        """
        Constructor parameters:

        :param config_dir: The location of the configuration files for the
            application
        """
        super(DXLATLookup, self).__init__(config_dir, "activetrustlookup.config")
        self._api_key = None
        self._tide_format = None
        self._tide_max_rec = None

    @property
    def api_key(self):
        """The ActiveTrust API key"""
        return self._api_key

    @property
    def tide_format(self):
        """The ActiveTrust default TIDE response format"""
        return self._tide_format

    @property
    def tide_max_rec(self):
        """The ActiveTrust default TIDE maximum return records. DXL maximum payload is 1Mb"""
        return self._tide_max_rec

    @property
    def client(self):
        """
        The DXL client used by the application to communicate with the DXL
        fabric
        """
        return self._dxl_client

    @property
    def config(self):
        """
        The application configuration (as read from the "activetrustlookup.config" file)
        """
        return self._config

    def on_run(self):
        """
        Invoked when the application has started running.
        """
        logger.info("On 'run' callback.")

    def on_load_configuration(self, config):
        """
        Invoked after the application-specific configuration has been loaded

        This callback provides the opportunity for the application to parse
        additional configuration properties.

        :param config: The application configuration
        """
        logger.info("On 'load configuration' callback.")

        # ActiveTrust API Key
        try:
            self._api_key = config.get(self.CONFIG_SECTION, self.APIKEY_PROP)
        except Exception:
            pass
        if not self._api_key:
            raise Exception("ActiveTrust API Key not found in configuration file: {0}".format(self._app_config_path))
        try:
            self._tide_format = config.get(self.CONFIG_SECTION, self.TIDE_FORMAT_PROP)
        except Exception:
            self._tide_format='json'
        try:
            self._tide_max_rec = config.get(self.CONFIG_SECTION, self.TIDE_MAX_REC_PROP)
        except Exception:
            self._tide_max_rec=100



    def on_dxl_connect(self):
        """
        Invoked after the client associated with the application has connected
        to the DXL fabric.
        """
        logger.info("On 'DXL connect' callback.")

    def on_register_services(self):
        """
        Invoked when services should be registered with the application
        """
        # Register service 'tide_srv'
        logger.info("Registering service: {0}".format("tide_srv"))
        service = ServiceRegistrationInfo(self._dxl_client, "/infoblox/activetrust/tide")
        logger.info("Registering request callback: {0}".format("tide_req"))
        self.add_request_callback(service, "/infoblox/activetrust/tide", TIDECallback(self), True)
        self.register_service(service)
        # Register service 'tide_lookup_srv'
        logger.info("Registering service: {0}".format("tide_lookup_srv"))
        service = ServiceRegistrationInfo(self._dxl_client, "/infoblox/activetrust/tide_lookup")
        logger.info("Registering request callback: {0}".format("tide_lookup_req"))
        self.add_request_callback(service, "/infoblox/activetrust/tide_lookup", TIDELookupCallback(self), True)
        self.register_service(service)
        # Register service 'dossier_srv'
        logger.info("Registering service: {0}".format("dossier_srv"))
        service = ServiceRegistrationInfo(self._dxl_client, "/infoblox/activetrust/dossier")
        logger.info("Registering request callback: {0}".format("dossier_req"))
        self.add_request_callback(service, "/infoblox/activetrust/dossier", DossierCallback(self), True)
        self.register_service(service)
        # Register service 'dossier_lookup_srv'
        logger.info("Registering service: {0}".format("dossier_lookup_srv"))
        service = ServiceRegistrationInfo(self._dxl_client, "/infoblox/activetrust/dossier_lookup")
        logger.info("Registering request callback: {0}".format("dossier_lookup_req"))
        self.add_request_callback(service, "/infoblox/activetrust/dossier_lookup", DossierLookupCallback(self), True)
        self.register_service(service)
