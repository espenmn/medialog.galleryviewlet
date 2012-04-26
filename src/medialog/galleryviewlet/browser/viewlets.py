from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class GalleryViewlet(ViewletBase):
    render = ViewPageTemplateFile('galleryviewlet.pt')


