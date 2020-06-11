from api.saml.metadata import Binding

NAME_ID_FORMAT_1 = 'urn:mace:shibboleth:1.0:nameIdentifier'
NAME_ID_FORMAT_2 = 'urn:oasis:names:tc:SAML:2.0:nameid-format:transient'

IDP_1_ENTITY_ID = 'http://idp1.hilbertteam.net/idp/shibboleth'
IDP_1_UI_INFO_DISPLAY_NAME = 'Shibboleth Test IdP 1'
IDP_1_UI_INFO_EN_DISPLAY_NAME = IDP_1_UI_INFO_DISPLAY_NAME
IDP_1_UI_INFO_ES_DISPLAY_NAME = IDP_1_UI_INFO_DISPLAY_NAME
IDP_1_UI_INFO_DESCRIPTION = 'Shibboleth Test IdP 1'
IDP_1_UI_INFO_INFORMATION_URL = 'http://idp1.hilbertteam.net'
IDP_1_UI_INFO_PRIVACY_STATEMENT_URL = 'http://idp1.hilbertteam.net'
IDP_1_UI_INFO_LOGO_URL = 'http://idp1.hilbertteam.net/logo.png'

IDP_1_SSO_URL = 'http://idp1.hilbertteam.net/idp/profile/SAML2/Redirect/SSO'
IDP_1_SSO_BINDING = Binding.HTTP_REDIRECT

IDP_2_ENTITY_ID = 'http://idp2.hilbertteam.net/idp/shibboleth'
IDP_2_UI_INFO_DISPLAY_NAME = 'Shibboleth Test IdP 2'
IDP_2_UI_INFO_EN_DISPLAY_NAME = IDP_2_UI_INFO_DISPLAY_NAME
IDP_2_UI_INFO_ES_DISPLAY_NAME = IDP_2_UI_INFO_DISPLAY_NAME
IDP_2_UI_INFO_DESCRIPTION = 'Shibboleth Test IdP 2'
IDP_2_UI_INFO_INFORMATION_URL = 'http://idp2.hilbertteam.net'
IDP_2_UI_INFO_PRIVACY_STATEMENT_URL = 'http://idp2.hilbertteam.net'
IDP_2_UI_INFO_LOGO_URL = 'http://idp2.hilbertteam.net/logo.png'

IDP_2_SSO_URL = 'http://idp2.hilbertteam.net/idp/profile/SAML2/Redirect/SSO'
IDP_2_SSO_BINDING = Binding.HTTP_REDIRECT

SP_ENTITY_ID = 'http://sp.hilbertteam.net/idp/shibboleth'

SP_ACS_URL = 'http://sp.hilbertteam.net/idp/profile/SAML2/POST'
SP_ACS_BINDING = Binding.HTTP_POST

SIGNING_CERTIFICATE = \
    '''MIICXDCCAcWgAwIBAgIBADANBgkqhkiG9w0BAQ0FADBLMQswCQYDVQQGEwJ1czEN
MAsGA1UECAwET2hpbzETMBEGA1UECgwKQUNNRSwgSW5jLjEYMBYGA1UEAwwPaGls
YmVydHRlYW0ubmV0MB4XDTIwMDUxODE4MjUyM1oXDTIxMDUxODE4MjUyM1owSzEL
MAkGA1UEBhMCdXMxDTALBgNVBAgMBE9oaW8xEzARBgNVBAoMCkFDTUUsIEluYy4x
GDAWBgNVBAMMD2hpbGJlcnR0ZWFtLm5ldDCBnzANBgkqhkiG9w0BAQEFAAOBjQAw
gYkCgYEAqx63LDc2vjoYlTvddjPOKDsduR0++A1lmGxdX1N6Ei4NRiWaqBnVij6m
Oqzq5quMA8M3du71aVzE0ELJOuhzrjpu6Rn40KGO6Ewiv3StQkbwAArrrIlIPA9U
MpsGD+/oNXlbF9ZbfqvxEoZcEk6XR6fJT7zXBNzp75dCi39D53MCAwEAAaNQME4w
HQYDVR0OBBYEFCmRcv2NFCSso9IRSFQsdST5FpBfMB8GA1UdIwQYMBaAFCmRcv2N
FCSso9IRSFQsdST5FpBfMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQENBQADgYEA
c/ddQRAswvrlYD8IOA9TCjyqkUJmyJBOj+d0PTzW7lF7NUyPSp0SunDq12RD8imV
q15wNzuzsiIfUZ7F/sp1iFH8ASrBS4sk39stDgUcjFNcwekihUGw3GfhGcniFvvi
a/F82fbPXBPajb9nXNyn3ZwlLsooeC06oIj8FlyHoR8=
'''

