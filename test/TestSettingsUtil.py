import unittest
import sys
import os
# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import settingsUtil as su
import json
import os

class TestSettingsUtil(unittest.TestCase):

    def setUp(self):
        self.empty_settings_file = 'data/empty_settings.RC0'
        self.temp_output_file = 'data/temp_output.RC0'

    def test_load_empty_settings_file(self):
        try:
            settings_dict = su.read_settings_file(self.empty_settings_file)
        except Exception as e:
            self.fail(f"Loading empty settings file raised an exception: {e}")

    def test_export_settings_file(self):
        # Load the empty settings file
        settings_dict = su.read_settings_file(self.empty_settings_file)
        
        # Export the dictionary to a temporary file
        su.write_settings_file(settings_dict,self.temp_output_file)
        
        # Read the original and exported files
        with open(self.empty_settings_file, 'r') as original_file:
            original_data = original_file.read()
        with open(self.temp_output_file, 'r') as output_file:
            output_data = output_file.read()
        
        # # find the line where the original file differs from the output file
        # for i, (line1, line2) in enumerate(zip(original_data.splitlines(), output_data.splitlines())):
        #     if line1 != line2:
        #         print(f"Original: {line1}")
        #         print(f"Output: {line2}")
        #         print(f"Line {i + 1}")
        #         break
        # # Ensure the output file matches the input file exactly
        self.assertEqual(original_data, output_data)

    def tearDown(self):
        # Remove the temporary output file if it exists
        if os.path.exists(self.temp_output_file):
            os.remove(self.temp_output_file)

if __name__ == '__main__':
    unittest.main()