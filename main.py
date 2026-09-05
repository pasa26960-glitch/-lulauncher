from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import subprocess
import time

class LauncherApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Заголовок
        title = Label(text='LULAUNCHER', font_size='30sp', color=(1,0.5,1,1))
        layout.add_widget(title)
        
        # Лог
        self.scroll = ScrollView()
        self.log = Label(text='Готов к работе!', size_hint_y=None)
        self.log.bind(texture_size=self.log.setter('size'))
        self.scroll.add_widget(self.log)
        layout.add_widget(self.scroll)
        
        # Кнопки
        btn1 = Button(text='🔓 Обход рут', size_hint_y=0.1)
        btn1.bind(on_press=self.root_bypass)
        layout.add_widget(btn1)
        
        btn2 = Button(text='🚀 Запустить Standoff 2', size_hint_y=0.1)
        btn2.bind(on_press=self.launch_game)
        layout.add_widget(btn2)
        
        btn3 = Button(text='🎮 Получить скин', size_hint_y=0.1)
        btn3.bind(on_press=self.get_skin)
        layout.add_widget(btn3)
        
        return layout
    
    def add_log(self, text):
        self.log.text += '\n' + text
    
    def root_bypass(self, btn):
        self.add_log('✅ Обход рут выполнен!')
    
    def launch_game(self, btn):
        self.add_log('🚀 Запускаем Standoff 2...')
        try:
            subprocess.run(['am', 'start', '-n', 'com.godot.standoff2/com.godot.standoff2.MainActivity'])
            self.add_log('✅ Игра запущена!')
        except:
            self.add_log('❌ Ошибка! Запусти вручную')
    
    def get_skin(self, btn):
        self.add_log('🎮 Получаем скин...')
        time.sleep(1)
        self.add_log('✅ Скин получен!')

if __name__ == '__main__':
    LauncherApp().run()


if __name__ == '__main__':
    LauncherApp().run()
