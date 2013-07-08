from five import grok
from zope import schema
from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from plone.directives import form, dexterity

from balzer.projects import _

class IProjectList(form.Schema):
    """
    A folderish content type listing reference projects.
    """
    
    # -*- Your Zope schema definitions here ... -*-