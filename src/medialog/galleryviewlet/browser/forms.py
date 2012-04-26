from zope.formlib import form
from zope.interface import implements
from zope.component import adapts
import zope.lifecycleevent
from zope.component import getMultiAdapter

from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from plone.app.form import base as ploneformbase

from medialog.galleryviewlet.interfaces import IGalleryviewletSettings 
from medialog.galleryviewlet import galleryviewletMessageFactory as _
from medialog.galleryviewlet.settings import GalleryviewletSettings
  

class GalleryviewletSettingsForm(ploneformbase.EditForm):
    """
    The page that holds all the settings
    """
    form_fields = form.FormFields(IGalleryviewletSettings)
      
    label = _(u'heading_galleryviewlet_settings_form', default=u"Galleryviewlet Settings")
    description = _(u'description_galleryviewlet_settings_form', default=u"Configure the parameters for this file.")
    form_name = _(u'title_galleryviewlet_settings_form', default=u"Galleryviewlet settings")
    
    