import os
from StringIO import StringIO
from App.Common import package_home
from cgi import FieldStorage
from ZPublisher.HTTPRequest import FileUpload

#loads a file
def loadxmlfile(rel_filename):
    ctype='text/xml'
    home = package_home(globals())
    filename = os.path.sep.join([home, rel_filename])
    data = open(filename, 'r').read()
    fp = StringIO(data)
    fp.seek(0)

    header_filename = rel_filename.split('/')[-1]
    env = {'REQUEST_METHOD':'PUT'}
    headers = {'content-type' : ctype,
                'content-length': len(data),
                'content-disposition':'attachment; filename=%s' % (header_filename,)}

    fs = FieldStorage(fp=fp, environ=env, headers=headers)
    return FileUpload(fs)