from five import grok
from plone.directives import dexterity, form
from eval.workspace.content.eval_workspace_app import IEVALWorkspaceApp

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IEVALWorkspaceApp)
    grok.require('zope2.View')
    grok.template('eval_workspace_app_view')
    grok.name('view')

