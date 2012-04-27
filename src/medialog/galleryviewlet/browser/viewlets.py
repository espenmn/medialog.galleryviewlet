from Acquisition import aq_inner
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoize
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implements, Interface
from Products.CMFCore.utils import getToolByName


from medialog.galleryviewlet import galleryviewletMessageFactory as _
from medialog.galleryviewlet.settings import GalleryviewletSettings
from medialog.galleryviewlet.settings import IGalleryviewletSettings


#dont know if all this is needed
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName



class GalleryViewlet(ViewletBase):
    render = ViewPageTemplateFile('galleryviewlet.pt')
    
    implements(IGalleryviewletSettings)

    def gallery(self):
		context=self.context
		self.settings = GalleryviewletSettings(context)
		return u"""
		<div tal:replace="structure context/%(gallerypath)s/@@placegalleryview">gallery here</div>
""" % {'gallerypath': self.settings.gallerypath}