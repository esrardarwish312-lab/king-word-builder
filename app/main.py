from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from word_engine import WordEngine

Window.clearcolor = (0.04, 0.06, 0.12, 1)

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 15
    spacing: 10

    Label:
        text: '[b]👑 KING REIGNS CYBERY WORD BUILDER[/b]'
        markup: True
        font_size: '21sp'
        size_hint_y: .12

    Spinner:
        id: language
        text: 'English'
        values: ['English', 'پښتو', 'دری']
        size_hint_y: .09

    Spinner:
        id: level
        text: 'All'
        values: ['All', 'Easy', 'Medium', 'Advanced']
        size_hint_y: .09

    TextInput:
        id: word
        hint_text: 'Enter an English word'
        multiline: False
        size_hint_y: .12

    Button:
        text: 'GENERATE WORDS'
        size_hint_y: .12
        background_color: .1, .35, .85, 1
        on_release: app.generate()

    ScrollView:
        do_scroll_x: False

        Label:
            id: result
            text: 'Your words will appear here'
            size_hint_y: None
            height: self.texture_size[1] + 30
            text_size: self.width - 20, None
            halign: 'left'
            valign: 'top'
'''

class KingWordBuilder(App):
    def build(self):
        self.title = 'KING REIGNS CYBERY WORD BUILDER'
        self.engine = WordEngine()
        return Builder.load_string(KV)

    def generate(self):
        word = self.root.ids.word.text.strip()
        level = self.root.ids.level.text
        language = self.root.ids.language.text

        results = self.engine.generate(word, level)

        if not results:
            self.root.ids.result.text = 'No matching words found.'
            return

        lines = [f'FOUND: {len(results)} WORDS\\n']

        for item in results:
            name = item["word"]
            data = item["data"]

            if language == 'پښتو':
                meaning = '، '.join(data["ps"])
            elif language == 'دری':
                meaning = data["fa"]
            else:
                meaning = data["definition"]

            lines.append(f'{name} — {meaning}')

        self.root.ids.result.text = '\\n'.join(lines)

if __name__ == "__main__":
    KingWordBuilder().run()
