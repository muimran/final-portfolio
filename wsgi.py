import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/root/customer-account-automation/")

from myapp import app as application

if _name_ == "_main_":
    application.run()