# BitNet Project Setup Guide

BitNet is a high-performance neural network implementation focusing on efficient inference using 1-bit quantization. This guide will help you set up and run BitNet models on your system using both command-line interface and a Streamlit web application.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Command Line Interface](#command-line-interface)
  - [Streamlit Web Interface](#streamlit-web-interface)
- [Available Models](#available-models)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Prerequisites

### System Requirements
- **Operating System**: Linux (Ubuntu recommended) or Windows with WSL2
- **Python**: Version 3.9 or higher
- **Git**: Latest stable version
- **C++ Compiler**: clang (LLVM) version 18 or higher
- **Build Tools**: cmake, ninja-build, build-essential, pkg-config
- **Internet Connection**: Required to download repositories and models

### Hardware Requirements
- Minimum 8GB RAM (16GB recommended for larger models)
- Sufficient disk space for models

## Installation

### 1. Clone the Repository
```bash
# Create and navigate to project directory
mkdir bitnet-project
cd bitnet-project

# Clone BitNet repository
git clone --recursive https://github.com/microsoft/BitNet.git
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python3 -m venv bitnet-venv
source bitnet-venv/bin/activate
```

### 3. Install Dependencies
```bash
# System dependencies
sudo apt update
sudo apt install -y build-essential pkg-config cmake git python3-pip ninja-build wget

# Install LLVM
wget https://apt.llvm.org/llvm.sh
chmod +x llvm.sh
sudo ./llvm.sh 18 -- --install-dir /usr/lib/llvm-18

# Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install streamlit  # For web interface
```

### 4. Build the Project
```bash
# Navigate to BitNet directory and build
cd BitNet
mkdir -p build
cd build
cmake ..
make
```

## Project Structure
```
bitnet-project/
├── app.py                  # Streamlit web application
├── bitnet-venv/           # Python virtual environment
├── BitNet/                # Main repository
│   ├── models/           # Downloaded models
│   ├── build/           # Build directory with binaries
│   │   └── bin/        # Compiled executables
│   ├── src/            # Source code
│   ├── run_inference.py # Original inference script
│   ├── setup_env.py    # Environment setup script
│   └── requirements.txt # Python dependencies
```

## Usage

### Command Line Interface

#### Running Different Models

1. **Small Model**
```bash
python setup_env.py --hf-repo 1bitLLM/bitnet_b1_58-large -q i2_s
python run_inference.py -m models/bitnet_b1_58-large/ggml-model-i2_s.gguf -p "Your prompt here"
```

2. **3B Model**
```bash
python setup_env.py --hf-repo 1bitLLM/bitnet_b1_58-3B -q i2_s
python run_inference.py -m models/bitnet_b1_58-3B/ggml-model-i2_s.gguf -p "Your prompt here"
```

### Streamlit Web Interface

1. **Start the Application**
```bash
# Navigate to project root
cd bitnet-project

# Activate virtual environment
source bitnet-venv/bin/activate

# Run Streamlit app
streamlit run app.py
```

2. **Using the Web Interface**
- Open your browser and navigate to `http://localhost:8501`
- Select a model from the sidebar
- Enter your prompt in the text area
- Click "Generate Response" to run inference
- View the generated response below

## Troubleshooting

### Common Issues

1. **Binary Not Found**
```bash
# Ensure binary has execute permissions
chmod +x BitNet/build/bin/llama-cli
```

2. **Model Loading Errors**
- Verify model files exist in the correct directory
- Check for sufficient disk space
- Ensure correct paths in configuration

3. **Streamlit Issues**
```bash
# Clear Streamlit cache if changes aren't reflecting
streamlit run app.py --clear-cache
```

### Memory Issues
If experiencing memory issues with larger models:

1. Check available memory:
```bash
free -h
```

2. Adjust swap space:
```bash
sudo fallocate -l 16G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License
This project uses code from Microsoft's BitNet repository. Please refer to the original repository for license information.

## Acknowledgments
- **Microsoft**: For developing the BitNet models
- **Streamlit**: For providing the web application framework
- **Community**: For contributions and feedback