from random import random
import os

from drobe_dd_metrics.src.mod import DrobeDDMetricsSender

def test_ml_metrics():
    dd_api_key = os.environ['DD_API_KEY']
    drobe_dd = DrobeDDMetricsSender(
        "test_ml_category_2",
        'test-image-tag',
        'stg',
        dd_api_key
    )
    drobe_dd.send_ml_metric("accuracy", random())
    drobe_dd.send_ml_metric("recall", random())
    drobe_dd.send_ml_metric("precision", random())