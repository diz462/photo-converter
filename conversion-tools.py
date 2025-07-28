def resize(file, scale):
    width = int(file.shape[1] * scale)
    height = int(file.shape[0] * scale)
