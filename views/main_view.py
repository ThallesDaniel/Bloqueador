import flet as ft
from controllers.site_controller import SiteController
from views.add_site_view import AddSiteView

class MainView(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.site_controller = SiteController()
        self.site_table = None
    
    def update_sites(self):
        self.site_table.controls.clear()
        sites = self.site_controller.get_all_sites()
        for site in sites:
            self.site_table.controls.append(
                ft.Row([
                    ft.Text(site["url"]),
                    ft.IconButton(icon=ft.icons.LOCK, on_click=lambda e, site=site: self.site_controller.block_site(site["url"])),
                    ft.IconButton(icon=ft.icons.LOCK_OPEN, on_click=lambda e, site=site: self.site_controller.unblock_site(site["url"]))
                ])
            )
        self.update()
    
    def show_add_site_dialog(self, e):
        # Define o diálogo para ser exibido na página
        add_site_dialog = AddSiteView(on_site_added=self.update_sites)
        self.page.dialog = add_site_dialog.build()
        self.page.dialog.open = True
        self.page.update()

    def build(self):
        self.site_table = ft.Column()
        return ft.Column(
            controls=[
                ft.ElevatedButton("Adicionar Site", on_click=self.show_add_site_dialog),
                self.site_table
            ]
        )