ENCRYPTION_CERTIFICATE = \
    '''MIIDEzCCAfugAwIBAgIUG6Nn1rlERS1vsi88tcdzSYX0oqAwDQYJKoZIhvcNAQEL
BQAwFTETMBEGA1UEAwwKaWRwdGVzdGJlZDAeFw0xNTEyMTEwMjIwMTRaFw0zNTEy
MTEwMjIwMTRaMBUxEzARBgNVBAMMCmlkcHRlc3RiZWQwggEiMA0GCSqGSIb3DQEB
AQUAA4IBDwAwggEKAoIBAQCBXv0o3fmT8iluyLjJ4lBAVCW+ZRVyEXPYQuRi7vfD
cO4a6d1kxiJLsaK0W88VNxjFQRr8PgDkWr28vwoH1rgk4pLsszLD48DBzD942peJ
l/S6FnsIJjmaHcBh4pbNhU4yowu63iKkvttrcZAEbpEro6Z8CziWEx8sywoaYEQG
ifPkr9ORV6Cn3txq+9gMBePG41GrtZrUGIu+xrndL0Shh4Pq0eq/9MAsVlIIXEa8
9WfH8J2kFcTOfoWtIc70b7TLZQsx4YnNcnrGLSUEcstFyPLX+Xtv5SNZF89OOIxX
VNjNvgE5DbJb9hMM4UAFqI+1bo9QqtxwThjc/sOvIxzNAgMBAAGjWzBZMB0GA1Ud
DgQWBBStTyogRPuAVG6q7yPyav1uvE+7pTA4BgNVHREEMTAvggppZHB0ZXN0YmVk
hiFodHRwczovL2lkcHRlc3RiZWQvaWRwL3NoaWJib2xldGgwDQYJKoZIhvcNAQEL
BQADggEBAFMfoOv+oISGjvamq7+Y4G7ep5vxlAPeK3RATYPYvAmyH946qZXh98ni
QXyuqZW5P5eEt86toY45IwDU5r09SKwHughEe99iiEkxh0mb2qo84qX9/qcg+kyN
jeLd/OSyolpUCEFNwOFcog7pj7Eer+6AHbwTn1Mjb5TBsKwtDMJsaxPvdj0u7M5r
xL/wHkFhn1rCo2QiojzjSlV3yLTh49iTyhE3cG+RxaNKDCxhp0jSSLX1BW/ZoPA8
+PMJEA+Q0QbyRD8aJOHN5O8jGxCa/ZzcOnYVL6AsEXoDiY3vAUYh1FUonOWw0m9H
p+tGUbGS2l873J5PrsbpeKEVR/IIoKo=
'''

INCORRECT_XML = ''

