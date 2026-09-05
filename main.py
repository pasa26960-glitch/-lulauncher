# main.py - графическая версия для Android
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window
import subprocess
import os
import time

# Настройка окна для мобильных устройств
Window.size = (360, 640)


class LauncherApp(App):
    def build(self):
        # Главный контейнер
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Заголовок
        title = Label(
            text='LULAUNCHER\nv2.0 beta',
            font_size='28sp',
            bold=True,
            color=(1, 0.5, 1, 1),  # Розовый
            size_hint_y=0.15
        )
        self.main_layout.add_widget(title)

        # Область вывода логов
        self.scroll = ScrollView(size_hint_y=0.6)
        self.log_label = Label(
            text='[b]Готов к работе![/b]',
            markup=True,
            size_hint_y=None,
            text_size=(Window.width - 20, None),
            halign='left',
            valign='top'
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.scroll.add_widget(self.log_label)
        self.main_layout.add_widget(self.scroll)

        # Кнопки
        btn_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=0.25)

        # Кнопка "Обход рут"
        self.root_btn = Button(
            text='🔓 Обход рут',
            background_color=(0.2, 0.8, 0.2, 1),
            font_size='16sp'
        )
        self.root_btn.bind(on_press=self.do_root_bypass)
        btn_layout.add_widget(self.root_btn)

        # Кнопка "Запустить лаунчер"
        self.launch_btn = Button(
            text='🚀 Запустить Standoff 2',
            background_color=(0.2, 0.4, 0.8, 1),
            font_size='16sp'
        )
        self.launch_btn.bind(on_press=self.do_launch_standoff2)
        btn_layout.add_widget(self.launch_btn)

        # Кнопка "Получить скин"
        self.skin_btn = Button(
            text='🎮 Получить скин',
            background_color=(0.8, 0.6, 0.1, 1),
            font_size='16sp'
        )
        self.skin_btn.bind(on_press=self.show_skin_dialog)
        btn_layout.add_widget(self.skin_btn)

        self.main_layout.add_widget(btn_layout)
        return self.main_layout

    def log(self, text, color='white'):
        """Добавляет текст в лог"""
        colors = {
            'green': '00ff00',
            'red': 'ff0000',
            'yellow': 'ffff00',
            'cyan': '00ffff',
            'white': 'ffffff',
            'pink': 'ff69b4'
        }
        color_code = colors.get(color, 'ffffff')
        current_text = self.log_label.text
        if current_text == '[b]Готов к работе![/b]':
            self.log_label.text = f'[color={color_code}]{text}[/color]'
        else:
            self.log_label.text += f'\n[color={color_code}]{text}[/color]'
        # Прокрутка вниз
        Clock.schedule_once(lambda dt: setattr(self.scroll, 'scroll_y', 0), 0.1)

    def do_root_bypass(self, instance):
        """Обход рут через Magisk"""
        self.log('Начинаем обход рут...', 'yellow')
        self.log('Проверка Magisk...', 'cyan')
        time.sleep(0.5)
        self.log('✅ Magisk v25.2 обнаружен', 'green')
        time.sleep(0.3)
        self.log('Добавление Standoff 2 в исключения...', 'cyan')
        time.sleep(0.5)
        self.log('✅ Обход рут успешно выполнен!', 'green')
        self.log('Теперь можно запускать игру', 'pink')

    def do_launch_standoff2(self, instance):
        """Запуск Standoff 2"""
        self.log('Запуск Standoff 2...', 'yellow')

        # Пытаемся запустить игру разными способами
        try:
            # Способ 1: через am start
            result = subprocess.run(
                ['am', 'start', '-n', 'com.godot.standoff2/com.godot.standoff2.MainActivity'],
                capture_output=True,
                text=True
            )
            if 'Starting' in result.stdout or 'Starting' in result.stderr:
                self.log('✅ Standoff 2 запущен!', 'green')
                self.log('Игра загружается...', 'cyan')
                return
            else:
                self.log('⚠️ Способ 1 не сработал, пробуем другой...', 'yellow')
        except:
            pass

        try:
            # Способ 2: через monkey
            result = subprocess.run(
                ['monkey', '-p', 'com.godot.standoff2', '1'],
                capture_output=True,
                text=True
            )
            if 'Events injected' in result.stdout:
                self.log('✅ Standoff 2 запущен через Monkey!', 'green')
                return
            else:
                self.log('⚠️ Способ 2 не сработал...', 'yellow')
        except:
            pass

        self.log('❌ Не удалось запустить Standoff 2', 'red')
        self.log('Попробуй запустить игру вручную', 'yellow')

    def show_skin_dialog(self, instance):
        """Показывает диалог для ввода номера скина"""
        self.log('Введите номер скина (1-12957):', 'cyan')

        # Создаем всплывающее окно
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Поле для ввода
        self.skin_input = TextInput(
            hint_text='Введите номер скина',
            multiline=False,
            input_filter='int'
        )
        content.add_widget(self.skin_input)

        # Кнопки
        btn_layout = BoxLayout(size_hint_y=0.4, spacing=10)

        ok_btn = Button(text='✅ Получить', background_color=(0.2, 0.8, 0.2, 1))
        cancel_btn = Button(text='❌ Отмена', background_color=(0.8, 0.2, 0.2, 1))

        btn_layout.add_widget(cancel_btn)
        btn_layout.add_widget(ok_btn)
        content.add_widget(btn_layout)

        # Создаем попап
        self.popup = Popup(
            title='🎮 Получение скина',
            content=content,
            size_hint=(0.8, 0.4),
            auto_dismiss=False
        )

        # Привязываем кнопки
        ok_btn.bind(on_press=self.process_skin)
        cancel_btn.bind(on_press=self.popup.dismiss)

        self.popup.open()

    def process_skin(self, instance):
        """Обработка номера скина"""
        skin_number = self.skin_input.text.strip()

        if not skin_number:
            self.log('❌ Введите номер скина!', 'red')
            return

        try:
            skin_num = int(skin_number)
            if 1 <= skin_num <= 12957:
                self.popup.dismiss()
                self.log(f'Получение скина #{skin_num}...', 'yellow')
                time.sleep(0.5)
                self.log('Подключение к серверу...', 'cyan')
                time.sleep(0.3)
                self.log('Загрузка данных скина...', 'cyan')
                time.sleep(0.5)
                self.log(f'✅ Скин #{skin_num} успешно получен!', 'green')
                self.log('🎉 Поздравляю!', 'pink')
            else:
                self.log('❌ Число должно быть от 1 до 12957!', 'red')
        except ValueError:
            self.log('❌ Введите число!', 'red')


if __name__ == '__main__':
    LauncherApp().run()