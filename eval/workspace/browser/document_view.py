from five import grok
from plone.directives import dexterity, form
from eval.workspace.content.document import IDocument

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IDocument)
    grok.require('zope2.View')
    grok.template('document_view')
    grok.name('view')