INCORRECT_ONE_IDP_METADATA_WITHOUT_DISPLAY_NAME = \
    '''<?xml version="1.0" encoding="UTF-8"?>
<!--
     This is example metadata only. Do *NOT* supply it as is without review,
     and do *NOT* provide it in real time to your partners.

     This metadata is not dynamic - it will not change as your configuration changes.
-->
<EntityDescriptor
  xmlns="urn:oasis:names:tc:SAML:2.0:metadata"
  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
  xmlns:shibmd="urn:mace:shibboleth:metadata:1.0"
  xmlns:xml="http://www.w3.org/XML/1998/namespace"
  xmlns:mdui="urn:oasis:names:tc:SAML:metadata:ui"
  entityID="{0}">
    <IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol urn:oasis:names:tc:SAML:1.1:protocol urn:mace:shibboleth:1.0">
        <KeyDescriptor use="signing">
            <ds:KeyInfo>
                    <ds:X509Data>
                        <ds:X509Certificate>
{1}
                        </ds:X509Certificate>
                    </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>
        <KeyDescriptor use="encryption">
            <ds:KeyInfo>
                    <ds:X509Data>
                        <ds:X509Certificate>
{2}
                        </ds:X509Certificate>
                    </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>
        <NameIDFormat>{3}</NameIDFormat>
        <NameIDFormat>{4}</NameIDFormat>
        <SingleSignOnService 
            Binding="{5}" 
            Location="{6}"/>
    </IDPSSODescriptor>
</EntityDescriptor>
'''.format(
        IDP_1_ENTITY_ID,
        SIGNING_CERTIFICATE,
        ENCRYPTION_CERTIFICATE,
        NAME_ID_FORMAT_1,
        NAME_ID_FORMAT_2,
        IDP_1_SSO_BINDING.value,
        IDP_1_SSO_URL)

INCORRECT_ONE_IDP_METADATA_WITHOUT_SSO_SERVICE = \
    '''<?xml version="1.0" encoding="UTF-8"?>
<!--
     This is example metadata only. Do *NOT* supply it as is without review,
     and do *NOT* provide it in real time to your partners.

     This metadata is not dynamic - it will not change as your configuration changes.
-->
<EntityDescriptor
  xmlns="urn:oasis:names:tc:SAML:2.0:metadata"
  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
  xmlns:shibmd="urn:mace:shibboleth:metadata:1.0"
  xmlns:xml="http://www.w3.org/XML/1998/namespace"
  xmlns:mdui="urn:oasis:names:tc:SAML:metadata:ui"
  entityID="{0}">
    <IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol urn:oasis:names:tc:SAML:1.1:protocol urn:mace:shibboleth:1.0">
        <Extensions>
            <shibmd:Scope regexp="false">example.org</shibmd:Scope>
            <mdui:UIInfo>
                <mdui:DisplayName xml:lang="en">{1}</mdui:DisplayName>
                <mdui:DisplayName xml:lang="es">{2}</mdui:DisplayName>
                <mdui:Description xml:lang="en">{3}</mdui:Description>
                <mdui:InformationURL xml:lang="en">{4}</mdui:InformationURL>
                <mdui:PrivacyStatementURL xml:lang="en">{5}</mdui:PrivacyStatementURL>
                <mdui:Logo height="10" width="10">{6}</mdui:Logo>
            </mdui:UIInfo>
        </Extensions>
        <KeyDescriptor use="signing">
            <ds:KeyInfo>
                    <ds:X509Data>
                        <ds:X509Certificate>
{7}
                        </ds:X509Certificate>
                    </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>
        <KeyDescriptor use="encryption">
            <ds:KeyInfo>
                    <ds:X509Data>
                        <ds:X509Certificate>
{8}
                        </ds:X509Certificate>
                    </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>
        <NameIDFormat>{9}</NameIDFormat>
        <NameIDFormat>{10}</NameIDFormat>
    </IDPSSODescriptor>
</EntityDescriptor>
'''.format(
        IDP_1_ENTITY_ID,
        IDP_1_UI_INFO_EN_DISPLAY_NAME,
        IDP_1_UI_INFO_ES_DISPLAY_NAME,
        IDP_1_UI_INFO_DESCRIPTION,
        IDP_1_UI_INFO_INFORMATION_URL,
        IDP_1_UI_INFO_PRIVACY_STATEMENT_URL,
        IDP_1_UI_INFO_LOGO_URL,
        SIGNING_CERTIFICATE,
        ENCRYPTION_CERTIFICATE,
        NAME_ID_FORMAT_1,
        NAME_ID_FORMAT_2)

