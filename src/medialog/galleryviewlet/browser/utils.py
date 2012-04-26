from zope.interface import implements, alsoProvides, noLongerProvides
from Products.Five.browser import BrowserView
from ..interfaces import IGalleryloaderUtilProtected, \
    IGalleryloaderUtil, IGalleryloader
from Products.CMFCore.utils import getToolByName

from plone.app.customerize import registration
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.component import getMultiAdapter

try:
    #For Zope 2.10.4
    from zope.annotation.interfaces import IAnnotations
except ImportError:
    #For Zope 2.9
    from zope.app.annotation.interfaces import IAnnotations


class GalleryloaderUtilProtected(BrowserView):
    """
    a protected traverable utility for 
    enabling and disabling galleryloader
    """
    implements(IGalleryloaderUtilProtected)
    def enable(self):
        utils = getToolByName(self.context, 'plone_utils')

        if not IGalleryloader.providedBy(self.context):
            alsoProvides(self.context, IGalleryloader)
            self.context.reindexObject(idxs=['object_provides'])
            utils.addPortalMessage("Gallery added.")
            self.request.response.redirect(self.context.absolute_url())
            
        else:  
            self.request.response.redirect(self.context.absolute_url())
        
    def disable(self):
        utils = getToolByName(self.context, 'plone_utils')
        
        if IGalleryloader.providedBy(self.context):
            noLongerProvides(self.context, IGalleryloader)
            self.context.reindexObject(idxs=['object_provides'])
            
            #now delete the annotation
            annotations = IAnnotations(self.context)
            metadata = annotations.get('medialog.galleryloader', None)
            if metadata is not None:
                del annotations['medialog.galleryloader']
                
            utils.addPortalMessage("Galleryloader removed.")
            
        self.request.response.redirect(self.context.absolute_url())
        
class GalleryloaderUtil(BrowserView):
    """
    a public traverable utility that checks if it is enabled etc
    more work to do here
    """
    implements(IGalleryloaderUtil)

    def enabled(self):
        return IGalleryloader.providedBy(self.context)    


    def view_enabled(self):
        utils = getToolByName(self.context, 'plone_utils')
        return True

    def should_include(self):
        return self.enabled() or self.view_enabled()
        
    
