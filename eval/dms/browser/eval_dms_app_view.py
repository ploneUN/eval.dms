from five import grok
from plone.directives import dexterity, form
from eval.dms.content.eval_dms_app import IEVALDMSApp

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IEVALDMSApp)
    grok.require('zope2.View')
    grok.template('eval_dms_app_view')
    grok.name('view')

