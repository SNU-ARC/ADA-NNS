import argparse
import h5py
import numpy as np

def save_fvecs(filename, data):
    with open(filename, 'wb') as f:
        for vec in data:
            f.write(np.int32([len(vec)]))  # Write the dimension of the feature vector
            f.write(vec.astype(np.float32).tobytes())  # Write the feature vector as FP32

def save_ivecs(filename, data):
    with open(filename, 'wb') as f:
        for vec in data:
            f.write(np.int32([len(vec)]))  # Write the dimension of the feature vector
            f.write(vec.astype(np.int32).tobytes())  # Write the feature vector as FP32

def hdf5_to_fvecs(hdf5_file):
    dataset_name = hdf5_file.split('-')[0]
    # Read data from HDF5 file
    with h5py.File(hdf5_file, 'r') as f:
        base = f['train'][:]
        query = f['test'][:]
        knn = f['neighbors'][:]

        # Save as fvecs format
        save_fvecs(f'{dataset_name}_base.fvecs', base)
        save_fvecs(f'{dataset_name}_query.fvecs', query)
        save_ivecs(f'{dataset_name}_groundtruth.ivecs', knn)

# HDF5 input
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Name of HDF5 dataset")
    parser.add_argument("hdf5_file_path", type=str, help="Nmae of HDF5 dataset")
    args = parser.parse_args()

    hdf5_to_fvecs(args.hdf5_file_path)
