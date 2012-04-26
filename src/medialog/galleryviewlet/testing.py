from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class MedialogGalleryviewlet(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import medialog.galleryviewlet
        xmlconfig.file('configure.zcml',
                       medialog.galleryviewlet,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'medialog.galleryviewlet:default')

MEDIALOG_GALLERYVIEWLET_FIXTURE = MedialogGalleryviewlet()
MEDIALOG_GALLERYVIEWLET_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(MEDIALOG_GALLERYVIEWLET_FIXTURE, ),
                       name="MedialogGalleryviewlet:Integration")