import h5py
f = h5py.File("DB6_processed_8ch/train.h5", "r")
print(f["data"].shape)
