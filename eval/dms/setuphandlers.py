from collective.grok import gs
from eval.dms import MessageFactory as _

@gs.importstep(
    name=u'eval.dms', 
    title=_('eval.dms import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('eval.dms.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
