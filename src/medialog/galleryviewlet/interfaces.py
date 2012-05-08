from zope.interface import Interface, Attribute
from zope import schema
from medialog.galleryviewlet import galleryviewletMessageFactory  as _
from OFS.interfaces import IItem

 
import urllib
from plone.memoize.instance import memoize

 
from zope.component import getMultiAdapter
 
#from collective.plonetruegallery.vocabularies import \
#    GallerySearchabelTextSourceBinder

#from collective.plonetruegallery.utils import getGalleryAdapter
 
 
class IGalleryviewletLayer(Interface):
    """
    marker interface for galleryviewlet layer
    
    """
    
class IGalleryviewlet(Interface):
    """
    marker interface for content types that can use the viewlet 
    """

    
class IGalleryviewletUtilProtected(Interface):

    def enable():
        """
        enable galleryviewlet on this object
        """

    def disable():
        """
        disable galleryviewlet on this object
        """


class IGalleryviewletUtil(Interface):

    def enabled():
        """
        checks if galleryviewlet is enabled  
        """

    def view_enabled():
        """
        checks if the galleryviewlet is selected
        """

class IGalleryviewletSettings(Interface):
    """
    The actual galleryviewlet settings
    """
    
    gallerypath = schema.TextLine(
        title=_(u"label_width_title_galleryviewlet_setting", default=u"Which Gallery"),
        description=_(u"label_width_description_galleryviewlet_setting", 
        default=u"The path to the gallery you want to  show."),
        required=True)
