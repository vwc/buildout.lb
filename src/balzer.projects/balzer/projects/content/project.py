from five import grok
from zope import schema
from plone.namedfile.field import NamedBlobImage
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from plone.directives import form, dexterity

from balzer.projects import _

class IProject(form.Schema):
    """
    A reference project.
    """
    
    # -*- Your Zope schema definitions here ... -*-

    form.widget(summary="plone.app.z3cform.wysiwyg.WysiwygFieldWidget")
    summary = schema.Text(
        title=_(u"Project Summary"),
        description=_(u"Enter a summary of the project goals."),
        required=False,
    )

    image = NamedBlobImage(
        title=_(u"Image"),
        description=_(u"Upload an image that will be shown in listings and search results."),
        required=False,
    )