INCORRECT_ONE_IDP_METADATA_WITH_SSO_SERVICE_WITH_WRONG_BINDING = \
    '''<?xml version="1.0" encoding="UTF-8"?>
<!--
     This is example metadata only. Do *NOT* supply it as is without review,
     and do *NOT* provide it in real time to your partners.

     This metadata is not dynamic - it will not change as your configuration changes.
-->
<EntityDescriptor
  xmlns="urn:oasis:names:tc:SAML:2.0:metadata"
  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
  xmlns:shibmd="urn:mace:shibboleth:metadata:1.0"
  xmlns:xml="http://www.w3.org/XML/1998/namespace"
  xmlns:mdui="urn:oasis:names:tc:SAML:metadata:ui"
  entityID="{0}">
    <IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol urn:oasis:names:tc:SAML:1.1:protocol urn:mace:shibboleth:1.0">
        <Extensions>
            <shibmd:Scope regexp="false">example.org</shibmd:Scope>
            <mdui:UIInfo>
                <mdui:DisplayName xml:lang="en">{1}</mdui:DisplayName>
                <mdui:DisplayName xml:lang="es">{2}</mdui:DisplayName>
                <mdui:Description xml:lang="en">{3}</mdui:Description>
                <mdui:InformationURL xml:lang="en">{4}</mdui:InformationURL>
                <mdui:PrivacyStatementURL xml:lang="en">{5}</mdui:PrivacyStatementURL>
                <mdui:Logo height="10" width="10">{6}</mdui:Logo>
            </mdui:UIInfo>
        </Extensions>
        <KeyDescriptor use="signing">
            <ds:KeyInfo>
                    <ds:X509Data>
                        <ds:X509Certificate>
{7}
                        </ds:X509Certificate>
                    </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>
        <KeyDescriptor use="encryption">
            <ds:KeyInfo>
                    <ds:X509Data>
                        <ds:X509Certificate>
{8}
                        </ds:X509Certificate>
                    </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>
        <NameIDFormat>{9}</NameIDFormat>
        <NameIDFormat>{10}</NameIDFormat>
        <SingleSignOnService 
            Binding="{11}" 
            Location="{12}"/>
    </IDPSSODescriptor>
</EntityDescriptor>
'''.format(
        IDP_1_ENTITY_ID,
        IDP_1_UI_INFO_EN_DISPLAY_NAME,
        IDP_1_UI_INFO_ES_DISPLAY_NAME,
        IDP_1_UI_INFO_DESCRIPTION,
        IDP_1_UI_INFO_INFORMATION_URL,
        IDP_1_UI_INFO_PRIVACY_STATEMENT_URL,
        IDP_1_UI_INFO_LOGO_URL,
        SIGNING_CERTIFICATE,
        ENCRYPTION_CERTIFICATE,
        NAME_ID_FORMAT_1,
        NAME_ID_FORMAT_2,
        Binding.HTTP_ARTIFACT.value,
        IDP_1_SSO_URL)

