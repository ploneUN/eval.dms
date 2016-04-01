from five import grok
from plone.directives import dexterity, form
from eval.dms.content.workspace import IWorkspace

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IWorkspace)
    grok.require('zope2.View')
    grok.template('workspace_view')
    grok.name('view')

