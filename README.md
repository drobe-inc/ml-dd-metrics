# ml-dd-metrics

## setup

```
make init
```

## version up

以下の 3 file の version を更新する (TODO: もっとちゃんとしたやり方考える)
- https://github.com/drobe-inc/ml-dd-metrics/blob/main/drobe_dd_metrics/__init__.py#L3
- https://github.com/drobe-inc/ml-dd-metrics/blob/main/pyproject.toml#L3
- https://github.com/drobe-inc/ml-dd-metrics/blob/main/setup.cfg#L3

## how to use

```
from drobe_dd_metrics import DrobeDDMetricsSender

drobe_dd = DrobeDDMetricsSender(
    'test-ml-category-1'
    'test-model-tag-1',
    'stg',
    DD_API_KEY
)
        
drobe_dd.send_ml_metric("accuracy", 0.83)
```
