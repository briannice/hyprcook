import os


def send_low_notification(title: str, body: str) -> None:
    os.system(f'notify-send -u low "{title}" "{body}"')


def send_normal_notification(title: str, body: str) -> None:
    os.system(f'notify-send -u normal "{title}" "{body}"')


def send_critical_notification(title: str, body: str) -> None:
    os.system(f'notify-send -u critical "{title}" "{body}"')
