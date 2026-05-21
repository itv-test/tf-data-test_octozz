import sys
import os
import re

#set module naming pattern to kebab-case
module_naming_pattern = re.compile(f"^([a-z]+_?)+")

# Get env vars
MODULE_NAME = os.environ['GHA_MODULE_NAME']
MODULE_DESCRIPTION = os.environ['GHA_MODULE_DESCRIPTION']

# Check name matches required pattern
if not module_naming_pattern.fullmatch(MODULE_NAME):
    print(f"Error: The module name must be in snake_case, e.g. analytics_hub. Supplied name - {MODULE_NAME}")
    sys.exit(1)
else:
    print(f"Success: Module name ({MODULE_NAME}) matches the required naming pattern")
    pass

#check for forbidden characters in description
if ";" in MODULE_DESCRIPTION:
    print(f"Error: We're sorry but ';' cannot be used in the description. Please use a comma instead.")
    sys.exit(1)
