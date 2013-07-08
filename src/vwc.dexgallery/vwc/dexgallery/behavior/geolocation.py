from persistent import Persistent
from zope.annotation import factory
from zope.interface import alsoProvides, implements
from zope.component import adapts

from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider
from plone.formwidget.geolocation import Geolocation, GeolocationField

from vwc.dexgallery import _

from Products.Maps.interfaces import IMapEnabled

# form field for geolocation behavior

class IGeolocatable(form.Schema):
    geolocation = GeolocationField(title = _(u'Geolocation'))
alsoProvides(IGeolocatable, IFormFieldProvider)

# marker for geolocatable content

class IGeolocatableMarker(IMapEnabled):
    pass

# geolocation storage in annotation

class GeolocatableAnnotation(Persistent):
    implements(IGeolocatable)
    adapts(IDexterityContent)

    def __init__(self):
        self.geolocation = Geolocation(0, 0)
Geolocatable = factory(GeolocatableAnnotation)
