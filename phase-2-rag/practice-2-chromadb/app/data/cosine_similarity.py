from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def compute_similarity(vec1, vec2):

    similarity = cosine_similarity(
        [np.array(vec1)],
        [np.array(vec2)]
    )[0][0]

    return similarity