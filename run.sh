#!/bin/bash

# Step 1: Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Step 2: Activate the virtual environment
source venv/bin/activate

# Step 3: Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 4: Run the GUI code
echo "Running the GUI application..."
python quiztimer.py
