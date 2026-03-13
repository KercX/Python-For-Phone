import sys

# --- CORE LOGIC FOR FLET INTERFACE ---
def run_modern_ui():
    import flet as ft
    
    def main(page: ft.Page):
        page.title = "Python for Phone"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 30
        page.window_width = 400
        page.window_height = 800

        # UI Components
        header = ft.Text("Control Panel", size=40, weight="bold", color="blue")
        status_icon = ft.Icon(name=ft.icons.CELLULAR_ALT, color="green")
        
        user_input = ft.TextField(
            label="Command Center", 
            hint_text="Enter instructions...",
            border_radius=15,
            prefix_icon=ft.icons.TERMINAL
        )

        def on_action(e):
            if user_input.value:
                output_text.value = f"Processing: {user_input.value}..."
                progress_bar.visible = True
                page.update()
                # Simulating work
                output_text.value = f"Done! Project '{user_input.value}' is active."
                progress_bar.visible = False
                page.update()

        action_btn = ft.FloatingActionButton(
            icon=ft.icons.PLAY_ARROW, 
            on_click=on_action,
            bgcolor="blue"
        )
        
        output_text = ft.Text("System ready", size=16, italic=True)
        progress_bar = ft.ProgressBar(width=400, color="blue", visible=False)

        # Dashboard View
        page.add(
            ft.Row([header, status_icon], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Divider(height=30, color="transparent"),
            user_input,
            ft.Row([action_btn], alignment=ft.MainAxisAlignment.END),
            ft.Divider(height=20),
            output_text,
            progress_bar,
            ft.Spacer(),
            ft.Text("Powered by Python Engine", size=12, color="grey")
        )

    ft.app(target=main)

# --- CORE LOGIC FOR KIVY INTERFACE ---
def run_native_ui():
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.core.window import Window

    class MobileApp(App):
        def build(self):
            Window.clearcolor = (0.05, 0.05, 0.05, 1)
            layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
            
            layout.add_widget(Label(
                text="System Interface", 
                font_size='35sp', 
                bold=True, 
                color=(0, 0.5, 1, 1)
            ))
            
            btn = Button(
                text="LAUNCH CORE", 
                size_hint=(1, 0.2),
                background_normal='',
                background_color=(0, 0.4, 0.8, 1)
            )
            
            layout.add_widget(btn)
            layout.add_widget(Label(text="Native Kernel Active", color=(0.5, 0.5, 0.5, 1)))
            return layout

    MobileApp().run()

# --- SELECTOR ENGINE ---
if __name__ == "__main__":
    print("Initializing Python for Phone...")
    try:
        import flet
        run_modern_ui()
    except ImportError:
        print("Flet not found. Falling back to Kivy native engine...")
        run_native_ui()
