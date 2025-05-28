from django.apps import AppConfig
import json
import django

from django.db.utils import OperationalError, ProgrammingError

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    def ready(self):
        try:
            from django_celery_beat.models import PeriodicTask, CrontabSchedule, IntervalSchedule
            if django.apps.apps.ready and not django.core.management.commands.migrate.Command().stdout:
                return
            # schedule, _ = CrontabSchedule.objects.get_or_create(
            #     minute='0',  # every hour at minute 0
            #     hour='*',
            # )

            schedule, _ = IntervalSchedule.objects.get_or_create(
                every=1,
                period=IntervalSchedule.SECONDS,
            )
            PeriodicTask.objects.values_list('name', 'task')

            PeriodicTask.objects.get_or_create(
                # crontab=schedule,
                interval=schedule,
                name='Run scheduler_task task every second',
                task='taskmanager.tasks.scheduler_task',
                defaults={'args': json.dumps([])},
            )
        except (OperationalError, ProgrammingError):
                # Database isn't ready yet — skip setup
                pass
