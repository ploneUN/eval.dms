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
#from plone.multilingualbehavior.directives import languageindependent
from plone.autoform.directives import write_permission, read_permission
from plone.formwidget.multifile import MultiFileFieldWidget
from collective import dexteritytextindexer

from eval.workspace import MessageFactory as _

from zope.app.container.interfaces import IObjectAddedEvent
from zope.lifecycleevent.interfaces import IObjectModifiedEvent
from Products.CMFCore.utils import getToolByName
from collective import dexteritytextindexer
from collective.dexteritytextindexer.utils import searchable

from plone.app.contenttypes.content import File

# Interface class; used to define content-type schema.

class DocumentFile(File):
   """defines class of document-file from IFile"""

