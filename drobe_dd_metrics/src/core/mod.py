"""
Submit metrics returns "Payload accepted" response
"""

from datetime import datetime
from typing import List

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_intake_type import MetricIntakeType
from datadog_api_client.v2.model.metric_payload import MetricPayload
from datadog_api_client.v2.model.metric_point import MetricPoint
from datadog_api_client.v2.model.metric_series import MetricSeries

import os
 

def send_custom_metrics_to_dd(metric: str, tags: List[str], value: float):
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
    configuration.api_key["apiKeyAuth"] = os.environ('DD_API_KEY')
    with ApiClient(configuration) as api_client:
        api_instance = MetricsApi(api_client)
        response = api_instance.submit_metrics(body=body)
