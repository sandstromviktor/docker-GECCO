import numpy as np
import gradio as gr
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
    output_path = '/'.join(path_list[:-1])
    command = ["gecco", "run", "--genome", path ,"-o", f"{output_path}/output/"]
    
    try:
        # Run the CLI command and capture its output
        result = subprocess.run(command, capture_output = True, text = True)
        
        # Extract the stdout from the result
        output_text = result.stderr
        return output_text, "HEJ"
    except subprocess.CalledProcessError as e:
        # Handle any errors or exceptions
        return f"Error: {e}"

demo = gr.Interface(fn=preprocess_file, 
                    inputs=gr.File(file_types=['fna'], label="Upload genome here"),  
                    outputs=[gr.Textbox(label="CLI Output"), gr.Textbox(label="CLI Output")],
                    title=title, 
                    description=head)
demo.launch(debug=True, server_name="0.0.0.0", server_port=8080)
