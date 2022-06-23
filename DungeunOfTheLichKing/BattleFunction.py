from PyQt5.QtWidgets import QMessageBox
from random import randint
import tracker

class Hero:
    """Класс героя"""
    Bat_qer = [7, 8, 9, 10, 11, 12]
    hp_hero = 100  # показатель героя
    szet = 0  # счетчик боев


# класс для счетчиков разных переменных
class peremenn:
    hp_kolwo = 1  # счетчик для хилки их количество
    Money = 1  # переменная для сбора монет


class Battle:
    """Функция боя"""
    def Battle_test(self):
        """Функция запускает саму битву"""
        Hero.szet += 1  # счетчик боев
        rand = randint(1, 3) # определяется какой будет враг
        """Здорвье врага"""
        hp_maus = 20
        hp_skel = 40
        hp_zombe = 30
        hp_doss = 50
        """Урон врага"""
        Bat_maus = [1, 2, 3, 4, 5, 6]
        Bat_skel = [3, 4, 5, 6, 7, 8]
        Bat_zombe = [2, 3, 4, 5, 6, 7]
        Bat_doss = [6, 7, 8, 9, 10, 11]

        if Hero.szet < 5: # проверка на колличество боёв
            if rand == 1:
                """Вывод текста врага"""
                tracker.Ui_MainWindow.Artmaus(self)
                self.listWidget.addItem('Шагая затемнённому коридору вы услышали шорох.\n'
                                        'Огромная, полугнила крыса с визгом наброслась на вас!\n\n')
                while True:
                    """Проходит симуляция боя"""
                    rand = randint(1, 6)
                    damag_mous = Bat_maus[rand - 1]
                    Hero.hp_hero = Hero.hp_hero - damag_mous

                    self.listWidget.addItem(
                                  'Мышь царапает вас и наносит вам: {} урона у вас осталось {} XP\n'.format(damag_mous,
                                                                                                            Hero.hp_hero))
                    death.death_test(self) # тест на смерть персонажа
                    damag_hero = Hero.Bat_qer[rand - 1]  # int(Bat_qer[rand - 1])
                    hp_maus = hp_maus - damag_hero
                    self.listWidget.addItem('Вы наносите удар и после брызга крови крыса визгнула и зашипела,\n'
                                            'она получилп: {} урона\n'.format(damag_hero))
                    if hp_maus <= 0: # проверка на здоровье врана
                        peremenn.Money += 10
                        self.listWidget.addItem('Вы убили крысу у вас осталось: {} здоровья\n\n'.format(Hero.hp_hero))
                        self.listWidget.addItem('Вы убили крысу и получили 10 монет теперь у вас: {} монет\n\n'.format(
                            peremenn.Money))
                        break
            elif rand == 2:
                tracker.Ui_MainWindow.ArtSkeleton(self)
                self.listWidget.addItem('Зайдя в комнату с каменными гробами, вам путь перегородил высокий скелет в латах!\n\n')
                while True:
                    rand = randint(1, 6)
                    damag_skel = Bat_skel[rand - 1]
                    Hero.hp_hero = Hero.hp_hero - damag_skel
                    self.listWidget.addItem(
                                  'Скелет треща своими костями и громыхая своей бронёй\n'
                                  'бьет вас ржавой алебардой и наносит вам: {} урона у вас осталось {} здоровья\n'.
                                      format(damag_skel, Hero.hp_hero))
                    death.death_test(self)
                    damag_hero = Hero.Bat_qer[rand - 1]
                    hp_skel = hp_skel - damag_hero
                    self.listWidget.addItem('Вы ударили своим мечом и скелет затрещав получет: {} урона\n'.format(damag_hero))
                    if hp_skel <= 0:
                        peremenn.Money += 30
                        self.listWidget.addItem('Вы убили скелета у вас осталось: {} здоровья\n\n'.format(Hero.hp_hero))
                        self.listWidget.addItem('Вы убили скелета и получили 30 монет теперь у вас: {} монет\n\n'.format(
                            peremenn.Money))
                        break
            elif rand == 3:
                self.listWidget.addItem('Вы зашли в команату заваленную гниющими трупами.\n'
                                        'Прочитав короткую молтиву, вы замечаете что один из них зашевелился....\n'
                                        'Он посмотрел на вас пустым взгядом и поковылял в вашу сторону\n\n')
                while True:
                    tracker.Ui_MainWindow.ArtZombie(self)
                    rand = randint(1, 6)
                    damag_zombe = Bat_zombe[rand - 1]
                    Hero.hp_hero = Hero.hp_hero - damag_zombe
                    self.listWidget.addItem(
                                  'Зомби бьёт вас обрубком руки и наносит вам: {} урона у вас осталось {} XP\n'.
                                      format(damag_zombe, Hero.hp_hero))
                    death.death_test(self)
                    damag_hero = Hero.Bat_qer[rand - 1]
                    hp_zombe = hp_zombe - damag_hero
                    self.listWidget.addItem('Вы наносите удар и зомби получет: {} урона\n'.format(damag_hero))
                    if hp_zombe <= 0:
                        peremenn.Money += 20
                        self.listWidget.addItem('Вы убили зомби у вас осталось: {} здоровья\n\n'.format(Hero.hp_hero))
                        self.listWidget.addItem('Вы убили зомби и получили 20 монет теперь у вас: {} монет\n\n'.format(
                            peremenn.Money))
                        break
        elif Hero.szet == 5:
            tracker.Ui_MainWindow.ArtLichboss(self)
            self.listWidget.addItem('Придя в древний тронный зал, вы видите ужасную фигуру на троне\n'
                                    '-Ты уже проиграл, смертный червь, иди же и прими свою смерть!\n\n')
            while True:
                rand = randint(1, 6)
                damag_doss = Bat_doss[rand - 1]
                Hero.hp_hero = Hero.hp_hero - damag_doss
                self.listWidget.addItem(
                              'Лич прочитал заклинание, его огромный меч с черным как ночь клинком\n'
                              'направился к вам и наносит: {} урона у вас осталось {} XP\n'.format(damag_doss,Hero.hp_hero))
                death.death_test(self)
                damag_hero = Hero.Bat_qer[rand - 1]  # int(Bat_qer[rand - 1])
                hp_doss = hp_doss - damag_hero
                self.listWidget.addItem('С молитвой на устах и бьёте своим светящимся клинком и лич получет: {} урона\n'.
                                        format(damag_hero))
                if hp_doss <= 0:
                    self.listWidget.addItem('Вы уничтожили Короля Лича, принцесса спасена!')
                    break



