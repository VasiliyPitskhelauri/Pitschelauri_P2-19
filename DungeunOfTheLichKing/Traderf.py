import BattleFunction
import tracker

class Trad:
    """Класс торговца"""
    def Trader(self):
        tracker.Ui_MainWindow.ArtTrader(self)
        """Вывод текста торговца"""
        self.listWidget.addItem('Странствующий торговец\n')
        self.listWidget.addItem(
                             'Вы неожиданно встречаете странствующего торговца,\n на его спине висит огромный рюкзак. '
                             'Он радостно приветствует вас.\n'
                             'Вы спрашиваете его как он здесь оказался.\n На все ваши вопросы он либо отнекивается, '
                             'либо уклончиво отвечает.')
        self.listWidget.addItem(
                             '-Сэр рыцарь, предлагаю перейти к делу, у меня вы можете приобрести:\n'
                             'Зелье здоровья за 30 монет,\n а так же я могу заточить ваш клинок'
                             '(повышение урона на 3 единицы) за 100 монет\n\n')

    def Health_Po(self):
        """Покупка зелий здоровья у торговца, если не хватает денег, об этом сообщается"""
        if BattleFunction.peremenn.Money < 30:
            self.listWidget.addItem('У вас недостаточно денег их количество = {} \n\n'.
                                    format(BattleFunction.peremenn.Money))
        elif BattleFunction.peremenn.Money >= 30:
            BattleFunction.peremenn.Money = BattleFunction.peremenn.Money - 30
            BattleFunction.peremenn.hp_kolwo += 1
            self.listWidget.addItem(' Вы приобрели зелье здоровья. Кол-во зелий = {}.Кол-во денег = {} \n\n'.format(
                BattleFunction.peremenn.hp_kolwo, BattleFunction.peremenn.Money))

    def Bat(self):
        """Заточка оружия у торговца, если не хватает денег, об этом сообщается"""
        if BattleFunction.peremenn.Money < 100:
            self.listWidget.addItem('У вас недостаточно денег их количество = {} \n\n'.
                                    format(BattleFunction.peremenn.Money))
        elif BattleFunction.peremenn.Money >= 100:
            BattleFunction.peremenn.Money = BattleFunction.peremenn.Money - 100
            for i in range(len(BattleFunction.Hero.Bat_qer)):
                BattleFunction.Hero.Bat_qer[i] += 3
            self.listWidget.addItem('Торговец весело напевая себе под нос заточил вас клинок\n\n')