CORRECT_ONE_IDP_METADATA = \
    '''<?xml version="1.0" encoding="UTF-8"?>
<!--
     This is example metadata only. Do *NOT* supply it as is without review,
     and do *NOT* provide it in real time to your partners.

     This metadata is not dynamic - it will not change as your configuration changes.
-->
<EntityDescriptor
  xmlns="urn:oasis:names:tc:SAML:2.0:metadata"
  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
  xmlns:shibmd="urn:mace:shibboleth:metadata:1.0"
  xmlns:xml="http://www.w3.org/XML/1998/namespace"
  xmlns:mdui="urn:oasis:names:tc:SAML:metadata:ui"
  entityID="{0}">
    <IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol urn:oasis:names:tc:SAML:1.1:protocol urn:mace:shibboleth:1.0">
        <Extensions>
            <shibmd:Scope regexp="false">example.org</shibmd:Scope>
            <mdui:UIInfo>
                <mdui:DisplayName xml:lang="en">{1}</mdui:DisplayName>
                <mdui:DisplayName xml:lang="es">{2}</mdui:DisplayName>
                <mdui:Description xml:lang="en">{3}</mdui:Description>
                <mdui:InformationURL xml:lang="en">{4}</mdui:InformationURL>
                <mdui:PrivacyStatementURL xml:lang="en">{5}</mdui:PrivacyStatementURL>
                <mdui:Logo height="10" width="10">{6}</mdui:Logo>
            </mdui:UIInfo>
        </Extensions>
        <KeyDescriptor use="signing">
            <ds:KeyInfo>
                    <ds:X509Data>
                        <ds:X509Certificate>
{7}
                        </ds:X509Certificate>
                    </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>
        <KeyDescriptor use="encryption">
            <ds:KeyInfo>
                    <ds:X509Data>
                        <ds:X509Certificate>
{8}
                        </ds:X509Certificate>
                    </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>
        <NameIDFormat>{9}</NameIDFormat>
        <NameIDFormat>{10}</NameIDFormat>
        <SingleSignOnService 
            Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST-SimpleSign" 
            Location="http://idp.hilbertteam.net/idp/profile/SAML2/POST-SimpleSign/SSO"/>
        <SingleSignOnService 
            Binding="{11}" 
            Location="{12}"/>
    </IDPSSODescriptor>
</EntityDescriptor>
'''.format(
        IDP_1_ENTITY_ID,
        IDP_1_UI_INFO_EN_DISPLAY_NAME,
        IDP_1_UI_INFO_ES_DISPLAY_NAME,
        IDP_1_UI_INFO_DESCRIPTION,
        IDP_1_UI_INFO_INFORMATION_URL,
        IDP_1_UI_INFO_PRIVACY_STATEMENT_URL,
        IDP_1_UI_INFO_LOGO_URL,
        SIGNING_CERTIFICATE,
        ENCRYPTION_CERTIFICATE,
        NAME_ID_FORMAT_1,
        NAME_ID_FORMAT_2,
        IDP_1_SSO_BINDING.value,
        IDP_1_SSO_URL)

CORRECT_ONE_IDP_METADATA_WITHOUT_NAME_ID_FORMAT = \
    '''<?xml version="1.0" encoding="UTF-8"?>
<!--
     This is example metadata only. Do *NOT* supply it as is without review,
     and do *NOT* provide it in real time to your partners.

     This metadata is not dynamic - it will not change as your configuration changes.
-->
<EntityDescriptor
  xmlns="urn:oasis:names:tc:SAML:2.0:metadata"
  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
  xmlns:shibmd="urn:mace:shibboleth:metadata:1.0"
  xmlns:xml="http://www.w3.org/XML/1998/namespace"
  xmlns:mdui="urn:oasis:names:tc:SAML:metadata:ui"
  entityID="{0}">
    <IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol urn:oasis:names:tc:SAML:1.1:protocol urn:mace:shibboleth:1.0">
        <Extensions>
            <shibmd:Scope regexp="false">example.org</shibmd:Scope>
            <mdui:UIInfo>
                <mdui:DisplayName xml:lang="en">{1}</mdui:DisplayName>
                <mdui:DisplayName xml:lang="es">{2}</mdui:DisplayName>
                <mdui:Description xml:lang="en">{3}</mdui:Description>
                <mdui:InformationURL xml:lang="en">{4}</mdui:InformationURL>
                <mdui:PrivacyStatementURL xml:lang="en">{5}</mdui:PrivacyStatementURL>
                <mdui:Logo height="10" width="10" xml:lang="en">{6}</mdui:Logo>
            </mdui:UIInfo>
        </Extensions>
        <KeyDescriptor use="signing">
            <ds:KeyInfo>
                    <ds:X509Data>
                        <ds:X509Certificate>
{7}
                        </ds:X509Certificate>
                    </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>
        <KeyDescriptor use="encryption">
            <ds:KeyInfo>
                    <ds:X509Data>
                        <ds:X509Certificate>
{8}
                        </ds:X509Certificate>
                    </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>
        <SingleSignOnService 
            Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST-SimpleSign" 
            Location="http://idp.hilbertteam.net/idp/profile/SAML2/POST-SimpleSign/SSO"/>
        <SingleSignOnService 
            Binding="{9}" 
            Location="{10}"/>
    </IDPSSODescriptor>
</EntityDescriptor>
'''.format(
        IDP_1_ENTITY_ID,
        IDP_1_UI_INFO_EN_DISPLAY_NAME,
        IDP_1_UI_INFO_ES_DISPLAY_NAME,
        IDP_1_UI_INFO_DESCRIPTION,
        IDP_1_UI_INFO_INFORMATION_URL,
        IDP_1_UI_INFO_PRIVACY_STATEMENT_URL,
        IDP_1_UI_INFO_LOGO_URL,
        SIGNING_CERTIFICATE,
        ENCRYPTION_CERTIFICATE,
        IDP_1_SSO_BINDING.value,
        IDP_1_SSO_URL)

