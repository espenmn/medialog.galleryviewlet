from zope.interface import implements, alsoProvides, noLongerProvides
from Products.Five.browser import BrowserView
from medialog.galleryviewlet.interfaces import IGalleryviewletUtilProtected, \
    IGalleryviewletUtil, IGalleryviewlet
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


class GalleryviewletUtilProtected(BrowserView):
    """
    a protected traverable utility for 
    enabling and disabling galleryviewlet
    """
    implements(IGalleryviewletUtilProtected)
    def enable(self):
        utils = getToolByName(self.context, 'plone_utils')

        if not IGalleryviewlet.providedBy(self.context):
            alsoProvides(self.context, IGalleryviewlet)
            self.context.reindexObject(idxs=['object_provides'])
            utils.addPortalMessage("Galleryviewlet added.")
            self.request.response.redirect(self.context.absolute_url())
            
        else:  
            self.request.response.redirect(self.context.absolute_url())
        
    def disable(self):
        utils = getToolByName(self.context, 'plone_utils')
        
        if IGalleryviewlet.providedBy(self.context):
            noLongerProvides(self.context, IGalleryviewlet)
            self.context.reindexObject(idxs=['object_provides'])
            
            #now delete the annotation
            annotations = IAnnotations(self.context)
            metadata = annotations.get('medialog.galleryviewlet', None)
            if metadata is not None:
                del annotations['medialog.galleryviewlet']
                
            utils.addPortalMessage("Galleryviewlet removed.")
            
        self.request.response.redirect(self.context.absolute_url())
        
class GalleryviewletUtil(BrowserView):
    """
    a public traverable utility that checks if it is enabled etc
    more work to do here
    """
    implements(IGalleryviewletUtil)

    def enabled(self):
        return IGalleryviewlet.providedBy(self.context)    


    def view_enabled(self):
        utils = getToolByName(self.context, 'plone_utils')
        return True

    def should_include(self):
        return self.enabled() or self.view_enabled()
        
    
