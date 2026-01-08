import os


def send_low_notification(title: str, body: str) -> None:
    os.system(f"dunstify -u low {title} {body}")


def send_normal_notification(title: str, body: str) -> None:
    os.system(f"dunstify -u normal {title} {body}")


def send_critical_notification(title: str, body: str) -> None:
    os.system(f"dunstify -u critical {title} {body}")
