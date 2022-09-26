Jenkins_Data_Extract.py DOCUMENTATION:
-------------------------------------

*INSTALLATION 1.1
-------------------------------------

	* This script runs in Python 3.8
	* Python imports(packages) required:
		-requests
		-python-jenkins
		-Create_csv_file.py (created custom module, should be include in the this script's folder)

	JENKINS DEPENDENCIES:
	--------------------
		The following jenkins plug-ins need to be on installed in order for the script to work:
			-pyenv pipeline plug-in
			-timestamper plug-in

*OTHER EXPLANATIONS 1.2
--------------------------------------
	*Create_csv_file.py import: This python module has two functions that are necesary in order to run the main script.
		*fucntions:
			*create_csv(data): Takes the fetched data from the jenkins console aquired from the main script. It creates
					 a csv file and appens the data. The path to this file has to be specified.
			*append_to_csv(data): If the csv file already exists, it appends the given data.
			


*TO DO LIST 1.3
-------------------------------------
*Add PowerBI functionality
