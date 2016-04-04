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
from plone.autoform.directives import write_permission, read_permission
from plone.formwidget.multifile import MultiFileFieldWidget
from collective import dexteritytextindexer
from Products.CMFCore.utils import getToolByName

from eval.dms import MessageFactory as _
from zope.app.container.interfaces import IObjectAddedEvent
from plone.autoform.directives import write_permission, read_permission

# Interface class; used to define content-type schema.

class IDocument(form.Schema, IImageScaleTraversable):
    """
    Document
    """

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
        title = _(u"Title"),
        required = False,
    )

    dexteritytextindexer.searchable('multifile')
    write_permission(multifile='cmf.ReviewPortalContent')
    read_permission(multifile='cmf.ReviewPortalContent')
    multifile = NamedBlobFile(
        title=_(u"Document"),
        description=_(u"Please attach a file"),
        required=False,
        )
    pass

alsoProvides(IDocument, IFormFieldProvider)

@grok.subscribe(IDocument, IObjectAddedEvent)
def _createObject(context, event):
    #id generation (Format: DOCUMENT-X)
    parent = context.aq_parent
    id = context.getId()
    catalog = getToolByName(context, 'portal_catalog')
    path = '/'.join(parent.getPhysicalPath())
    brains = catalog.unrestrictedSearchResults(path={'query': path, 'depth' : 1}, portal_type='ppp.dms.document')
    if len(brains) > 1:
        brains = [int(brain.getId.split('-')[1]) for brain in brains if 'DOCUMENT' in  brain.getId]
        context_id = int(max(brains))+1
    else:
        context_id = 1
    context_id = 'DOCUMENT-' + str(context_id)
    parent.manage_renameObject(id, context_id) 
    context.reindexObject()
    return
