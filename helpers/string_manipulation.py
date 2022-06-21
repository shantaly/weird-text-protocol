def split_chunks(str, chunkSize):
    return [str[i:i+chunkSize] for i in range(0, len(str), chunkSize)] if str else []
