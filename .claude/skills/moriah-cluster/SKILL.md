---
name: moriah-cluster
description: Run jobs on the HUJI Moriah SLURM cluster from this repo — SSH tunnel access, rsync sync, GPU sbatch submission, monitoring, and pulling results back. Use when training/eval is too slow locally and should run on a GPU node.
---

# Moriah cluster (HUJI) — run jobs from NLP-projects

The cluster is reachable through an **SSH tunnel on port 2222** as user `shaulytolk`.
Login node: `moriah-gw-01`. Lab dir: `/sci/labs/orzuk/shaulytolk/`.
Repo on cluster: `/sci/labs/orzuk/shaulytolk/NLP-projects` (mirror of `/Users/stolk/github/NLP-projects`).

## Access patterns

```bash
# Run a command (plain)
ssh -p 2222 shaulytolk@localhost "<cmd>"

# Run a command that needs modules / sbatch / the env — MUST use a login shell
ssh -p 2222 shaulytolk@localhost "bash -l -c 'cd /sci/labs/orzuk/shaulytolk/NLP-projects/<dir> && <cmd>'"

# Copy files up (or down — swap src/dst)
rsync -avz -e 'ssh -p 2222' <local_path> shaulytolk@localhost:/sci/labs/orzuk/shaulytolk/NLP-projects/<dir>/
rsync -avz -e 'ssh -p 2222' shaulytolk@localhost:/sci/labs/orzuk/shaulytolk/NLP-projects/<dir>/<file> <local_path>
```

Always add `-o ConnectTimeout=10`. For non-interactive checks add `-o BatchMode=yes`.

## Modules & environment

- GPU: `ml cuda/12.8.1` (or `cuda/12.4.1`). Python: `ml python/3.13.5`. `ml uv` is available.
- There is no shared NLP env by default — create a per-exercise venv once and reuse:
  ```bash
  ssh -p 2222 shaulytolk@localhost "bash -l -c '
    ml python/3.13.5
    cd /sci/labs/orzuk/shaulytolk/NLP-projects/<dir>
    python -m venv .venv && source .venv/bin/activate
    pip install -q torch transformers numpy matplotlib
  '"
  ```
- HF model cache already exists at `/sci/labs/orzuk/shaulytolk/hf_cache`. Export
  `HF_HOME=/sci/labs/orzuk/shaulytolk/hf_cache` in jobs to reuse downloads and avoid re-pulling.

## GPU partition

- Partition `catfish` with `--gres=gpu:l4:1` (L4 GPU). CPU-only jobs are rejected on catfish.
- CPU-only prep can run directly on the login node.

## sbatch template

```bash
#!/bin/bash
#SBATCH --job-name=<name>
#SBATCH --time=2:00:00
#SBATCH --cpus-per-task=4
#SBATCH --partition=catfish
#SBATCH --gres=gpu:l4:1
#SBATCH --mem=32G
#SBATCH --output=./logs/slurm/%x_%j.out
#SBATCH --error=./logs/slurm/%x_%j.err

cd /sci/labs/orzuk/shaulytolk/NLP-projects/<dir>
ml cuda/12.8.1
ml python/3.13.5
source .venv/bin/activate
export HF_HOME=/sci/labs/orzuk/shaulytolk/hf_cache
python <script>.py
```

Submit (note the login shell), then monitor:

```bash
ssh -p 2222 shaulytolk@localhost "bash -l -c 'cd /sci/labs/orzuk/shaulytolk/NLP-projects/<dir> && mkdir -p logs/slurm && sbatch <job>.sbatch'"
ssh -p 2222 shaulytolk@localhost "bash -l -c 'squeue -u shaulytolk'"
ssh -p 2222 shaulytolk@localhost "tail -n 40 /sci/labs/orzuk/shaulytolk/NLP-projects/<dir>/logs/slurm/<name>_<jobid>.out"
```

## Typical workflow

1. rsync the local code + any data the cluster lacks (e.g. the dataset folder) up to the repo dir.
2. Create/activate the venv (once) and install deps.
3. Write an sbatch script (template above) and `sbatch` it via a login shell.
4. Poll `squeue` and tail the `.out`/`.err` logs until done.
5. rsync the output artifacts (plots, result files) back down.

## Gotchas

- `sbatch`, `ml`, and venv activation only work under `bash -l -c '...'` (login shell). A plain
  `ssh ... "sbatch ..."` fails with "command not found".
- The tunnel host is `localhost:2222`, not `moriah-gw-01` directly.
- Git on the cluster uses SSH remotes; HTTPS password auth no longer works. Prefer rsync for
  quick sync over committing/pulling.
