from apscheduler.jobstores.base import JobLookupError
from apscheduler.triggers.cron import CronTrigger
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from elasticclient import get_netflow_resampled
from models import Detector
from nescient import core
from scheduler import scheduler


def le_job(detector_instance: Detector):
    core(get_netflow_resampled(
        "now",
        detector_instance.sampling_interval,
        detector_instance.elastic_host,
        detector_instance.elastic_index
    ), detector_instance)

@receiver(post_save, sender=Detector)
def upsert_jobs_after_save(sender, instance: Detector, **kwargs):
    scheduler.add_job(
        func=le_job,
        trigger=CronTrigger(second=instance.sampling_interval),
        args=[instance],
        id=instance.device_slug,
        max_instances=1,
        replace_existing=True
    )

@receiver(post_delete, sender=Detector)
def delete_jobs_after_delete(sender, instance: Detector, **kwargs):
    try:
        scheduler.remove_job(instance.device_slug)
    except JobLookupError as e:
        print("[Nescient] {} Job not found while checked after deleting instance of Detector by slug {}"
              .format(e.__str__(), instance.device_slug))