# tasks.py
from celery import shared_task
import json

@shared_task
def say_hello(name):
    print(f"Hello, {name}")

import time
import random

@shared_task
def process_order(order_id):
    """
    A Celery task to simulate processing an order.
    This task will be sent to Redis and picked up by a Celery worker.
    """
    print(f"Processing order {order_id}...")
    # Simulate doing some work
    processing_time = random.randint(5, 20)
    time.sleep(processing_time)
    print(f"Finished processing order {order_id} in {processing_time} seconds.")
    return f"Order {order_id} processed."

@shared_task
def scheduler_task():
    print("⏰ This runs every second!")
