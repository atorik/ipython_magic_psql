import re
import sys
import pexpect
from pexpect import replwrap

from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)


class PsqlWrapper:
    def __init__(self, port, dbname):

        port = port
        dbname = dbname
        prompt = "postgres=# "  # TODO: consider normal user
        psql_cmd = 'psql -p ' + port + ' -d ' + dbname

        self.psql = replwrap.REPLWrapper(psql_cmd, prompt, None)

    def exec_query(self, query):
        query = query.replace('\n','')
        print(self.psql.run_command(query))

    # TODO: need exit
    # def exit():


@magics_class
class PsqlMagics(Magics):
    def __init__(self, shell):
        super(PsqlMagics, self).__init__(shell)

        self.cons = {}

#    @line_magic('psql')
#    def exec_line(self, line):
#        result = self.psql.exec_query(line)
#        return result

    @cell_magic('psql')
    def exec_cell(self, con_info, cell):

        first_con = re.search('con_name:(\w+) user:(\w+) port:(\w+)', con_info)

        if first_con:
            con_name = first_con.group(1)
            user = first_con.group(2)
            port = first_con.group(3)

            if not con_name in self.cons.keys():
                self.cons[con_name] = PsqlWrapper(port, user)

            result = self.cons[con_name].exec_query(cell)

        elif con_info in self.cons.keys():
            result = self.cons[con_info].exec_query(cell)

        else:
            print("Not allowed format.")

        return result


def load_ipython_extension(ip):
    ip.register_magics(PsqlMagics)
