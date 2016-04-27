from five import grok
from plone.directives import dexterity, form
from eval.workspace.content.config import IConfig

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IConfig)
    grok.require('zope2.View')
    grok.template('config_view')
    grok.name('view')

