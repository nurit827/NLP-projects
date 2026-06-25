#!/bin/bash
#SBATCH --job-name=ex5_all
#SBATCH --time=2:00:00
#SBATCH --cpus-per-task=4
#SBATCH --partition=salmon
#SBATCH --gres=gpu:l40s:1
#SBATCH --mem=32G
#SBATCH --output=./logs/slurm/%x_%j.out
#SBATCH --error=./logs/slurm/%x_%j.err

cd /sci/labs/orzuk/shaulytolk/NLP-projects/Ex5
source .venv/bin/activate
export HF_HOME=/sci/labs/orzuk/shaulytolk/hf_cache
python -c "import torch; print('cuda available:', torch.cuda.is_available(), torch.cuda.get_device_name(0) if torch.cuda.is_available() else '')"
python run_all.py
