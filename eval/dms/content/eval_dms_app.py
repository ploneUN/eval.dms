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

from eval.dms import MessageFactory as _

from plone.dexterity.utils import createContentInContainer, createContent
from zope.app.container.interfaces import IObjectAddedEvent
from zope.component import getMultiAdapter
from eval.dms.loadxmlfile import loadxmlfile
# Interface class; used to define content-type schema.

class IEVALDMSApp(form.Schema, IImageScaleTraversable):
    """
    Regional and EVAL HQ Repository
    """
    pass

alsoProvides(IEVALDMSApp, IFormFieldProvider)

@grok.subscribe(IEVALDMSApp, IObjectAddedEvent)
def _createObject(context, event):
    #auto create config and workspace folders on ppp dms
    createContentInContainer(context, 'eval.dms.config', checkConstraints=False, title='Config')
    createContentInContainer(context, 'eval.dms.workspace', checkConstraints=False, title='Workspace')
    
    #auto enable faceted navigation
    faceted = getMultiAdapter((context, context.REQUEST), name=u'faceted_subtyper')
    faceted.enable()

    #auto import dms-app.xml config
    query = {'import_button': 'Import',
            'import_file': loadxmlfile('/profiles/default/eval_dms.xml'),
            'redirect': ''}
    view = context.unrestrictedTraverse('@@faceted_exportimport')
    view(**query)
    context.reindexObject()