CORRECT_ONE_IDP_METADATA_WITH_ONE_CERTIFICATE = \
    '''<?xml version="1.0" encoding="UTF-8"?>
<!--
     This is example metadata only. Do *NOT* supply it as is without review,
     and do *NOT* provide it in real time to your partners.

     This metadata is not dynamic - it will not change as your configuration changes.
-->
<EntityDescriptor
  xmlns="urn:oasis:names:tc:SAML:2.0:metadata"
  xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
  xmlns:shibmd="urn:mace:shibboleth:metadata:1.0"
  xmlns:xml="http://www.w3.org/XML/1998/namespace"
  xmlns:mdui="urn:oasis:names:tc:SAML:metadata:ui"
  entityID="{0}">
    <IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol urn:oasis:names:tc:SAML:1.1:protocol urn:mace:shibboleth:1.0">
        <Extensions>
            <shibmd:Scope regexp="false">example.org</shibmd:Scope>
            <mdui:UIInfo>
                <mdui:DisplayName xml:lang="en">{1}</mdui:DisplayName>
                <mdui:DisplayName xml:lang="es">{2}</mdui:DisplayName>
                <mdui:Description xml:lang="en">{3}</mdui:Description>
                <mdui:InformationURL xml:lang="en">{4}</mdui:InformationURL>
                <mdui:PrivacyStatementURL xml:lang="en">{5}</mdui:PrivacyStatementURL>
                <mdui:Logo height="10" width="10" xml:lang="en">{6}</mdui:Logo>
            </mdui:UIInfo>
        </Extensions>
        <KeyDescriptor>
            <ds:KeyInfo>
                    <ds:X509Data>
                        <ds:X509Certificate>
{7}
                        </ds:X509Certificate>
                    </ds:X509Data>
            </ds:KeyInfo>
        </KeyDescriptor>
        <NameIDFormat>{8}</NameIDFormat>
        <NameIDFormat>{9}</NameIDFormat>
        <SingleSignOnService 
            Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST-SimpleSign" 
            Location="http://idp.hilbertteam.net/idp/profile/SAML2/POST-SimpleSign/SSO"/>
        <SingleSignOnService 
            Binding="{10}" 
            Location="{11}"/>
    </IDPSSODescriptor>
</EntityDescriptor>
'''.format(
        IDP_1_ENTITY_ID,
        IDP_1_UI_INFO_EN_DISPLAY_NAME,
        IDP_1_UI_INFO_ES_DISPLAY_NAME,
        IDP_1_UI_INFO_DESCRIPTION,
        IDP_1_UI_INFO_INFORMATION_URL,
        IDP_1_UI_INFO_PRIVACY_STATEMENT_URL,
        IDP_1_UI_INFO_LOGO_URL,
        SIGNING_CERTIFICATE,
        NAME_ID_FORMAT_1,
        NAME_ID_FORMAT_2,
        IDP_1_SSO_BINDING.value,
        IDP_1_SSO_URL)

