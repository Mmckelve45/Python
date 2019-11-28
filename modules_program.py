#importing from another .py file (modules)
from modules import my_func
my_func()

#importing from a package
from MyMainPackage import some_main_script
#importing from subpackage
from MyMainPackage.SubPackage import mysubscript

some_main_script.report_main()

mysubscript.sub_report()

