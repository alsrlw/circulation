from nose.tools import set_trace
import flask
from flask import Response
from flask_babel import lazy_gettext as _
from core.model import (
    ExternalIntegration,
    get_one,
    get_one_or_create,
)
from core.util.problem_detail import ProblemDetail
from . import SettingsController
from api.admin.google_oauth_admin_authentication_provider import GoogleOAuthAdminAuthenticationProvider
from api.admin.problem_details import *

class AdminAuthServicesController(SettingsController):

    def process_admin_auth_services(self):
        self.require_system_admin()
        provider_apis = [GoogleOAuthAdminAuthenticationProvider]
        self.protocols = self._get_integration_protocols(provider_apis, protocol_name_attr="NAME")
        if flask.request.method == 'GET':
            return self.process_get()
        else:
            return self.process_post()

    def process_get(self):
        auth_services = self._get_integration_info(ExternalIntegration.ADMIN_AUTH_GOAL, self.protocols)
        return dict(
            admin_auth_services=auth_services,
            protocols=self.protocols,
        )

    def process_post(self):
        protocol = flask.request.form.get("protocol")
        id = flask.request.form.get("id")
        auth_service = ExternalIntegration.admin_authentication(self._db)
        fields = {"protocol": protocol, "id": id, "auth_service": auth_service}
        error = self.validate_form_fields(**fields)
        if error:
            return error

        is_new = False

        if not auth_service:
            if protocol:
                auth_service, is_new = get_one_or_create(
                    self._db, ExternalIntegration, protocol=protocol,
                    goal=ExternalIntegration.ADMIN_AUTH_GOAL
                )
            else:
                return NO_PROTOCOL_FOR_NEW_SERVICE

        name = flask.request.form.get("name")
        auth_service.name = name

        [protocol] = [p for p in self.protocols if p.get("name") == protocol]
        result = self._set_integration_settings_and_libraries(auth_service, protocol)
        if isinstance(result, ProblemDetail):
            return result

        if is_new:
            return Response(unicode(auth_service.protocol), 201)
        else:
            return Response(unicode(auth_service.protocol), 200)

    def validate_form_fields(self, **fields):
        if fields.get("protocol") and fields.get("protocol") not in ExternalIntegration.ADMIN_AUTH_PROTOCOLS:
            return UNKNOWN_PROTOCOL
        if fields.get("auth_service"):
            if fields.get("id") and int(fields.get("id")) != fields.get("auth_service").id:
                return MISSING_SERVICE
            if fields.get("protocol") != fields.get("auth_service").protocol:
                return CANNOT_CHANGE_PROTOCOL
        else:
            if fields.get("id"):
                return MISSING_SERVICE

    def process_delete(self, protocol):
        self.require_system_admin()
        service = get_one(self._db, ExternalIntegration, protocol=protocol, goal=ExternalIntegration.ADMIN_AUTH_GOAL)
        if not service:
            return MISSING_SERVICE
        self._db.delete(service)
        return Response(unicode(_("Deleted")), 200)