import os, shutil

original_dataset_dir = 'pic'

base_dir = 'dataset'
try:
    os.mkdir(base_dir)
except:
    pass

train_dir = os.path.join(base_dir, 'train')
try:
    os.mkdir(train_dir)
except:
    pass

train_cat_dir = []
for i in range(100):
    train_cat_dir.append(os.path.join(train_dir, str(i)))
    try:
        os.mkdir(train_cat_dir[-1])
    except:
        pass


for i in range(100):
    fnames = ['{}_{}.jpg'.format(i, (i*100)+j) for j in range(1,101)]
    for fname in fnames:
        src = os.path.join(original_dataset_dir, fname)
        dst = os.path.join(train_cat_dir[i], fname)
        shutil.copyfile(src, dst)
