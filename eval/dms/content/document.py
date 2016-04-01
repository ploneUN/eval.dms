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

from eval.dms import MessageFactory as _


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
    form.widget(multifile=MultiFileFieldWidget)
    multifile = schema.List(
            title=_(u"Document"),
            required=False,
            value_type=NamedBlobFile(),
        )
    pass

alsoProvides(IDocument, IFormFieldProvider)
