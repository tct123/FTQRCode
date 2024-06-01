import flet as ft
import qrcode
import qrcode.image.svg
from datetime import datetime
from mylocale.TR import tr


def main(page: ft.Page):
    def generate(e):
        filename = datetime.now()
        if method == "basic":
            # Simple factory, just a set of rects.
            factory = qrcode.image.svg.SvgImage
        elif method == "fragment":
            # Fragment factory (also just a set of rects)
            factory = qrcode.image.svg.SvgFragmentImage
        else:
            # Combined path factory, fixes white space that may occur when zooming
            factory = qrcode.image.svg.SvgPathImage

        img = qrcode.make(data=url.value)
        name = f"{filename}qr.png"
        img.save(name)
        qrcode_img.src = name
        qrcode_img.update()

    page.title = "FTQRCode"
    page.appbar = ft.AppBar(title=ft.Text(page.title))
    qrcode_img = ft.Image("assets/icon.png", width=100, height=100)
    url = ft.TextField(label="Value")
    btn = ft.TextButton(text="Generate", on_click=generate)
    page.add(ft.SafeArea(ft.Column(controls=[qrcode_img, url, btn])))


ft.app(main)
