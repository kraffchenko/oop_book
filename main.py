from text_handler import (get_key_from_line, update_value, update_dict, reset_value,
take_alt_path, append_path)
from CTkMessagebox import CTkMessagebox
import customtkinter
from PIL import Image
import random


import tkinter as tk

sections = {}


class Section:
    def __init__(self, section_number, section_text):
        self.number = section_number
        self.text = section_text
        self.next_sections = []
        self.needed_items = None
        self.related_section = None
        self.type = None
        self.parent_section = None

class Character:
    def __init__(self, force, agility, resistence):
        self.force = force
        self.agility = agility
        self.resistence = resistence

class Item:
    def __init__(self, name):
        self.name = name
class Weapon(Item):
    def __init__(self, name, hit_buff):
        super().__init__(name)
        self.status = None
        self.hit_buff = hit_buff


class Armor(Item):
    def __init__(self, name, defence_buff, armor_type):
        super().__init__(name)
        self.status = None
        self.defence_buff = defence_buff
        self.armor_type = armor_type


class MainCharacter(Character):
    def __init__(self, force, agility, resistence):
        super().__init__(force, agility, resistence)
        self.soul_points = None
        self.weapon = None
        self.head_armor = None
        self.body_armor = None
        self.legs_armor = None
        self.feet_armor = None
        self.arms_armor = None

        self.inventory = []





with open("texte.txt", encoding='utf-8') as file:

    value = ""
    key = ""
    times = 0

    for line in file:
        if "###" in line and times == 0:
            key = get_key_from_line(line)
            times += 1
        elif "###" not in line:
            value = update_value(value, line)
        else:
            section = Section(key, value)
            sections[key] = section
            key = reset_value()
            value = reset_value()
            key = get_key_from_line(line)
    sections[key] = section

all_pathes = [["72"],  ["15"], ["90"], ["46"], ["60", "56"], ["38"], ["10"], ["89"], ["13"], ["40", "97"], ["100"],
              ["71"], ["77"], ["88"], ["92"], ["3"], ["33"], ["16"], ["11"], ["90"], ["76"], ["55"], ["7"], ["33"],
              ["58"], ["65"], ["35"], ["42", "40", "71"], ["101"], ["292"], ["K1"], ["K1"], ["256", "105"], ["271"],
              ["K59", "K8"]]

sections_keys_list = list(sections.keys())
for index in range(0, 35):
    for cur_object in all_pathes[index]:
        sections[sections_keys_list[index]].next_sections.append(sections[cur_object])