CORRECT_MULTIPLE_IDPS_METADATA = \
    '''<?xml version="1.0" encoding="UTF-8"?>
<!--
      This is example metadata only. Do *NOT* supply it as is without review,
      and do *NOT* provide it in real time to your partners.

      This metadata is not dynamic - it will not change as your configuration changes.
-->
<EntityDescriptors>
  <EntityDescriptor xmlns="urn:oasis:names:tc:SAML:2.0:metadata" 
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#" 
    xmlns:shibmd="urn:mace:shibboleth:metadata:1.0" 
    xmlns:xml="http://www.w3.org/XML/1998/namespace" 
    xmlns:mdui="urn:oasis:names:tc:SAML:metadata:ui" 
    entityID="{0}">
    <IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol urn:oasis:names:tc:SAML:1.1:protocol urn:mace:shibboleth:1.0">
      <Extensions>
        <shibmd:Scope regexp="false">example.org</shibmd:Scope>
        <mdui:UIInfo>
          <mdui:DisplayName xml:lang="en">{1}</mdui:DisplayName>
          <mdui:DisplayName xml:lang="es">{2}</mdui:DisplayName>
        </mdui:UIInfo>
      </Extensions>
      <KeyDescriptor use="signing">
        <ds:KeyInfo>
          <ds:X509Data>
            <ds:X509Certificate>
{3}
            </ds:X509Certificate>
          </ds:X509Data>
        </ds:KeyInfo>
      </KeyDescriptor>
      <KeyDescriptor use="encryption">
        <ds:KeyInfo>
          <ds:X509Data>
            <ds:X509Certificate>
{4}
            </ds:X509Certificate>
          </ds:X509Data>
        </ds:KeyInfo>
      </KeyDescriptor>
      <NameIDFormat>{5}</NameIDFormat>
      <NameIDFormat>{6}</NameIDFormat>
      <SingleSignOnService 
        Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST-SimpleSign" 
        Location="http://idp.hilbertteam.net/idp/profile/SAML2/POST-SimpleSign/SSO"/>
      <SingleSignOnService 
        Binding="{7}" 
        Location="{8}"/>
    </IDPSSODescriptor>
  </EntityDescriptor>
  <EntityDescriptor xmlns="urn:oasis:names:tc:SAML:2.0:metadata" 
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#" 
    xmlns:shibmd="urn:mace:shibboleth:metadata:1.0" 
    xmlns:xml="http://www.w3.org/XML/1998/namespace" 
    xmlns:mdui="urn:oasis:names:tc:SAML:metadata:ui" 
    entityID="{9}">
    <IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol urn:oasis:names:tc:SAML:1.1:protocol urn:mace:shibboleth:1.0">
      <Extensions>
        <shibmd:Scope regexp="false">example.org</shibmd:Scope>
        <mdui:UIInfo>
          <mdui:DisplayName xml:lang="en">{10}</mdui:DisplayName>
          <mdui:DisplayName xml:lang="es">{11}</mdui:DisplayName>
        </mdui:UIInfo>
      </Extensions>
      <KeyDescriptor use="signing">
        <ds:KeyInfo>
          <ds:X509Data>
            <ds:X509Certificate>
{12}
            </ds:X509Certificate>
          </ds:X509Data>
        </ds:KeyInfo>
      </KeyDescriptor>
      <KeyDescriptor use="encryption">
        <ds:KeyInfo>
          <ds:X509Data>
            <ds:X509Certificate>
{13}
            </ds:X509Certificate>
          </ds:X509Data>
        </ds:KeyInfo>
      </KeyDescriptor>
      <NameIDFormat>{14}</NameIDFormat>
      <NameIDFormat>{15}</NameIDFormat>
      <SingleSignOnService 
        Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST-SimpleSign" 
        Location="http://idp.hilbertteam.net/idp/profile/SAML2/POST-SimpleSign/SSO"/>
      <SingleSignOnService 
        Binding="{16}" 
        Location="{17}"/>
    </IDPSSODescriptor>
  </EntityDescriptor>
</EntityDescriptors>
'''.format(
        IDP_1_ENTITY_ID,
        IDP_1_UI_INFO_EN_DISPLAY_NAME,
        IDP_1_UI_INFO_ES_DISPLAY_NAME,
        SIGNING_CERTIFICATE,
        ENCRYPTION_CERTIFICATE,
        NAME_ID_FORMAT_1,
        NAME_ID_FORMAT_2,
        IDP_1_SSO_BINDING.value,
        IDP_1_SSO_URL,
        IDP_2_ENTITY_ID,
        IDP_2_UI_INFO_EN_DISPLAY_NAME,
        IDP_2_UI_INFO_ES_DISPLAY_NAME,
        SIGNING_CERTIFICATE,
        ENCRYPTION_CERTIFICATE,
        NAME_ID_FORMAT_1,
        NAME_ID_FORMAT_2,
        IDP_2_SSO_BINDING.value,
        IDP_2_SSO_URL)

