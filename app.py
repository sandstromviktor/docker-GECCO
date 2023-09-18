import numpy as np
import gradio as gr
from zipfile import ZipFile
import subprocess
import tempfile
import shutil
import os

# app title
title = "GECCO | Gene Cluster prediction with Conditional Random Fields"

# app description
head = (
  "<center>"
  "<img src='file/static/gecco-square.png' width=200px style='margin:15px'>"
  "GECCO (Gene Cluster prediction with Conditional Random Fields) is a fast and scalable method for identifying<br> putative novel Biosynthetic Gene Clusters (BGCs) in genomic and metagenomic data using Conditional Random Fields (CRFs)."
  "</center>"
)

def preprocess_file(fileobj):
    path = fileobj.name
    return run_gecco(path)

def run_gecco(path):
    path_list = path.split("/")
    output_path = os.path.join('/'.join(path_list[:-1]), "output")
    command = ["gecco", "run", "--genome", path ,"-o", output_path]
    
    try:
        # Run the CLI command and capture its output
        result = subprocess.run(command, capture_output = True, text = True)
        
        # Extract the stdout from the result
        output_text = result.stderr
        
    except subprocess.CalledProcessError as e:
        # Handle any errors or exceptions
        return f"Error: {e}"
    
    path_walk_generator = os.walk(output_path, topdown=False)
    files = [file for _, _, files in path_walk_generator for file in files if not file.endswith(".zip")]     
    print("List of files", files)
    zip_path = os.path.join(output_path, f"{path.split('/')[3]}.zip")
    with ZipFile(zip_path, "w") as zipObj:
        for file in files:
            zipObj.write(os.path.join(output_path, file), file)
    return output_text, zip_path

demo = gr.Interface(fn=preprocess_file, 
                    inputs=gr.File(file_types=['fna'], label="Upload genome here"),  
                    outputs=[gr.Textbox(label="CLI Output"), gr.File(label="GECCO file Output")],
                    title=title, 
                    description=head)
demo.launch(debug=True, server_name="0.0.0.0", server_port=8080)
