"""
this script runs all of the notebooks in the preprocessing folder so that they do not need to be opened individually
"""

import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

os.environ['PYDEVD_DISABLE_FILE_VALIDATION'] = '1'

def execute_notebook(notebook_path):

    notebook_dir = os.path.dirname(notebook_path)

    with open(notebook_path, 'r') as f:
        # Read the notebook
        nb = nbformat.read(f, as_version=4)
        
        # Create the preprocessor
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        
        # Execute the notebook
        try:
            ep.preprocess(nb, {'metadata': {'path': notebook_dir}})
        except Exception as e:
            print(f"Error executing {notebook_path}: {e}")
            return

        # # Optionally: Save the executed notebook to a file
        # with open(notebook_path, 'w', encoding='utf-8') as f:
        #     nbformat.write(nb, f)

def run_all_notebooks_in_folder(folder_path):
    # List all files in the folder
    files = sorted(os.listdir(folder_path))
    
    for file in files:
        # Check if the file is a Jupyter notebook
        if file.endswith('.ipynb'):
            full_path = os.path.join(folder_path, file)
            print(f"Executing {full_path}...")
            execute_notebook(full_path)
            print(f"Finished executing {full_path}")

if __name__ == "__main__":
    folder_path = "notebooks/1 - preprocessing"  
    run_all_notebooks_in_folder(folder_path)

