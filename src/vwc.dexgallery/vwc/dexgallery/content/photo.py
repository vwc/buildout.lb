from zope.interface import Interface
from plone.indexer import indexer
from plone.directives import form
from plone.namedfile.field import NamedBlobImage
from plone.app.textfield import RichText
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from vwc.dexgallery import _

class IPhoto(form.Schema):
    """
    A photo appearing in the image gallery.
    """
    image = NamedBlobImage(
        title = _(u'Photo'),
        )
    
    caption = RichText(
        title = _(u'Caption'),
        required = False,
        )
    
    tags = RelationList(
        title = _(u'Tags'),
        default = [],
        value_type=RelationChoice(
            title = _(u'Tag'),
            source = ObjPathSourceBinder(
                navigation_tree_query = {'path': {'query':'/'}},
                portal_type = 'Document',
                ),
            ),
        required = False,
        )

@indexer(Interface)
def null_indexer(obj):
    raise AttributeError

@indexer(IPhoto)
def photo_tags(obj):
    tags = set()
    for relation in obj.tags:
        if relation.isBroken():
            continue
        tags.add(relation.to_object.Title())
    return list(tags)

@indexer(IPhoto)
def SearchableText(obj):
    return ' '.join([obj.Title(), obj.Description(), obj.caption.output])
