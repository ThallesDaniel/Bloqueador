import flet as ft
from controllers.site_controller import SiteController

class AddSiteView(ft.UserControl):
    def __init__(self, on_site_added):
        super().__init__()
        self.on_site_added = on_site_added
        self.site_controller = SiteController()
    
    def add_site(self, e):
        site_url = self.site_url_field.value
        if site_url:
            self.site_controller.add_site(site_url)
            self.on_site_added()  # Atualiza a lista de sites bloqueados
            self.dialog.open = False  # Fecha o diálogo
            self.page.update()  # Atualiza a página

    def build(self):
        self.site_url_field = ft.TextField(label="URL do site")
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Adicionar Site"),
            content=ft.Column([
                self.site_url_field,
                ft.ElevatedButton("Adicionar", on_click=self.add_site)
            ]),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: self.close_dialog())
            ],
        )
        return self.dialog

    def close_dialog(self):
        self.dialog.open = False
        self.page.update()
