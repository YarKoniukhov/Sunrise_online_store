from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    # Задача отправки email-уведомлений при успешном оформлении заказа.
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\nYou have successfully placed an order. ' \
              f'Your order id is {order.id}.'
    mail_send = send_mail(subject, message, 'sunrise@gmail.com', [order.email, 'yarko1903@gmail.com'])

    return mail_send



