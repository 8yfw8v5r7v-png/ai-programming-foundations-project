import os

# List of all directories to create
directories = [
    'notebooks',
    'data/raw',
    'data/processed',
    'data/external',
    'models',
    'results/figures',
    'results/reports',
    'tests',
    'docs',
    'config',
    'src/data',
    'src/preprocessing',
    'src/models',
    'src/utils',
]

# Create all directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f"Created/Verified: {directory}")

# Create .gitkeep files to preserve empty directories in git
gitkeep_files = [
    'notebooks/.gitkeep',
    'data/raw/.gitkeep',
    'data/processed/.gitkeep',
    'data/external/.gitkeep',
    'models/.gitkeep',
    'results/figures/.gitkeep',
    'results/reports/.gitkeep',
    'tests/.gitkeep',
    'docs/.gitkeep',
    'config/.gitkeep',
]

for gitkeep in gitkeep_files:
    with open(gitkeep, 'w') as f:
        f.write('')
    print(f"Created: {gitkeep}")

print("\n✅ All directories and .gitkeep files created successfully!")