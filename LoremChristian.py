import sublime
import sublime_plugin
import random


class LoremgibsonCommand(sublime_plugin.TextCommand):


    @classmethod
    def generate_sentence(self, length=5):
        basetext = ['for','God','so','loved','the','world','that','he','gave','his','one','and','only','Son','that','whoever','believes','in','him','shall','not','perish','but','have','eternal','life','For','I','know','the','plans','I','have','for','you','declares','the','LORD','plans','to','prosper','you','and','not','to','harm','you','plans','to','give','you','hope','and','a','future','And','we','know','that','in','all','things','God','works','for','the','good','of','those','who','love','him','who','have','been','called','according','to','his','purpose','I','can','do','everything','through','him','who','gives','me','strength','In','the','beginning','God','created','the','heavens','and','the','earth','in','the','LORD','with','all','your','heart','and','lean','not','on','your','own','understanding','in','all','your','ways','acknowledge','him','and','he','will','make','your','paths','straight','Do','not','conform','any','longer','to','the','pattern','of','this','world','but','be','transformed','by','the','renewing','of','your','mind','Then','you','will','be','able','to','test','and','approve','what','God’s','will','is—his','good','pleasing','and','perfect','will','Do','not','be','anxious','about','anything','but','in','everything','by','prayer','and','petition','with','thanksgiving','present','your','requests','to','God','Therefore','go','and','make','disciples','of','all','nations','baptizing','them','in','the','name','of','the','Father','and','of','the','Son','and','of','the','Holy','Spirit','For','it','is','by','grace','you','have','been','saved','through','faith—and','this','not','from','yourselves','it','is','the','gift','of','God',''Therefore,'I','urge','you','brothers','in','view','of','God’s','mercy','to','offer','your','bodies','as','living','sacrifices','holy','and','pleasing','to','God—this','is','your','spiritual','act','of','worship','The','thief','comes','only','to','steal','and','kill','and','destroy;','I','have','come','that','they','may','have','life','and','have','it','to','the','full','For','I','am','with','you','and','no','one','is','going','to','attack','and','harm','you','because','I','have','many','people','in','this','city','One','night','the','Lord','spoke','to','Paul','in','a','vision:','Do','not','be','afraid;','keep','on','speaking','do','not','be','silent','So','Paul','stayed','for','a','year','and','a','half','teaching','them','the','word','of','God','I','have','been','crucified','with','Christ','and','I','no','longer','live','but','Christ','lives','in','me','The','life','I','live','in','the','body','I','live','by','faith','in','the','Son','of','God','who','loved','me','and','gave','himself','for','me',''If,'we','confess','our','sins','he','is','faithful','and','just','and','will','forgive','us','our','sins','and','purify','us','from','all','unrighteousness','for','all','have','sinned','and','fall','short','of','the','glory','of','God','Jesus','answered','I','am','the','way','and','the','truth','and','the','life','No','one','comes','to','the','Father','except','through','me','and','teaching','them','to','obey','everything','I','have','commanded','you','And','surely','I','am','with','you','always','to','the','very','end','of','the','age','But','God','demonstrates','his','own','love','for','us','in','this:','While','we','were','still','sinners','Christ','died','for','us','Finally','brothers','whatever','is','true','whatever','is','noble','whatever','is','right','whatever','is','pure','whatever','is','lovely','whatever','is','admirable—if','anything','is','excellent','or','praiseworthy—think','about','such','things',''And,'the','peace','of','God','which','transcends','all','understanding','will','guard','your','hearts','and','your','minds','in','Christ','Jesus','Have','I','not','commanded','you?','Be','strong','and','courageous','Do','not','be','terrified;','do','not','be','discouraged','for','the','LORD','your','God','will','be','with','you','wherever','you','go','but','those','who','hope','in','the','LORD']
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
