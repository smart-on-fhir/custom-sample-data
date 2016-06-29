import json
import sys
import os
from fhirclient.models.fhirabstractbase import FHIRValidationError
from fhirclient.models.fhirelementfactory import FHIRElementFactory

def validateResource(path, basePath):
  bundleHeader = "="*80 + "\n" + path.replace(basePath, "") + "\n" + "="*80
  print bundleHeader

  try:
    with open(path) as dataFile:
      resource = json.loads(dataFile.read())

  except ValueError as e: 
    print "Error parsing JSON:\n{0}".format(e)
    return 1

  if "resourceType" not in resource:
    print "Resource has no resourceType"
    return 1

  try:
    FHIRElementFactory.instantiate(resource['resourceType'], resource)
  except FHIRValidationError as e:
    print(e)
    return 1

  print "Valid"
  return 0

def validateDir(basePath):
  failStatus = 0
  for root, dirs, files in os.walk(basePath):
    for fileName in files:
      if fileName[0] is ".": continue
      filePath = os.path.join(root, fileName)
      result = validateResource(filePath, basePath)
      failStatus = max(failStatus, result)

  return failStatus

targetDir = sys.argv[1] if len(sys.argv) > 1 else "./fhir-resources/"
result = validateDir(targetDir)
sys.exit(result)

