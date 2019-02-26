#!/bin/bash
#SBATCH -c 18
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH -p largenode
#SBATCH -o job_%j.out
#SBATCH -e job_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=matsen@fredhutch.org
hostname
source activate py36
mkdir -p /mnt/beagle/delete10/matsen_e/vampire/uuid/oneoff1
cp output/basic_params.json /mnt/beagle/delete10/matsen_e/vampire/uuid/oneoff1/model_params.json
cp output/all-subjects.train.200K.csv /mnt/beagle/delete10/matsen_e/vampire/uuid/oneoff1/training.csv
tcr-vae train /mnt/beagle/delete10/matsen_e/vampire/uuid/oneoff1/model_params.json /mnt/beagle/delete10/matsen_e/vampire/uuid/oneoff1/training.csv output/all-subjects.train.200K.best_weights.h5 output/diagnostics.csv
