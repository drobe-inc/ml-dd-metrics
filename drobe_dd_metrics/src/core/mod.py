"""
Submit metrics returns "Payload accepted" response
"""

import time
from datetime import datetime
from typing import List

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_intake_type import MetricIntakeType
from datadog_api_client.v2.model.metric_payload import MetricPayload
from datadog_api_client.v2.model.metric_point import MetricPoint
from datadog_api_client.v2.model.metric_series import MetricSeries

NUM_MAX_RETRY = 3


def send_custom_metrics_to_dd(metric: str, tags: List[str], value: float, dd_api_key: str):
    # dd_api_key が set されていない場合は送らない
    if (dd_api_key is None): 
        print("[dd-metrics][dev] category: {}, value: {}, tags: {} ".format(metric, value, tags))
        return

    body = MetricPayload(
        series=[
            MetricSeries(
                metric=metric,
                type=MetricIntakeType(3),  # gauge
                points=[
                    MetricPoint(
                        timestamp=int(datetime.now().timestamp()),
                        value=value,
                    ),
                ],
                tags=tags,
            ),
        ],
    )

    configuration = Configuration()
    configuration.api_key["apiKeyAuth"] = dd_api_key
    with ApiClient(configuration) as api_client:
        api_instance = MetricsApi(api_client)
        # retry 機構を入れる
        for num_retry in range(NUM_MAX_RETRY + 1):
            try:
                api_instance.submit_metrics(body=body)
                return
            except Exception as e:
                if num_retry == NUM_MAX_RETRY:
                    raise e
                time.sleep(2**num_retry)
