import requests

from django.conf import settings


def send_order_notification(order):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_ADMIN_CHAT_ID
    location_text = ""

    if order.latitude and order.longitude:
        location_text = (
            f"\n🗺 Xarita:\n"
            f"https://maps.google.com/?q={order.latitude},{order.longitude}\n"
        )
    items_text = ""

    for item in order.items.all():
        items_text += (
            f"🍽 {item.menu_item.name} x{item.quantity}\n"
        )

    message = f"""
🔔 Yangi buyurtma #{order.id}

👤 {order.customer_name}
📞 {order.phone}
📍 {order.address}
{location_text} 

📦 Buyurtma:

{items_text}

💰 {order.total:,.0f} so'm

Status: Yangi
"""

    requests.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": message
        }
    )

def send_status_notification(order):
    if not order.telegram_id:
        return

    status_messages = {
        'new': '🆕 Buyurtmangiz qabul qilindi',
        'cooking': '👨‍🍳 Buyurtmangiz tayyorlanmoqda',
        'ready': '✅ Buyurtmangiz tayyor',
        'delivered': '🚚 Buyurtmangiz yetkazildi',
        'cancelled': '❌ Buyurtmangiz bekor qilindi',
    }

    message = f"""
{status_messages.get(order.status, '📦 Buyurtma holati yangilandi')}

Buyurtma #{order.id}
"""

    requests.post(
        f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
        json={
            "chat_id": order.telegram_id,
            "text": message
        }
    )

def send_receipt_notification(order):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_ADMIN_CHAT_ID

    caption = f"""
💰 Yangi to'lov cheki

Buyurtma #{order.id}

👤 {order.customer_name}
📞 {order.phone}

💵 {order.total:,.0f} so'm

To'lov holati: Chek yuborilgan
"""

    if not order.receipt:
        return

    photo_url = order.receipt.url

    requests.post(
        f"https://api.telegram.org/bot{token}/sendPhoto",
        data={
            "chat_id": chat_id,
            "caption": caption
        },
        files={
            "photo": open(order.receipt.path, "rb")
        }
    )