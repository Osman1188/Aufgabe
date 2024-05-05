import cherrypy
from mako.template import Template
from app.database import Database_cl

class Application_cl(object):
    def __init__(self):
        self.databaseHandler = Database_cl()

    @cherrypy.expose
    def index(self):
        # The database handler is used to read data from a CSV file.
        data = self.databaseHandler.readCsv()
        # 'students' variable is passed to the template. The 'students'
        # variable contains the data read from the CSV file. The
        return Template(filename="content/index.tpl").render(students=data)

