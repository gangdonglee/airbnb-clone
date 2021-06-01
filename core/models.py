from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(
        auto_now_add=True
    )  # 장고는 내가 새로운 Model를 만들면 django가 현재 날짜랑 시간을 여기다 넣어준다.
    update = models.DateTimeField(auto_now=True)  # 내가 model을 저장할때마다 그 당시의 시간을 넣어준다.

    class Meta:
        abstract = True

    pass
