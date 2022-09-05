from .core.mod import send_custom_metrics_to_dd

class DrobeDDMetricsSender:
    def __init__(self, ml_category: str, model_tag: str, env: str, dd_api_key: str):
        """
        ml model の training 結果を datadog に送信する。

        Attributes
        ----------
        ml_category: str
            item_recommendation や size_recommendation などの大きなカテゴリ
        image_tag: str
            ml model の traingin を行なった docker image の tag や image tag の model 名の組み合わせなど、モデルバージョンを識別できるもの
        env: str
            stg もしくは prd の環境名
        """

        assert type(ml_category).__name__ == "str", "The type of ml_category should be str, but {}".format(
            type(ml_category).__name__
        )
        assert type(model_tag).__name__ == "str", "The type of model_tag should be str, but {}".format(
            type(model_tag).__name__
        )
        assert env == "stg" or env == "prd", 'The env shoulde be "stg" or "prd", but {}'.format(env)
        self.ml_category = ml_category
        self.model_tag = model_tag
        self.env = env
        self.dd_api_key = dd_api_key


    def send_ml_metric(self, metric_type: str, score: float) -> None:
        """
        ml model の training 結果を datadog に送信する。

        Attributes
        ----------
        metric_type: str
            accuracy や recall などの ml の metrics 名
        score: float
            accuracy などの score の値
        """
        assert type(metric_type).__name__ == "str", "The type of metric_type should be str, but {}".format(
            type(metric_type).__name__
        )
        assert type(score).__name__ == "float", "The type of score should be float, but {}".format(
            type(score).__name__
        )

        custom_metrics_name = "ml.metric.{}".format(self.ml_category)

        tags = [
            "env:{}".format(self.env),
            "ml-metric:{}".format(metric_type),
            "ml-model-tag:{}".format(self.model_tag),
        ]

        send_custom_metrics_to_dd(custom_metrics_name, tags, score, self.dd_api_key)
