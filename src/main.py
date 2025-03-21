import flet as ft
import qrcode
import qrcode.image.svg
from datetime import datetime
from mylocale.TR import tr
from mylist import mylist
import os


def main(page: ft.Page):
    def handle_nav_change(e):
        page.controls.clear()
        selected_index = (
            page.navigation_bar.selected_index
            if e is None
            else e.control.selected_index
        )
        if selected_index == 0:
            page.add(ft.SafeArea(ft.Column(controls=[qrcode_img, url, selector, btn])))
        elif selected_index == 1:
            page.add(ft.Text("Commute!"))
        page.update()

    def set_selected_index():
        page.navigation_bar.selected_index = 0
        handle_nav_change(None)

    def generate(e):
        name = os.path.join(os.getenv("FLET_APP_STORAGE_TEMP"), "qr.svg")
        page.adaptive = True
        print(name)
        if os.path.exists(name):
            os.remove(name)
            if selector.value == "basic":
                # Simple factory, just a set of rects.
                factory = qrcode.image.svg.SvgImage
            elif selector.value == "fragment":
                # Fragment factory (also just a set of rects)
                factory = qrcode.image.svg.SvgFragmentImage
            else:
                # Combined path factory, fixes white space that may occur when zooming
                factory = qrcode.image.svg.SvgPathImage

            img = qrcode.make(data=url.value, image_factory=factory)
            img.save(name)
            qrcode_img.src = name
            qrcode_img.update()
            page.update()
        else:
            if selector.value == "basic":
                # Simple factory, just a set of rects.
                factory = qrcode.image.svg.SvgImage
            elif selector.value == "fragment":
                # Fragment factory (also just a set of rects)
                factory = qrcode.image.svg.SvgFragmentImage
            else:
                # Combined path factory, fixes white space that may occur when zooming
                factory = qrcode.image.svg.SvgPathImage

            img = qrcode.make(
                data=url.value, image_factory=factory
            )  # image_factory=factory
            img.save(name)
            qrcode_img.src = name
            qrcode_img.update()
            page.update()

    page.title = "FTQRCode"
    page.appbar = ft.AppBar(title=ft.Text(page.title))
    page.navigation_bar = ft.NavigationBar(
        on_change=handle_nav_change,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.CAMERA_ALT_OUTLINED, selected_icon=ft.Icons.CAMERA_ALT
            ),
            ft.NavigationBarDestination(icon=ft.Icons.QR_CODE),
        ],
    )
    qrcode_img = ft.Image("assets/icon.png", width=100, height=100)
    url = ft.TextField(label="Value")
    btn = ft.TextButton(text="Generate", on_click=generate)
    selector = ft.Dropdown(
        options=[ft.dropdown.Option(option) for option in mylist],
        value="basic",
    )
    set_selected_index()


ft.app(main)
