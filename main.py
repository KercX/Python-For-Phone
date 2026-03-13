import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Python for Phone - Enterprise Edition"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.window_width = 400
    page.window_height = 800
    page.scroll = "hidden"

    # --- 1. DATA STORAGE (Simulated Database) ---
    app_data = {
        "user": "Developer",
        "tasks": [],
        "logs": []
    }

    # --- 2. APP LOGIC ---
    def add_log(message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        app_data["logs"].append(f"[{timestamp}] {message}")

    def change_tab(e):
        index = e.control.selected_index
        main_content.controls.clear()
        
        if index == 0: # Home Tab
            main_content.controls.append(home_view())
        elif index == 1: # Dashboard Tab
            main_content.controls.append(dashboard_view())
        elif index == 2: # Settings Tab
            main_content.controls.append(settings_view())
            
        page.update()

    # --- 3. UI COMPONENTS (VIEWS) ---
    
    def home_view():
        return ft.Container(
            content=ft.Column([
                ft.Text("Welcome back,", size=20, color="grey"),
                ft.Text(f"{app_data['user']}! 👋", size=45, weight="bold"),
                ft.Divider(height=40, color="transparent"),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.SHIELD_MOON, color="blue"),
                                title=ft.Text("System Security"),
                                subtitle=ft.Text("Your connection is encrypted."),
                            ),
                            ft.Row([ft.TextButton("Details"), ft.TextButton("Optimize")], alignment="end")
                        ]), padding=10
                    )
                ),
                ft.Text("Recent Activity", size=25, weight="w600"),
                ft.ListView(expand=True, spacing=10, controls=[
                    ft.Text(log, size=14, color="grey") for log in reversed(app_data["logs"][-5:])
                ])
            ], scroll="adaptive"),
            padding=30, expand=True
        )

    def dashboard_view():
        task_input = ft.TextField(label="New Task Name", border_radius=15)
        
        def on_add(e):
            if task_input.value:
                app_data["tasks"].append(task_input.value)
                add_log(f"Added task: {task_input.value}")
                task_input.value = ""
                main_content.controls.clear()
                main_content.controls.append(dashboard_view())
                page.update()

        return ft.Container(
            content=ft.Column([
                ft.Text("Project Manager", size=35, weight="bold"),
                ft.Row([task_input, ft.IconButton(ft.icons.ADD_CIRCLE, on_click=on_add, icon_size=40, icon_color="blue")]),
                ft.Divider(),
                ft.Column([ft.Checkbox(label=t, value=False) for t in app_data["tasks"]], scroll="adaptive")
            ]), padding=30, expand=True
        )

    def settings_view():
        return ft.Container(
            content=ft.Column([
                ft.Text("Settings", size=35, weight="bold"),
                ft.Switch(label="Push Notifications", value=True),
                ft.Switch(label="Dark Mode", value=True, on_change=lambda _: setattr(page, "theme_mode", "light" if page.theme_mode == "dark" else "dark") or page.update()),
                ft.Dropdown(
                    label="Language",
                    options=[ft.dropdown.Option("English"), ft.dropdown.Option("Ukrainian")],
                    value="English"
                ),
                ft.ElevatedButton("Logout", color="red", icon=ft.icons.LOGOUT)
            ]), padding=30, expand=True
        )

    # --- 4. NAVIGATION & LAYOUT ---
    main_content = ft.Column([home_view()], expand=True)
    
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME_OUTLINED, selected_icon=ft.icons.HOME, label="Home"),
            ft.NavigationDestination(icon=ft.icons.DASHBOARD_OUTLINED, selected_icon=ft.icons.DASHBOARD, label="Manager"),
            ft.NavigationDestination(icon=ft.icons.SETTINGS_OUTLINED, selected_icon=ft.icons.SETTINGS, label="Settings"),
        ],
        on_change=change_tab
    )

    # Initial Log
    add_log("Application started successfully")
    
    page.add(
        ft.Container(
            content=main_content,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#1a1a2e", "#16213e"]
            ),
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
