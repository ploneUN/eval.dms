from collective.grok import gs
from eval.workspace import MessageFactory as _

@gs.importstep(
    name=u'eval.workspace', 
    title=_('eval.workspace import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('eval.workspace.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
