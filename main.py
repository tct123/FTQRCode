import flet as ft
import qrcode
from datetime import datetime


def main(page: ft.Page):
    def generate(e):
        filename = datetime.now()
        img = qrcode.make(data=url.value)
        name = f"{filename}qr.png"
        img.save(name)
        qrcode_img.src = name
        qrcode_img.update()

    page.title = "FTQRCode"
    page.appbar = ft.AppBar(title=ft.Text(page.title))
    qrcode_img = ft.Image(
        "assets/icon.png",
        width=100,
        height=100
        
    )
    url = ft.TextField()
    btn = ft.TextButton(text="Generate", on_click=generate)
    page.add(ft.SafeArea(ft.Column(controls=[qrcode_img, url, btn])))


ft.app(main)
