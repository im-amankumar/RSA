Requirements
  1. python 3.7.9
  2. anaconda cli
  3. SQL lite

amaconda cli (commands)
1. working with conda

# Step 1: Check if Conda is installed
conda -V

# Step 2: Update Conda
conda update conda

# Step 3: Create a new environment
conda create -n tf python=3.7.9

# Step 4: Activate the environment
conda activate tf

# Step 5: Install additional packages
conda install numpy pandas

# Step 6: Deactivate the environment
conda deactivate

# Step 7: Remove the environment if no longer needed
conda remove -n tf --all

2. run the server

python app.py
