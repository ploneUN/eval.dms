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

from plone.dexterity.utils import createContentInContainer, createContent
from zope.app.container.interfaces import IObjectAddedEvent
from zope.component import getMultiAdapter
from eval.workspace.loadxmlfile import loadxmlfile
# Interface class; used to define content-type schema.

class IEVALWorkspaceApp(form.Schema, IImageScaleTraversable):
    """
    Regional and EVAL HQ Repository
    """
    pass

alsoProvides(IEVALWorkspaceApp, IFormFieldProvider)

@grok.subscribe(IEVALWorkspaceApp, IObjectAddedEvent)
def _createObject(context, event):
    #auto create config and workspace folders on ppp workspace
    # createContentInContainer(context, 'eval.workspace.config', checkConstraints=False, title='Config')
    # createContentInContainer(context, 'eval.workspace.workspace', checkConstraints=False, title='Workspace')
    
    #auto enable faceted navigation
    faceted = getMultiAdapter((context, context.REQUEST), name=u'faceted_subtyper')
    faceted.enable()

    #auto import workspace-app.xml config
    query = {'import_button': 'Import',
            'import_file': loadxmlfile('/profiles/default/eval_workspace.xml'),
            'redirect': ''}
    view = context.unrestrictedTraverse('@@faceted_exportimport')
    view(**query)
    context.reindexObject()




