from zope.interface import Interface, Attribute
from zope import schema
from medialog.galleryviewlet import galleryviewletMessageFactory  as _
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from OFS.interfaces import IItem


class IGalleryloaderLayer(Interface):
    """
    marker interface for galleryloader layer
    
    """
    
class IGalleryloaderUtilProtected(Interface):

    def enable():
        """
        enable galleryloader on this object
        """

    def disable():
        """
        disable galleryloader on this object
        """
        self.request.response.redirect(self.context.absolute_url())


class IGalleryloaderUtil(Interface):

    def enabled():
        """
        checks if galleryloader is enabled  
        """

    def view_enabled():
        """
        checks if the galleryloader is selected
        """

class IGalleryloaderSettings(Interface):
    """
    The actual gallery settings
    """
    
    width = schema.TextLine(
        title=_(u"label_width_title_galleryloader_setting", default=u"Gallery"),
        description=_(u"label_width_description_galleryloader_setting", 
            default=u"The path to the gallery."),
        default=u"600px",
        required=True
    )

