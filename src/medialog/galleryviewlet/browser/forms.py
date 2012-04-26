from zope.formlib import form
from zope.interface import implements
from zope.component import adapts
import zope.lifecycleevent
from zope.component import getMultiAdapter

from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from plone.app.form import base as ploneformbase

from medialog.galleryviewlet.interfaces import IGalleryloaderSettings 
from medialog.galleryviewlet import galleryviewletMessageFactory as _
from medialog.galleryviewlet.settings import GalleryloaderSettings
  

class GalleryloaderSettingsForm(ploneformbase.EditForm):
    """
    The page that holds all the settings
    """
    form_fields = form.FormFields(IGalleryloaderSettings)
      
    label = _(u'heading_galleryloader_settings_form', default=u"Galleryloader Settings")
    description = _(u'description_galleryloader_settings_form', default=u"Configure the parameters for this file.")
    form_name = _(u'title_galleryloader_settings_form', default=u"Galleryloader settings")
    
    