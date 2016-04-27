from five import grok
from zope.formlib import form
from zope import schema
from zope.interface import implements
from zope.component import getMultiAdapter
from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget
import datetime
import calendar
from plone import api

grok.templatedir('templates')

class IContentNavigation(IPortletDataProvider):

    portlet_title = schema.TextLine(
            title = u"Search Add App Portlet Title",
            required=False,
        )

class Assignment(base.Assignment):
    implements(IContentNavigation)
    
    def __init__(self, portlet_title=None):
        self.portlet_title = portlet_title

    @property
    def title(self):
        return "Search Portlet"

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('templates/searchevalworkspaceportlet.pt')
    def __init__(self, context, request, view, manager, data):
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager
        self.data = data
        
    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def path(self):
        return '/'.join(self.context.getPhysicalPath())
        
    def contents(self):
        return self.data

    #returns values on status search field;  
    def status(self):
        catalog = self.catalog
        path = self.path
        status = [{'status': 'All'}]
        brains = catalog.searchResults(path={'query': path, 'depth' : 1})
        for brain in brains:
            obj = brain.getObject()
            #checks if status is not in the list yet
            if not any(d['status'] == brain.review_state for d in status):
                status.append({'status':brain.review_state})
        return status

    #returns true if user has editor, reviewer, manager or admin role            
    def roles(self):
        current = str(api.user.get_current())
        roles = ''
        if current != 'Anonymous User':
            roles = api.user.get_roles(username=current, obj= self.context)
        allowed =  ['Editor','Reviewer','Manager', 'Administrator'] 
        return any((True for x in roles if x in allowed))

    #returns form value request
    def searched_value(self, name=None):
        result = ''
        if self.request.form.has_key('project'):
            form = self.request.form
            result = form[name]
        return result

class AddForm(base.AddForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"EVAL Workspace Search Portlet"
    description = ''
    
    def create(self, data):
        assignment = Assignment()
        form.applyChanges(assignment, self.form_fields, data)
        return assignment

class EditForm(base.EditForm):
    form_fields = form.Fields(IContentNavigation)
    label = u"Edit Search Portlet"
    description = ''
