from five import grok
from plone.directives import dexterity, form
from eval.workspace.content.document_file import DocumentFile

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(DocumentFile)
    grok.require('zope2.View')
    grok.template('document_file_view')
    grok.name('view')
