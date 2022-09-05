from random import random

from drobe_dd_metrics.src.mod import ml_metrics


def test_ml_metrics():
    ml_metrics("test_ml_category_2", "accuracy", random(), 'test-image-tag', 'stg')
    ml_metrics("test_ml_category_2", "recall", random(), 'test-image-tag', 'stg')
    ml_metrics("test_ml_category_2", "precision", random(), 'test-image-tag', 'stg')