main_char = MainCharacter(5, 5, 6)
sections["42"].related_section = sections["11"]
sections["42"].type = "item_check"
sections["271"].related_section = sections["271"]
sections["271"].type = "test"
sections["K8"].related_section = [sections["K59"]]
sections["K8"].type = "fight"
sections["K59"].related_section = [sections["K59"]]
sections["K59"].type = "fight"
sections["60"].parent_section = sections["11"]
sections["56"].parent_section = sections["11"]
def ask_question():

    msg = CTkMessagebox(title="Choose your destiny!", message="Nimmst du die Öllaterne oder das Schwert?",
                        icon="question", option_1="Öllaterne", option_2="Schwert", option_3="Beide")
    response = msg.get()
    lantern = Item("Öllaterne")
    basic_sword = Weapon("Schwert", 3)
    sections["60"].needed_items = [basic_sword]
    sections["56"].needed_items = [lantern]

    if response == "Öllaterne":
        msg.destroy()
        main_char.inventory.append(lantern)
        return
    elif response == "Schwert":
        msg.destroy()
        main_char.inventory.append(basic_sword)
        return
    else:
        msg.destroy()
        main_char.inventory.extend([basic_sword, lantern])

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.toplevel_window = None
        self.current_section = sections["1"]

        self.geometry("650x650")
        self.resizable(False, False)
        self.configure(fg_color='gray11')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.button = customtkinter.CTkButton(master=self, text="Weiter", command=self.next,
                                                          fg_color='gray11', hover_color='gray')
        self.button.grid(column=0, row=2, rowspan=2, columnspan=2, sticky="nsew")
        self.second_button = customtkinter.CTkButton(master=self, text="Weiter", command=self.alt_next,
                                                     fg_color='gray11', hover_color='gray')
        self.third_button = customtkinter.CTkButton(master=self, text="Weiter", command=self.second_alt_next,
                                                    fg_color='gray11', hover_color='gray')

        self.title("Abenteuer")

        self.text_font = customtkinter.CTkFont(family="Arial", size=17)
        self.textbox = customtkinter.CTkTextbox(master=self, corner_radius=0, fg_color="transparent", font=self.text_font)
        self.textbox.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=50)
        self.textbox.insert("0.0", self.current_section.text)

        self.header_font = customtkinter.CTkFont(family="Arial", size=13)
        self.header = customtkinter.CTkLabel(master=self, corner_radius=0, fg_color="transparent", font=self.header_font, text=self.current_section.number)
        self.header.grid(row=0, column=0, columnspan=2)

    def len_checker(self, next_sections):
        for widget in self.winfo_children():
            if isinstance(widget, customtkinter.CTkButton):
                widget.destroy()
        if len(self.current_section.next_sections) == 1:
            self.button = customtkinter.CTkButton(master=self, text="Weiter", command=self.next,
                                                  fg_color='gray11', hover_color='gray')
            self.button.grid(column=0, row=2, rowspan=2, columnspan=2, sticky="nsew")
        elif len(self.current_section.next_sections) == 2:
            self.button = customtkinter.CTkButton(master=self, text=f"Zur Sektion {next_sections[0].number}", command=self.next,
                                                  fg_color='gray11', hover_color='gray')
            self.button.grid(column=0, row=2, sticky="nsew", rowspan=2)
            self.second_button = customtkinter.CTkButton(master=self, text=f"Zur Sektion {next_sections[1].number}", command=self.alt_next,
                                                  fg_color='gray11', hover_color='gray')
            self.second_button.grid(column=1, row=2, rowspan=2, sticky="nsew")
        else:
            self.button = customtkinter.CTkButton(master=self, text=f"Zur Sektion {next_sections[0].number}", command=self.next,
                                                  fg_color='gray11', hover_color='gray')
            self.button.grid(column=0, row=2, sticky="nsew")
            self.second_button = customtkinter.CTkButton(master=self, text=f"Zur Sektion {next_sections[1].number}", command=self.alt_next,
                                                  fg_color='gray11', hover_color='gray')
            self.second_button.grid(column=1, row=2, sticky="nsew")
            self.third_button = customtkinter.CTkButton(master=self, text=f"Zur Sektion {next_sections[2].number}", command=self.second_alt_next,
                                                  fg_color='gray11', hover_color='gray')
            self.third_button.grid(column=0, row=3, columnspan=2, sticky="nsew")

    def create_test_force_window(self, related_section):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ForceTestWindow(needed_points=14, related_section=related_section)
        else:
            self.toplevel_window.focus()

    def create_fight_window(self, force, agility, resistence):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = FightWindow(enemy_attack=force,
                                               enemy_defence=agility, enemy_resistence=resistence)
        else:
            self.toplevel_window.focus()

    def item_checker(self, related_section):
        for section in sections.values():
            if section == related_section:
                for next_section in related_section.next_sections:
                    for item in next_section.needed_items:
                        if main_char.inventory.count(item) == 0:
                            related_section.next_sections.remove(next_section)
        self.len_checker(self.current_section.next_sections)

    def test_checker(self, status, related_section):
        print(related_section)
        if status == True:
            related_section.next_sections.remove(related_section.next_sections[1])
        elif status == False:
            related_section.next_sections.remove(related_section.next_sections[0])
        self.len_checker(self.current_section.next_sections)

    def event_checker(self, current_section):
        section_found = False
        events = {
            "42": ask_question,
            "271": self.create_test_force_window,
            "K8": [self.create_fight_window, 10, 10, 2],
            "K59": [self.create_fight_window, 10, 10, 2],
        }
        for section in events.keys():
            if current_section.number == section:
                section_found = True
                if current_section.type == "item_check":
                    events[section]()
                    self.item_checker(current_section.related_section)
                elif current_section.type == "test":
                    events[section](current_section.related_section)
                elif current_section.type == "fight":
                    events[section][0](events[section][1], events[section][2], events[section][3])
        if section_found == False:
            self.len_checker(current_section.next_sections)


    def update_text(self, text):
        self.textbox.delete("0.0", tk.END)
        self.textbox.insert("0.0", text)

    def update_header(self, section):
        self.header.destroy()

        self.header = customtkinter.CTkLabel(master=self, corner_radius=0, fg_color="transparent", font=self.header_font,
                                             text=f"Sektion {section}")
        self.header.grid(row=0, column=0, columnspan=2)

    def next(self):
        next_section = self.current_section.next_sections[0]
        header = next_section.number
        text = next_section.text
        self.current_section = next_section
        return self.update_text(text), self.update_header(header), self.event_checker(self.current_section)

    def alt_next(self):
        next_section = self.current_section.next_sections[1]
        header = next_section.number
        text = next_section.text
        self.current_section = next_section
        return self.update_text(text), self.update_header(header), self.event_checker(self.current_section)

    def second_alt_next(self):
        next_section = self.current_section.next_sections[2]
        header = next_section.number
        text = next_section.text
        self.current_section = next_section
        return self.update_text(text), self.update_header(header), self.event_checker(self.current_section)

