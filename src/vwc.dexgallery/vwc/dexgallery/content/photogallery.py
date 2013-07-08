from five import grok
from zope import schema
from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from plone.directives import form, dexterity

from vwc.dexgallery import _

class IPhotoGallery(form.Schema):
    """
    A Photo Gallery with geotagging and Map Integration
    """
    
    # -*- Your Zope schema definitions here ... -*-