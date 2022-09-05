from .core.mod import send_custom_metrics_to_dd


def ml_metrics(ml_category: str, metric_type: str, score: float, image_tag: str, env: str) -> None:
    """
    ml model の training 結果を datadog に送信する。

    Attributes
    ----------
    ml_category: str
        item_recommendation や size_recommendation などの大きなカテゴリ
    metric_type: str
        accuracy や recall などの ml の metrics 名
    score: float
        accuracy などの score の値
    image_tag: str
        ml model の traingin を行なった docker image の tag
    env: str
        stg もしくは prd の環境名
    """
    assert type(ml_category).__name__ == "str", "The type of ml_category should be str, but {}".format(
        type(ml_category).__name__
    )
    assert type(metric_type).__name__ == "str", "The type of metric_type should be str, but {}".format(
        type(metric_type).__name__
    )
    assert type(image_tag).__name__ == "str", "The type of image_tag should be str, but {}".format(
        type(image_tag).__name__
    )
    assert type(score).__name__ == "float", "The type of score should be float, but {}".format(
        type(score).__name__
    )
    assert env == "stg" or env == "prd", 'The env shoulde be "stg" or "prd", but {}'.format(env)

    custom_metrics_name = "ml.metric.{}".format(ml_category)

    tags = [
        "env:{}".format(env),
        "ml-metric:{}".format(metric_type),
        "ml-image-tag:{}".format(image_tag),
    ]

    send_custom_metrics_to_dd(custom_metrics_name, tags, score)
