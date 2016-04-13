from five import grok
from plone.directives import dexterity, form
from eval.dms.content.workspace import IWorkspace
from Products.CMFCore.utils import getToolByName

grok.templatedir('templates')

class mydocs_view(dexterity.DisplayForm):
    grok.context(IWorkspace)
    grok.require('zope2.View')
    grok.template('mydocs_view')

    @property
    def catalog(self):
    	return getToolByName(self.context, 'portal_catalog')

    @property
    def form(self):
        request = self.request
        return request.form

    def contents(self):
    	context = self.context
    	catalog = self.catalog
        form = self.form
    	path = '/'.join(context.getPhysicalPath())
    	results = []
    	brains = catalog.searchResults(path={'query': path, 'depth':1},
                                        portal_type=('File','Image'),
                    					sort_on='id', 
                    					sort_order='reverse')

        status = ''
        author = ''
        file_type = ''
        title = ''
        if form:
            title = form['title'].lower()
            status = form['status'].lower()
            file_type = form['file_type'].lower()
            author = form['author'].lower()

        for brain in brains:
    	    obj = brain.getObject()
            if (status in ['all', '', brain.review_state] and
                (author in ['', None, 'all'] or author in brain.Creator) and
                (file_type in ['', None, 'all'] or file_type in obj.getContentType()) and
                (title in ['', None, 'all'] or title in obj.title.lower())):
                results.append({
                    'title' : obj.title,
    				'id': brain.getId, 
                    'author': brain.Creator,
                    'filename': obj.getFilename(),
                    'file_type': obj.getContentType(),
    				'path': brain.getURL(),
				    'status':brain.review_state})
    	return results

    def searchedValue(self, name=None):
        result = 0
        form = self.form
        if form.has_key('data'):
            result = form[name]
        return result
