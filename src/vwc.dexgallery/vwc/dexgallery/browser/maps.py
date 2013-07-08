from zope.interface import implements
from zope.component import adapts
from Products.Maps.interfaces import IMarker, IMapView, IRichMarker
from Products.Maps.adapters import BaseMap
from Products.Maps.browser.map import DefaultMapView
from vwc.dexgallery.behavior.geolocation import IGeolocatableMarker, IGeolocatable
from vwc.dexgallery.content.photogallery import IPhotoGallery

class GeolocatableMap(BaseMap):
    adapts(IGeolocatableMarker)
    
    def getMarkers(self):
        return GeolocatableMarker(self)

class PhotoGalleryMapView(DefaultMapView):
    implements(IMapView)
    adapts(IPhotoGallery)

    def getMarkers(self):
        if self.map is None:
            return
        for x in self.map.getMarkers():
            if x.longitude and x.latitude:
                yield IRichMarker(x)

class GeolocatableMarker(object):
    implements(IMarker)
    adapts(IGeolocatableMarker)

    def __init__(self, context):
        self.context = context

    @property
    def latitude(self):
        return IGeolocatable(self.context).geolocation.latitude

    @property
    def longitude(self):
        return IGeolocatable(self.context).geolocation.longitude

    @property
    def title(self):
        return self.context.Title()

    @property
    def description(self):
        return self.context.Description()

    @property
    def layers(self):
        return ()

    @property
    def icon(self):
        return "Red Marker"

    @property
    def url(self):
        return self.context.absolute_url()