class death:
    """функция, проверка на показатель хп"""
    def death_test(self):
        if Hero.hp_hero <= 0:
            msg = QMessageBox()
            msg.setWindowTitle("Вы умерли....")
            msg.setText("Под напором врага вы не выдержали и пали! Начните сначала.")
            msg.setIcon(QMessageBox.Warning)

            msg.exec_()
            self.listWidget.show()
            self.close
        if Hero.szet == 6: # если все битвы пройдены герой победил
            msg = QMessageBox()
            msg.setWindowTitle("Вы победили")
            msg.setText("Король Лич побеждён!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            self.listWidget.show()
            self.close



class clicked:
    """Класс привязанный к кнопке для запуска функций"""
    def clicked_resum(self):
        Battle.Battle_test(self)
        death.death_test(self)

# функция зелья здоровья
class Health:

    def Health_Potion(self):
        """Функция выстанавливающая здорвье главного героя"""
        if peremenn.hp_kolwo != 0:
            Hero.hp_hero = Hero.hp_hero + 20
            self.listWidget.addItem('Испив волшебное зелье, вы чувствуете прилив сил.\n'
                                    'Вы востановили 20 очков здоровья и ваше здоровье = {} \n\n'.format(Hero.hp_hero))
            peremenn.hp_kolwo -= 1
