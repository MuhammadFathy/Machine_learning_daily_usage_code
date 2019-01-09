# clean unused var in python and free memory
import time
import gc

sentences = []
vocab = {}

del sentences, vocab
gc.collect()
time.sleep(10)