class ForceTestWindow(customtkinter.CTkToplevel):
    def __init__(self, needed_points, related_section):
        super().__init__()
        self.geometry("400x300")
        self.geometry("650x650")
        self.won = False
        self.resizable(False, False)
        self.configure(fg_color='gray11')
        self.needed_points = needed_points - main_char.force
        self.related_section = related_section
        self.images = {
            1: "./images/dice_1.png",
            2: "./images/dice_2.png",
            3: "./images/dice_3.png",
            4: "./images/dice_4.png",
            5: "./images/dice_5.png",
            6: "./images/dice_6.png",
        }

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=1)
        self.font = customtkinter.CTkFont(family="Arial", size=20)

        self.top_label = customtkinter.CTkLabel(self, text=f"Du brauchst {self.needed_points} Punkte", fg_color="transparent", font=self.font)
        self.top_label.grid(row=0, column=0, columnspan=2)

        self.first_dice_image = customtkinter.CTkImage(light_image=Image.open(self.images[1]),
                                  dark_image=Image.open(self.images[1]),
                                  size=(150, 150))
        self.first_dice = customtkinter.CTkLabel(self, image=self.first_dice_image, text="")
        self.first_dice.grid(column=0, row=1)

        self.second_dice_image = customtkinter.CTkImage(light_image=Image.open(self.images[1]),
                                  dark_image=Image.open(self.images[1]),
                                  size=(150, 150))
        self.second_dice = customtkinter.CTkLabel(self, image=self.second_dice_image, text="")
        self.second_dice.grid(column=1, row=1)

        self.button = customtkinter.CTkButton(self, text="Würfeln", command=self.roll_dice, font=self.font, width=200, height=75)

        self.button.grid(column=0, row=2, columnspan=2,)

    def change_top_label(self, points):
        self.top_label.destroy()
        self.top_label = customtkinter.CTkLabel(self, text=f"Du hast {points} Punkte", fg_color="transparent",
                                                font=self.font)
        self.top_label.grid(row=0, column=0, columnspan=2)

    def change_dice_pictures(self, first_dice_points, second_dice_points):
        self.first_dice.destroy()
        self.second_dice.destroy()
        self.first_dice_image = customtkinter.CTkImage(light_image=Image.open(self.images[first_dice_points]),
                                                       dark_image=Image.open(self.images[first_dice_points]),
                                                       size=(150, 150))
        self.first_dice = customtkinter.CTkLabel(self, image=self.first_dice_image, text="")
        self.first_dice.grid(column=0, row=1)

        self.second_dice_image = customtkinter.CTkImage(light_image=Image.open(self.images[second_dice_points]),
                                                        dark_image=Image.open(self.images[second_dice_points]),
                                                        size=(150, 150))
        self.second_dice = customtkinter.CTkLabel(self, image=self.second_dice_image, text="")
        self.second_dice.grid(column=1, row=1)

    def change_button(self):
        self.button = customtkinter.CTkButton(self, text="Verlassen", command=self.destroy_window, font=self.font,
                                              width=200, height=75)
        self.button.grid(column=0, row=2, columnspan=2, )

    def win_window(self):
        pass

    def lose_window(self):
        pass

    def roll_dice(self):
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        points = first_dice + second_dice
        if points > self.needed_points:
            self.won = True
        if points <= self.needed_points:
            main_char.resistence -= 1
            self.won = False

        return self.change_top_label(points), self.change_dice_pictures(first_dice, second_dice), self.change_button()

    def destroy_window(self):
        return self.destroy(), app.test_checker(self.won, self.related_section)

