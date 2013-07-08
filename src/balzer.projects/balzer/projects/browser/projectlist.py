
from five import grok
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from plone.dexterity.interfaces import IDexterityContent

from balzer.projects.content.project import IProject
from balzer.projects.content.projectlist import IProjectList

class View(grok.View):
    grok.context(IProjectList)
    grok.require('zope2.View')
    grok.name('view')
    
    
    def teststring(self):
        context = aq_inner(self.context)
        return 'Test String Dummy'
    
    def projects(self):
        """ Query the catalog to construct a list of Projects in this folder and
            return a dictionary of values.
        """
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        return catalog(object_provides=IProject.__identifier__,
                                path='/'.join(context.getPhysicalPath()),
                                review_state='published')
