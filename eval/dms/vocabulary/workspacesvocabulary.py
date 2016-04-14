from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource
from Products.CMFCore.utils import getToolByName
from eval.dms.content.workspace import IWorkspace

class Workspaces(grok.GlobalUtility):
    grok.name('eval.dms.workspacesvocabulary')
    grok.implements(IVocabularyFactory)
    
    def __call__(self, context):
        catalog = getToolByName(context, 'portal_catalog')
        brains = catalog(object_provides=IWorkspace.__identifier__)
        path = context.getPhysicalPath()[-1]
        #items = [SimpleTerm(value=brain.UID, token=brain.UID, title=brain.Title) for brain in brains if set(brain.getPath().split('/')[:-2]).issubset(path) and brain.review_state == 'active']
        items = [SimpleTerm(value=brain.UID, token=brain.UID, title=brain.Title) for brain in brains if path in brain.getPath().split('/')[:-1]]
        return SimpleVocabulary(items)