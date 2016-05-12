from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer

from eval.workspace import MessageFactory as _
from zope.app.container.interfaces import IObjectAddedEvent
from zope.container.interfaces import INameChooser
from zope.component import getUtility, getMultiAdapter
from plone.portlets.interfaces import IPortletManager, IPortletAssignmentMapping, IPortletRetriever
from eval.workspace.portlet import mydocs_portlet


# Interface class; used to define content-type schema.

class IWorkspace(form.Schema, IImageScaleTraversable):
    """
    Workspaces
    """
    pass

alsoProvides(IWorkspace, IFormFieldProvider)

@grok.subscribe(IWorkspace, IObjectAddedEvent)
def _createObject(context, event):
    column = getUtility(IPortletManager, name=u'plone.leftcolumn', context=context)
    manager = getMultiAdapter((context, column,), IPortletAssignmentMapping)
    assignment = mydocs_portlet.Assignment()
    chooser = INameChooser(manager)
    assignment.button_label = 'My Documents Portlet'
    manager[chooser.chooseName(None, assignment)] = assignment
