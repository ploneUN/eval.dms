from five import grok
from plone.directives import dexterity, form
from Products.CMFCore.interfaces import IContentish

grok.templatedir('templates')

class faceted_regional_document_listing(grok.View):
    grok.context(IContentish)
    grok.require('zope2.View')
    
    def author_fullname(self, username=None):
        if username:
            membership = self.context.portal_membership.getMemberById(username)
            return membership.getProperty('fullname')
        return ''