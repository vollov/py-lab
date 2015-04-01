import argparse, sys

class HedgingArgParser(argparse.ArgumentParser):
    
    def format_usage(self):
        usage_line = argparse.ArgumentParser.format_usage()
        return usage_line.replace('__init__.py', 'run.bat')
    
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)
        
def run(run_name, task_name):
    print 'run application with {} {}'.format(run_name, task_name)

if __name__=='__main__':    
    parser = HedgingArgParser(prog='run.bat', description='Application to move hedging files.')
    parser.add_argument('run_name', metavar='run_name',  nargs=1,
                   help='the name of this run, run_name = '\
                   +' [base|IR-100|IR+100|IR-20|IR+20|Eqty-5'\
                   +'|Eqty+5|Eqty-10|Eqty+10|Eqty-30|EqtyIR]')
    
    parser.add_argument('task_name', metavar='task_name',  nargs=1,
                   help='task name of this run, task_name = '\
                   +' [stage_to_secure|secure_to_prod|postrun]')
    args = parser.parse_args()
    run_name = parser.get_default('run_name')
    task_name = parser.get_default('task_name')
#    if run_name is None or task_name is None:
#        print "run.bat run_name task_name"
#        print "task_name = [stage_to_secure | secure_to_prod | postrun]"
#    else:
    run(run_name, task_name)