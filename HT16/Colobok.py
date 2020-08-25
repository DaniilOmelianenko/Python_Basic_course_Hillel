class Hero:
    def __init__(self, name):
        self.name = name

class Autor(Hero):
    def start_tale(self):
        speech = '''\nЖил-был старик со старухою. Просит старик:'''
        return speech

    def appear_colobok(self):
        print('''\n  Взяла старуха крылышко, по коробу поскребла, по сусеку помела, и набралось
муки пригорошни с две. Замесила на сметане, изжарила в масле и положила на
окошечко постудить.
    Колобок полежал-полежал, да вдруг и покатился — с окна на лавку, с лавки на
пол, по полу да к дверям, перепрыгнул через порог в сени, из сеней на крыльцо, с
крыльца на двор, со двора за ворота, дальше и дальше\n''')
        return Colobok("Колобок")

    def meet_beast(self, beast):
        speech = f'''Катится колобок по дороге, а навстречу ему {beast}'''
        return speech

class Colobok(Hero):
    def appear_colobok(self):
        colobok = True
        return colobok

    def escape_from_home(self):
        speech = '''Надоело Колобку на окне лежать, он прыг с окна на лавку, с лавки на пол, 
        прыг через порог на крыльцо, с крыльца во двор, со двора за ворота и был таков.'''
        return print(speech)

    def escape_from_beast(self, beast):
        speech = f'''— Не ешь меня, {beast}! Я тебе песенку спою, — сказал колобок и запел:
Я по коробу скребен,
По сусеку метен,
На сметане мешон
Да в масле пряжон,
На окошке стужон;
Я от дедушки ушел,
Я от бабушки ушел,
И от тебя, {beast}, не хитро уйти!
И покатился себе дальше; только {beast} его и видел!..'''
        return speech


class Beast(Hero):
    def __init__(self, name):
        self.name = name

    def beast_speech(self, name):
        if name == 'lisa':
            speech = '''— Здравствуй, колобок! Какой ты хорошенький!'''
            return speech
        else:
            speech = '''Колобок, колобок! Я тебя съем.'''
            return speech


class Babka(Hero):
    def bake_colobok(self):
        speech = '''— Из чего печь-то? Муки нету.'''
        return speech


class Ded(Hero):
    def tell_babka_about_colobok(self):
        speech = '''— Испеки, старуха, колобок.'''
        return speech

    def how_to_make(self):
        speech = '''— Э-эх, старуха! По коробу поскреби, по сусеку помети; авось муки и наберется.'''
        return speech


class Tale:
    def __init__(self, babka, ded, autor, beast):
        self.babka = babka
        self.ded = ded
        self.colobok = None
        self.autor = autor
        self.beast = beast

    def babkin_dom(self):
        print(self.autor.start_tale(self.autor))
        print(self.ded.tell_babka_about_colobok(self.babka))
        print(self.babka.bake_colobok(self.ded))
        print(self.ded.how_to_make(self.babka))
        self.colobok = self.autor.appear_colobok(self.colobok)
        return ''''''

    def wood(self, beast):
        beast = self.beast
        print(self.autor.meet_beast(beast))




my_tail = Tale(Babka, Ded, Autor, Beast)
print(my_tail.babkin_dom())
print(my_tail.wood(beast='zayac'))