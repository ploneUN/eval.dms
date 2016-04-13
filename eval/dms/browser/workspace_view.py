from five import grok
from plone.directives import dexterity, form
from eval.dms.content.workspace import IWorkspace
from Products.CMFCore.utils import getToolByName

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IWorkspace)
    grok.require('zope2.View')
    grok.template('workspace_view')
    grok.name('view')

    @property
    def catalog(self):
    	return getToolByName(self.context, 'portal_catalog')

    def contents(self):
    	context = self.context
    	catalog = self.catalog
    	path = '/'.join(context.getPhysicalPath())
    	results = []
    	brains = catalog.searchResults(path={'query': path, 'depth':1},
    					portal_type=('File','Image'),
    					sort_on='id', 
    					sort_order='reverse' )
    	return brains

    def searchedValue(self, name=None):
        result = 0
        if self.request.form.has_key('data'):
            form = self.request.form
            result = form[name]
        return result
