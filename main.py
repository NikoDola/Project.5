import random
from kivy.clock import Clock

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.animation import Animation

# Display start, widht and height
Config.set('graphics', 'width', '439')
Config.set('graphics', 'height', '757')


class CoinFlip(App):
    def build(self):
        return BoxLayoutExample()


class BoxLayoutExample(BoxLayout):
    result = 0
    count_head = 0
    count_tail = 0
    row_head_count = 0
    row_tail_count = 0

    result_text = StringProperty("")
    row_head_text = StringProperty("")
    row_tail_text = StringProperty("")

    count_head_text = StringProperty("")
    count_tail_text = StringProperty("")

    sound_enable = True

    default_image_head = "Assets/head_default.png"
    default_image_tail = "Assets/tail_default.png"
    default_image_list = (default_image_head, default_image_tail)
    default_image = random.choice(default_image_list)

    def Play_sound(self):
        sound = SoundLoader.load("Assets/coin_flip.mp3")
        if self.sound_enable:
            sound.play()

    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "S O U N D  O N"
            self.sound_enable = True
        else:
            widget.text = "S O U N D  O F F"
            self.sound_enable = False

    def disable_button_for_delay(self, button, delay):
        button.disabled = True
        Clock.schedule_once(lambda dt: self.enable_button(button), delay)

    def enable_button(self, button):
        button.disabled = False

    def flip_coin(self):
        image1 = self.ids.image_widget.source = 'Assets/coin_head.gif'
        image2 = self.ids.image_widget.source = 'Assets/coin_tail.gif'
        lista = (image1, image2)
        chosen_image = random.choice(lista)
        self.ids.image_widget.source = chosen_image

        if chosen_image == image1:
            self.count_head += 1
            self.row_head_count += 1
            self.row_tail_count = 0
        else:
            self.count_tail += 1
            self.row_tail_count += 1
            self.row_head_count = 0

        # Schedule the delayed updates
        Clock.schedule_once(lambda dt: self.update_texts(chosen_image), 1.25)

    def update_texts(self, chosen_image):
        if chosen_image == 'Assets/coin_head.gif':
            self.count_head_text = f"Head {self.count_head}"
            if self.row_head_count >= 2:
                self.result_text = f"{self.row_head_count} Heads in a row"
            else:
                self.result_text = f" Head!"
        else:
            self.count_tail_text = f"Tail {self.count_tail}"
            if self.row_tail_count >= 2:
                self.result_text = f"{self.row_tail_count} Tails in a row"
            else:
                self.result_text = f"Tail!"

        if 3 <= self.row_head_count <= 5 or 3 <= self.row_tail_count <= 5:
            self.ids.Row_Label.font_size = 30
        elif 6 <= self.row_head_count <= 9 or 6 <= self.row_tail_count <= 9:
            self.ids.Row_Label.font_size = 40
        else:
            self.ids.Row_Label.font_size = 22




if __name__ == '__main__':
    CoinFlip().run()