class FightWindow(customtkinter.CTkToplevel):
    def __init__(self, enemy_attack, enemy_defence, enemy_resistence):
        super().__init__()
        self.geometry("400x300")
        self.geometry("650x650")
        self.won = None
        self.resizable(False, False)
        self.configure(fg_color='gray11')
        self.opp = Character(enemy_attack, enemy_defence, enemy_resistence)


        self.images = {
            1: "./images/dice_1.png",
            2: "./images/dice_2.png",
            3: "./images/dice_3.png",
            4: "./images/dice_4.png",
            5: "./images/dice_5.png",
            6: "./images/dice_6.png",
        }

        self.round = 1
        self.my_attack = main_char.force + main_char.weapon.hit_buff
        self.my_defence = (main_char.agility + main_char.head_armor.defence_buff + main_char.body_armor.defence_buff
                   + main_char.arms_armor.defence_buff + main_char.legs_armor.defence_buff
                   + main_char.feet_armor.defence_buff)


        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.font = customtkinter.CTkFont(family="Arial", size=20)

        self.top_label = customtkinter.CTkLabel(self, text=f"{self.round} Runde", fg_color="transparent", font=self.font)
        self.top_label.grid(row=0, column=1, columnspan=3)

        self.my_chars_label = customtkinter.CTkLabel(self,
                                                        text=f"Angriff: {self.my_attack}"
                                                             f"\nVerteidigung: {self.my_defence}"
                                                             f"\nHP: {main_char.resistence}", fg_color="transparent",
                                                        font=self.font)
        self.my_chars_label .grid(row=1, column=0, columnspan=2)

        self.enemy_chars_label = customtkinter.CTkLabel(self,
                                                        text=f"Angriff: {self.opp.force}"
                                                             f"\nVerteidigung: {self.opp.agility}"
                                                             f"\nHP: {self.opp.resistence}", fg_color="transparent",
                                                        font=self.font)
        self.enemy_chars_label .grid(row=1, column=3, columnspan=2)

        self.my_first_dice_image = customtkinter.CTkImage(light_image=Image.open(self.images[1]),
                                  dark_image=Image.open(self.images[1]),
                                  size=(100, 100))
        self.my_first_dice = customtkinter.CTkLabel(self, image=self.my_first_dice_image, text="")
        self.my_first_dice.grid(column=0, row=2)

        self.my_second_dice_image = customtkinter.CTkImage(light_image=Image.open(self.images[1]),
                                  dark_image=Image.open(self.images[1]),
                                  size=(100, 100))
        self.my_second_dice = customtkinter.CTkLabel(self, image=self.my_second_dice_image, text="")
        self.my_second_dice.grid(column=1, row=2)

        self.enemy_first_dice_image = customtkinter.CTkImage(light_image=Image.open(self.images[1]),
                                  dark_image=Image.open(self.images[1]),
                                  size=(100, 100))
        self.enemy_first_dice = customtkinter.CTkLabel(self, image=self.enemy_first_dice_image, text="")
        self.enemy_first_dice.grid(column=3, row=2)

        self.enemy_second_dice_image = customtkinter.CTkImage(light_image=Image.open(self.images[1]),
                                  dark_image=Image.open(self.images[1]),
                                  size=(100, 100))
        self.enemy_second_dice = customtkinter.CTkLabel(self, image=self.enemy_second_dice_image, text="")
        self.enemy_second_dice.grid(column=4, row=2)

        self.event_log = customtkinter.CTkTextbox(master=self, corner_radius=0, fg_color="transparent", font=self.font)
        self.event_log.grid(row=3, column=1, columnspan=3, rowspan=2, sticky="nsew")
        self.event_log.insert("0.0", "Warten auf den Anfang des Kampfes")

        self.button = customtkinter.CTkButton(self, text="Würfeln", command=self.roll_dice, font=self.font, width=200, height=75)
        self.button.grid(column=1, row=4, columnspan=3)

    def change_top_label(self):
        self.top_label.destroy()
        self.top_label = customtkinter.CTkLabel(self, text=f"{self.round} Runde", fg_color="transparent", font=self.font)
        self.top_label.grid(row=0, column=1, columnspan=3)

    def change_enemy_label(self):
        self.enemy_chars_label = customtkinter.CTkLabel(self,
                                                        text=f"Angriff: {self.opp.force}"
                                                             f"\nVerteidigung: {self.opp.agility}"
                                                             f"\nHP: {self.opp.resistence}", fg_color="transparent",
                                                        font=self.font)
        self.enemy_chars_label.grid(row=1, column=3, columnspan=2)

    def change_my_label(self):
        self.my_chars_label = customtkinter.CTkLabel(self,
                                                     text=f"Angriff: {self.my_attack}"
                                                          f"\nVerteidigung: {self.my_defence}"
                                                          f"\nHP: {main_char.resistence}", fg_color="transparent",
                                                     font=self.font)
        self.my_chars_label .grid(row=1, column=0, columnspan=2)

    def change_dice_pictures(self, first_dice_points, second_dice_points, third_dice_points, fourth_dice_points):
        self.my_first_dice.destroy()
        self.my_second_dice.destroy()
        self.enemy_first_dice.destroy()
        self.enemy_second_dice.destroy()
        first_dice_image = customtkinter.CTkImage(light_image=Image.open(self.images[first_dice_points]),
                                  dark_image=Image.open(self.images[first_dice_points]),
                                  size=(100, 100))
        first_dice = customtkinter.CTkLabel(self, image=first_dice_image, text="")
        first_dice.grid(column=0, row=2)

        second_dice_image = customtkinter.CTkImage(light_image=Image.open(self.images[second_dice_points]),
                                  dark_image=Image.open(self.images[second_dice_points]),
                                  size=(100, 100))
        second_dice = customtkinter.CTkLabel(self, image=second_dice_image, text="")
        second_dice.grid(column=1, row=2)
        third_dice_image = customtkinter.CTkImage(light_image=Image.open(self.images[third_dice_points]),
                                  dark_image=Image.open(self.images[third_dice_points]),
                                  size=(100, 100))
        third_dice = customtkinter.CTkLabel(self, image=third_dice_image, text="")
        third_dice.grid(column=3, row=2)

        fourth_dice_image = customtkinter.CTkImage(light_image=Image.open(self.images[fourth_dice_points]),
                                  dark_image=Image.open(self.images[fourth_dice_points]),
                                  size=(100, 100))
        fourth_dice = customtkinter.CTkLabel(self, image=fourth_dice_image, text="")
        fourth_dice.grid(column=4, row=2)


    def hp_checker(self):
        if main_char.resistence == 0:
            self.won = False
        elif self.opp.resistence == 0:
            self.won = True
        return self.won

    def end_function(self):
        died = self.hp_checker()
        if died == True:
            self.destroy_window()
        elif died == False:
            self.destroy_window()

    def enemy_roles(self):
        self.button.destroy()
        self.button = customtkinter.CTkButton(self, text="Würfeln", command=self.roll_dice, font=self.font, width=200, height=75)
        self.button.grid(column=1, row=4, columnspan=3)
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        third_dice = random.randint(1, 6)
        fourth_dice = random.randint(1, 6)
        points = third_dice + fourth_dice + self.opp.agility
        defence = first_dice + second_dice + self.my_defence
        self.round += 1
        if points > defence:
            main_char.resistence -= 1
            self.event_log.delete("0.0", tk.END)
            self.event_log.insert("0.0", f"Du hast {defence} Verteidigungspunkte und dein Gegner hat mit {points} Angriffspunkten leider getroffen! Jetzt bist du dran.")
        else:
            self.event_log.delete("0.0", tk.END)
            self.event_log.insert("0.0", f"Der Gegner hat mit {points} Angriffspunkten nicht geschafft, dich mit {defence} Verteidigungspunkten zu treffen, jetzt bist du dran!")


        return self.change_top_label(), self.change_dice_pictures(first_dice, second_dice, third_dice, fourth_dice), self.change_my_label(), self.end_function()

    def roll_dice(self):
        self.button.destroy()
        self.button = customtkinter.CTkButton(self, text="Lass den Gegner würfeln", command=self.enemy_roles, font=self.font, width=200, height=75)
        self.button.grid(column=1, row=4, columnspan=3)
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        third_dice = random.randint(1, 6)
        fourth_dice = random.randint(1, 6)
        points = first_dice + second_dice + self.my_attack
        enemy_defence = third_dice + fourth_dice + self.opp.agility
        self.round += 1
        if points > enemy_defence:
            self.opp.resistence -= 1
            self.event_log.delete("0.0", tk.END)
            self.event_log.insert("0.0", f"Gut gemacht! Du hast mit {points} Angriffspunkten deinen Gegner mit {enemy_defence} Verteidigungspunkten getroffen! Jetzt ist dein Gegner dran!")
        else:
            self.event_log.delete("0.0", tk.END)
            self.event_log.insert("0.0", f"Leider hast du mit {points} Angriffspunkten deinen Gegner mit {enemy_defence} Verteidigungspunkten nicht getroffen! Jetzt ist dein Gegner dran!")


        return self.change_top_label(), self.change_dice_pictures(first_dice, second_dice, third_dice, fourth_dice),self.change_enemy_label(), self.end_function()

    def destroy_window(self):
        return self.destroy(),


#затригерить айтем чекер не только на 42 секции а в целом, либо поменять айтем чекер на добаввление секции а не на удаление
#разобраться с рассчетом атаки и защиты
#посмотреть можно ли из всех чекеров сделать статические функции
#посмотреть как более независимо использовать класс керектер и класс мейнкеректер в битве не создавая каждый раз селф объект

print(sections)
app = App()
app.mainloop()

