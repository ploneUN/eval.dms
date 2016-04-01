from zope.interface import implements
from Products.CMFQuickInstallerTool.interfaces import INonInstallable
from five import grok
from collective.grok import gs
from zope.i18nmessageid import MessageFactory

# Set up the i18n message factory for our package
MessageFactory = MessageFactory('eval.dms')

_ = MessageFactory

class HiddenProducts(grok.GlobalUtility):
    """This hides the upgrade profiles from the quick installer tool."""
    implements(INonInstallable)
    grok.name('eval.dms.upgrades')

    def getNonInstallableProducts(self):
        return [
            'eval.dms.upgrades',
        ]

gs.profile(name=u'default',
           title=u'eval.dms',
           description=_(u''),
           directory='profiles/default')
