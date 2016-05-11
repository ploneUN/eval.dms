from five import grok
from plone.directives import dexterity, form
from eval.workspace.content.workspace import IWorkspace
from Products.CMFCore.utils import getToolByName
from plone import api

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
    					portal_type=('File','Image', 'eval.workspace.document_file'),
    					sort_on='id', 
    					sort_order='reverse' )
    	return brains

    def searchedValue(self, name=None):
        result = 0
        if self.request.form.has_key('data'):
            form = self.request.form
            result = form[name]
        return result

    def roles(self, obj=None):
        current = str(api.user.get_current())
        roles = api.user.get_roles(username=current, obj= obj)
        allowed =  ['Owner','Manager', 'Administrator'] 
        return any((True for x in roles if x in allowed))
