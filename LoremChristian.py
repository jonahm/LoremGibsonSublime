import sublime
import sublime_plugin
import random


class LoremgibsonCommand(sublime_plugin.TextCommand):


    @classmethod
    def generate_sentence(self, length=5):
        basetext = ['for'
,'God'
,'so'
,'loved'
,'the'
,'world'
,'that'
,'he'
,'gave'
,'his'
,'one'
,'and'
,'only'
,'Son'
,'that'
,'whoever'
,'believes'
,'in'
,'him'
,'shall'
,'not'
,'perish'
,'but'
,'have'
,'eternal'
,'life'
,'For'
,'I'
,'know'
,'the'
,'plans'
,'I'
,'have'
,'for'
,'you'
,'declares'
,'the'
,'LORD'
,'plans'
,'to'
,'prosper'
,'you'
,'and'
,'not'
,'to'
,'harm'
,'you'
,'plans'
,'to'
,'give'
,'you'
,'hope'
,'and'
,'a'
,'future'
,'And'
,'we'
,'know'
,'that'
,'in'
,'all'
,'things'
,'God'
,'works'
,'for'
,'the'
,'good'
,'of'
,'those'
,'who'
,'love'
,'him'
,'who'
,'have'
,'been'
,'called'
,'according'
,'to'
,'his'
,'purpose'
,'I'
,'can'
,'do'
,'everything'
,'through'
,'him'
,'who'
,'gives'
,'me'
,'strength'
,'In'
,'the'
,'beginning'
,'God'
,'created'
,'the'
,'heavens'
,'and'
,'the'
,'earth']
        random.shuffle(basetext)
        sentence = basetext[0:length]
        sentence[0] = sentence[0][0].upper() + sentence[0][1:]  # upcase first char of sentence
        sentence[-1] = sentence[-1] + '.'  # adding some punctuation
        sentence = ' '.join(sentence)
        return sentence

    @classmethod
    def generate_paragraph(self, length=4):
        paragraph = []
        for i in range(length):
            paragraph.append(LoremgibsonCommand.generate_sentence(random.randint(7, 17)))
        return ' '.join(paragraph)


    def run(self, edit):
        out = LoremgibsonCommand.generate_paragraph(random.randint(3, 9))
        out = out.replace('- ', '-')
        out = out.replace(' -', '-')
        out = out.replace('-.', '.')
        out = out + ' '
        self.view.insert(edit, self.view.sel()[0].begin(), out)
