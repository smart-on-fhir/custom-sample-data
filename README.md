# TESTING - DO NOT USE

To have custom data added to the SMART Sandbox servers, please submit a pull request to this repository that adds a JSON FHIR bundle with a new patient resource and the rest of your data referencing that patient. The file should be placed into the ```fhir-resources``` folder, and ids in the resource must not match exsiting ids in the SMART Sandbox, and should be prefixed with a word unique to your organization or application (e.g. myapp-patient-1). 

Please post questions on our google group: https://groups.google.com/forum/#!forum/smart-on-fhir