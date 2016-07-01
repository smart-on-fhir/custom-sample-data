# Using the sample data validator

1. Make sure you have a copy of Python 2.x installed 
2. Clone this repository
3. Run ```pip install -r requirements.txt``` to install the Python dependencies
4. Add a JSON FHIR bundle with your data to the ```fhir-resources``` folder
5. Run ```python validate.py```


# Add custom patients to the SMART Sandbox

Once your files validate successfully, please submit a pull request to this repository that adds a JSON FHIR bundle with a new patient resource and the rest of your data referencing that patient. The file should be placed into the ```fhir-resources``` folder. Ids in the resource must not match exsiting ids in the SMART Sandbox, and should be prefixed with a word unique to your organization or application (e.g. myapp-patient-1).