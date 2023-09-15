import numpy as np
import gradio as gr
import subprocess
import tempfile
import os

def run(input_file, output_folder):

    with tempfile.NamedTemporaryFile(delete=False) as temp_input_file:
        temp_input_file.write(input_file.read())
        temp_input_file_path = temp_input_file.name

    command = [f"gecco run --genome {temp_input_file_path} -o ./"]
    
    try:
        # Run the CLI command and capture its output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # Extract the stdout from the result
        output_text = result.stdout
        
        return output_text
    except subprocess.CalledProcessError as e:
        # Handle any errors or exceptions
        return f"Error: {e}"

demo = gr.Interface(fn=run, inputs=gr.File(file_types=['fna'], label="Upload file here yo"),  outputs=gr.Textbox(label="CLI Output"))
demo.launch()
