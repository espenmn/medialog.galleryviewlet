from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class GalleryLoader(ViewletBase):
    render = ViewPageTemplateFile('galleryloader.pt')