INCORRECT_ONE_SP_METADATA_WITHOUT_ACS_SERVICE = \
    '''<EntityDescriptor 
    xmlns="urn:oasis:names:tc:SAML:2.0:metadata"
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
    xmlns:shibmd="urn:mace:shibboleth:metadata:1.0"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
    xmlns:mdui="urn:oasis:names:tc:SAML:metadata:ui"
    entityID="{0}">
  <SPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol urn:oasis:names:tc:SAML:1.1:protocol urn:oasis:names:tc:SAML:1.0:protocol">
    <KeyDescriptor>
      <ds:KeyInfo>
        <ds:X509Data>
          <ds:X509Certificate>
{1}
          </ds:X509Certificate>
        </ds:X509Data>
      </ds:KeyInfo>
      <EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#aes128-gcm"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#aes192-gcm"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#aes256-gcm"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes192-cbc"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes256-cbc"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#tripledes-cbc"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#rsa-oaep"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p"/>
    </KeyDescriptor>
  </SPSSODescriptor>
</EntityDescriptor>
'''.format(
        SP_ENTITY_ID,
        SIGNING_CERTIFICATE)

CORRECT_ONE_SP_METADATA = \
    '''<EntityDescriptor 
    xmlns="urn:oasis:names:tc:SAML:2.0:metadata"
    xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
    xmlns:shibmd="urn:mace:shibboleth:metadata:1.0"
    xmlns:xml="http://www.w3.org/XML/1998/namespace"
    xmlns:mdui="urn:oasis:names:tc:SAML:metadata:ui"
    entityID="{0}">
  <SPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol urn:oasis:names:tc:SAML:1.1:protocol urn:oasis:names:tc:SAML:1.0:protocol">
    <KeyDescriptor>
      <ds:KeyInfo>
        <ds:X509Data>
          <ds:X509Certificate>
{1}
          </ds:X509Certificate>
        </ds:X509Data>
      </ds:KeyInfo>
      <EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#aes128-gcm"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#aes192-gcm"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#aes256-gcm"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes128-cbc"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes192-cbc"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#aes256-cbc"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#tripledes-cbc"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#rsa-oaep"/>
      <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p"/>
    </KeyDescriptor>
    <AssertionConsumerService 
        Binding="{2}" 
        Location="{3}/" 
        index="1"/>
    <AssertionConsumerService 
        Binding="{2}" 
        Location="{3}" 
        index="0"/>
  </SPSSODescriptor>
</EntityDescriptor>
'''.format(
        SP_ENTITY_ID,
        SIGNING_CERTIFICATE,
        SP_ACS_BINDING.value,
        SP_ACS_URL)
