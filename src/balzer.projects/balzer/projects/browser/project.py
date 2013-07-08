
from five import grok
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from plone.dexterity.interfaces import IDexterityContent

from balzer.projects.content.project import IProject

class View(grok.View):
    grok.context(IProject)
    grok.require('zope2.View')
    grok.name('view')
