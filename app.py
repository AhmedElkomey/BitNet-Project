import streamlit as st
import subprocess
import os

# Set the title of the app
st.title("BitNet Explorer")

# Sidebar for model selection
st.sidebar.title("Model Selection")
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "BitNet", "models")

model_options = {
    "Small Model (bitnet_b1_58-large)": os.path.join(MODEL_DIR, "bitnet_b1_58-large", "ggml-model-i2_s.gguf"),
    "3B Model (bitnet_b1_58-3B)": os.path.join(MODEL_DIR, "bitnet_b1_58-3B", "ggml-model-i2_s.gguf"),
    "Llama3-8B Model (Llama3-8B-1.58-100B-tokens)": os.path.join(MODEL_DIR, "Llama3-8B-1.58-100B-tokens", "ggml-model-i2_s.gguf")
}

model_name = st.sidebar.selectbox("Choose a model", list(model_options.keys()))
model_path = model_options[model_name]

# Display the selected model path for debugging
st.sidebar.write(f"Model Path: {model_path}")

def generate_response(prompt, model_path):
    try:
        # Path to run_inference.py
        run_inference_path = os.path.join(os.getcwd(), "BitNet", "run_inference.py")
        # Directory where run_inference.py is located
        run_inference_dir = os.path.dirname(run_inference_path)

        # Construct the command
        cmd = [
            "python",
            run_inference_path,
            "-m", model_path,
            "-p", prompt
        ]

        # Run the command using subprocess, setting the working directory
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=300,  # Adjust as needed
            cwd=run_inference_dir  # Set the working directory
        )

        # Process the result as before
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return f"Error: {result.stderr.strip()}"
    except subprocess.TimeoutExpired:
        return "Error: Request timed out"
    except Exception as e:
        return f"Error: {str(e)}"

# Text input for the user prompt
prompt = st.text_area("Enter your prompt:", value="What is the capital of France?")

# Button to run inference
if st.button("Generate Response"):
    with st.spinner("Generating response..."):
        response = generate_response(prompt, model_path)
    st.success("Done!")
    st.write("**Response:**")
    st.write(response)
