import flet as ft


def main(pg: ft.Page):
    pg.title = "Calculator"
    pg.vertical_alignment = ft.MainAxisAlignment.END
    pg.horizontal_alignment = ft.MainAxisAlignment.CENTER
    pg.window_width = 340
    pg.window_height = 700
    pg.window_resizable = False

    result = ft.Text(value="", color=ft.colors.WHITE, bgcolor=ft.colors.INDIGO_400, size=32)
    global_data = result.value
    is_contrast_mode = False

    def calc(e):
        nonlocal global_data
        data = e.control.data
        result.value = global_data + data
        if data == '=':
            if global_data == "":
                result.value = "Değer Giriniz"
            else:
                try:
                    result.value = eval(global_data)
                except SyntaxError:
                    result.value = "Error"
            global_data = ''
        else:
            global_data += data
        pg.update()

    def theme_changed():
        nonlocal is_contrast_mode
        is_contrast_mode = not is_contrast_mode
        if is_contrast_mode:
            pg.theme_mode = ft.ThemeMode.DARK
            result.bgcolor = ft.colors.BLACK
            result.color = ft.colors.WHITE
        else:
            pg.theme_mode = ft.ThemeMode.LIGHT
            result.bgcolor = ft.colors.WHITE
            result.color = ft.colors.BLACK
        pg.update()

    def eventC(_):
        nonlocal global_data
        result.value = ""
        global_data = ""
        pg.update()

    def d(_):
        nonlocal global_data
        if len(result.value) > 0:
            result.value = result.value[:-1]
            global_data = global_data[:-1]
        pg.update()

    def event(e):
        nonlocal global_data
        data_e = e.control.data
        if data_e in "1234567890":
            if len(global_data) < 12:
                global_data += data_e
                result.value += data_e
        elif data_e == "00":
            if len(global_data) < 11:
                global_data += data_e
                result.value += data_e
        elif data_e == ".":
            if len(global_data) < 11 and "." not in global_data:
                global_data += data_e
                result.value += data_e
        pg.update()

    pg.theme_mode = ft.ThemeMode.LIGHT

    pg.appbar = ft.AppBar(
        leading_width=40,
        title=ft.Text("Calculator"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(
                ft.Switch(on_change=theme_changed)
            ),
        ],
    )

    pg.add(
        ft.Row(controls=[result], alignment=ft.MainAxisAlignment.END),
        ft.Row(
            spacing=10,
            controls=[
                ft.ElevatedButton("C", data="C", on_click=eventC,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("%", data="%", on_click=calc,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("d", data="d", on_click=d, style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("/", data="/", on_click=calc,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30))
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton("7", data="7", on_click=event,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("8", data="8", on_click=event,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("9", data="9", on_click=event,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("x", data="*", on_click=calc,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
            ],
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton("4", data="4", on_click=event,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("5", data="5", on_click=event,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("6", data="6", on_click=event,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("-", data="-", on_click=calc,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton("1", data="1", on_click=event,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("2", data="2", on_click=event,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("3", data="3", on_click=event,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("+", data="+", on_click=calc,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton("00", data="00", on_click=event,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=28)),
                ft.ElevatedButton("0", data="0", on_click=event,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton(".", data=".", on_click=event,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
                ft.ElevatedButton("=", data="=", on_click=calc,
                                  style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30)),
            ]
        )
    )

    pg.update()


ft.app(target=main)
