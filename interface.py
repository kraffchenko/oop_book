from CTkMessagebox import CTkMessagebox
import customtkinter
from PIL import Image
import random


import tkinter as tk




class ForceTestWindow(customtkinter.CTkToplevel):
    def __init__(self, parent, needed_points, default_force, section, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.geometry("400x300")
        self.geometry("650x650")
        self.won = False
        self.resizable(False, False)
        self.configure(fg_color='gray11')
        self.vitality = parent.vitality
        self.parent_function = parent.test_checker
        self.needed_points = needed_points - default_force
        self.section = section
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
        self.top_label = customtkinter.CTkLabel(self, text=f"Du hast {points} Punkte", fg_color="transparent", font=self.font)
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
        self.button = customtkinter.CTkButton(self, text="Verlassen", command=self.destroy_window, font=self.font, width=200, height=75)
        self.button.grid(column=0, row=2, columnspan=2,)

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
        if points < self.needed_points:
            self.parent.vitality -= 1
            self.won = False


        return self.change_top_label(points), self.change_dice_pictures(first_dice, second_dice), self.change_button()

    def destroy_window(self):
        return self.destroy(), self.parent_function(self.won, self.section)

class FightWindow(customtkinter.CTkToplevel):
    def __init__(self, parent, my_attack, my_defence, my_resistence, enemy_attack, enemy_defence, enemy_resistence, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.geometry("400x300")
        self.geometry("650x650")
        self.won = None
        self.resizable(False, False)
        self.configure(fg_color='gray11')


        self.images = {
            1: "./images/dice_1.png",
            2: "./images/dice_2.png",
            3: "./images/dice_3.png",
            4: "./images/dice_4.png",
            5: "./images/dice_5.png",
            6: "./images/dice_6.png",
        }

        self.round = 1

        self.my_attack = my_attack
        self.my_defence = my_defence
        self.my_resistence = my_resistence

        self.enemy_attack = enemy_attack
        self.enemy_defence = enemy_defence
        self.enemy_resistence = enemy_resistence

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
                                                             f"\nHP: {self.my_resistence}", fg_color="transparent",
                                                        font=self.font)
        self.my_chars_label .grid(row=1, column=0, columnspan=2)

        self.enemy_chars_label = customtkinter.CTkLabel(self,
                                                        text=f"Angriff: {self.enemy_attack}"
                                                             f"\nVerteidigung: {self.enemy_defence}"
                                                             f"\nHP: {self.enemy_resistence}", fg_color="transparent",
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
                                                        text=f"Angriff: {self.enemy_attack}"
                                                             f"\nVerteidigung: {self.enemy_defence}"
                                                             f"\nHP: {self.enemy_resistence}", fg_color="transparent",
                                                        font=self.font)
        self.enemy_chars_label.grid(row=1, column=3, columnspan=2)

    def change_my_label(self):
        self.my_chars_label = customtkinter.CTkLabel(self,
                                                     text=f"Angriff: {self.my_attack}"
                                                          f"\nVerteidigung: {self.my_defence}"
                                                          f"\nHP: {self.my_resistence}", fg_color="transparent",
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
        if self.my_resistence == 0:
            self.won = False
        elif self.enemy_resistence == 0:
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
        points = third_dice + fourth_dice + self.enemy_attack
        defence = first_dice + second_dice + self.my_defence
        self.round += 1
        if points > defence:
            self.my_resistence -= 1
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
        enemy_defence = third_dice + fourth_dice + self.enemy_defence
        self.round += 1
        if points > enemy_defence:
            self.enemy_resistence -= 1
            self.event_log.delete("0.0", tk.END)
            self.event_log.insert("0.0", f"Gut gemacht! Du hast mit {points} Angriffspunkten deinen Gegner mit {enemy_defence} Verteidigungspunkten getroffen! Jetzt ist dein Gegner dran!")
        else:
            self.event_log.delete("0.0", tk.END)
            self.event_log.insert("0.0", f"Leider hast du mit {points} Angriffspunkten deinen Gegner mit {enemy_defence} Verteidigungspunkten nicht getroffen! Jetzt ist dein Gegner dran!")


        return self.change_top_label(), self.change_dice_pictures(first_dice, second_dice, third_dice, fourth_dice),self.change_enemy_label(), self.end_function()

    def destroy_window(self):
        return self.destroy(),







def ask_question(parent):

    msg = CTkMessagebox(title="Choose your destiny!", message="Nimmst du die Öllaterne oder das Schwert?",
                        icon="question", option_1="Öllaterne", option_2="Schwert", option_3="Beide")
    response = msg.get()

    if response == "Öllaterne":
        msg.destroy()
        parent.book["items"].append("Öllaterne")
        return
    elif response == "Schwert":
        msg.destroy()
        parent.book["items"].append("Schwert")
        parent.characteristics["characteristics"]["weapons"][1]["name"] = "Schwert"
        parent.characteristics["characteristics"]["weapons"][1]["hit_buff"] = 3
        return
    else:
        msg.destroy()
        parent.book["items"].extend(["Schwert", "Öllaterne"])




class App(customtkinter.CTk):
    def __init__(self, book, characteristics, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.book = book

        self.characteristics = characteristics
        self.toplevel_window = None
        self.section_256_test = None

        self.current_path = self.book["Sections"]["1"]

        self.defence = None
        self.attack = None
        self.force = characteristics["characteristics"]["perks"]["force"]
        self.vitality = 6

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
        self.textbox.insert("0.0", self.current_path["text"])

        self.header_font = customtkinter.CTkFont(family="Arial", size=13)
        self.header = customtkinter.CTkLabel(master=self, corner_radius=0, fg_color="transparent", font=self.header_font, text=f"Sektion 1")
        self.header.grid(row=0, column=0, columnspan=2)

    def update_text(self, text):
        self.textbox.delete("0.0", tk.END)
        self.textbox.insert("0.0", text)

    def update_header(self, section):
        self.header.destroy()

        self.header = customtkinter.CTkLabel(master=self, corner_radius=0, fg_color="transparent", font=self.header_font,
                                             text=f"Sektion {section}")
        self.header.grid(row=0, column=0, columnspan=2)

    def len_checker(self, options):
        for widget in self.winfo_children():
            if isinstance(widget, customtkinter.CTkButton):
                widget.destroy()
        if len(self.current_path['path']) == 1:
            self.button = customtkinter.CTkButton(master=self, text="Weiter", command=self.next,
                                                  fg_color='gray11', hover_color='gray')
            self.button.grid(column=0, row=2, rowspan=2, columnspan=2, sticky="nsew")
        elif len(self.current_path['path']) == 2:
            self.button = customtkinter.CTkButton(master=self, text=f"Zur Sektion {options[0]}", command=self.next,
                                                  fg_color='gray11', hover_color='gray')
            self.button.grid(column=0, row=2, sticky="nsew", rowspan=2)
            self.second_button = customtkinter.CTkButton(master=self, text=f"Zur Sektion {options[1]}", command=self.alt_next,
                                                  fg_color='gray11', hover_color='gray')
            self.second_button.grid(column=1, row=2, rowspan=2, sticky="nsew")
        else:
            self.button = customtkinter.CTkButton(master=self, text=f"Zur Sektion {options[0]}", command=self.next,
                                                  fg_color='gray11', hover_color='gray')
            self.button.grid(column=0, row=2, sticky="nsew")
            self.second_button = customtkinter.CTkButton(master=self, text=f"Zur Sektion {options[1]}", command=self.alt_next,
                                                  fg_color='gray11', hover_color='gray')
            self.second_button.grid(column=1, row=2, sticky="nsew")
            self.third_button = customtkinter.CTkButton(master=self, text=f"Zur Sektion {options[2]}", command=self.second_alt_next,
                                                  fg_color='gray11', hover_color='gray')
            self.third_button.grid(column=0, row=3, columnspan=2, sticky="nsew")


    def defence_counter(self):
        agility = self.characteristics["characteristics"]["perks"]["agility"]
        clothes = self.characteristics["characteristics"]["clothes"]
        defence_buff = 0
        items = clothes.keys()
        for item in items:
            buff = clothes[item]["defence_buff"]
            defence_buff += buff
        self.defence = agility + defence_buff
        return self.defence


    def attack_counter(self):
        weapons = self.characteristics["characteristics"]["weapons"]
        hit_buff = 0
        items = weapons.keys()
        for item in items:
            buff = weapons[item]["hit_buff"]
            hit_buff += buff
            print(buff)
        self.attack = self.force + hit_buff
        return self.attack

    def create_test_force_window(self, section):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ForceTestWindow(parent=self, needed_points=14, default_force=self.force, section=section)
        else:
            self.toplevel_window.focus()

    def create_fight_window(self, attack, defence, resistence):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = FightWindow(parent=self, my_defence=self.defence_counter(),
                                               my_attack=self.attack_counter(), my_resistence=self.vitality, enemy_attack=attack,
                                               enemy_defence=defence, enemy_resistence=resistence)
        else:
            self.toplevel_window.focus()




    def test_checker(self, status, section):
        tests = {
            "tests": {
                "parent_section": {
                    "271": {"256": True,
                            "105": False
                            },
                },
            }
        }
        reviewed_sections = tests["tests"]["parent_section"][section].keys()
        for child_section in reviewed_sections:
            searched_status = tests["tests"]["parent_section"][section][child_section]
            if searched_status != status:
                self.book["Sections"][section]["path"].remove(child_section)
        self.len_checker(self.current_path['path'])

    def item_checker(self, section):
        user_items = self.book["items"]
        needed_items = {
            "needed_items": {
                "parent_section": {
                    "11": {"60": ["Schwert"],
                           "56": ["Öllaterne"]
                           },
                },
            }
        }
        reviewed_sections = needed_items["needed_items"]["parent_section"][section].keys()
        for child_section in reviewed_sections:
            searched_items = needed_items["needed_items"]["parent_section"][section][child_section]
            for item in searched_items:
                if user_items.count(item) == 0:
                    self.book["Sections"][section]["path"].remove(child_section)
                else:
                    pass
        self.len_checker(self.current_path['path'])

    def event_checker(self, section):
        section_found = False
        events = {
            "events": {
                "42": {
                    "func": ask_question,
                    "related_section": "11",
                    "type": "item_check"
                },
                "271": {
                    "func": self.create_test_force_window,
                    "related_section": "271",
                    "type": "test"
                },
                "K8": {
                    "func": self.create_fight_window,
                    "related_section": "K59",
                    "type": "fight",
                    "enemy": {
                        "attack": 11,
                        "defence": 10,
                        "resistence": 2,

                    }
                },
                "K59": {
                    "func": self.create_fight_window,
                    "related_section": "K59",
                    "type": "fight",
                    "enemy": {
                        "attack": 10,
                        "defence": 10,
                        "resistence": 2,
                    }
                },


            },
        }
        all_sections = events["events"].keys()
        for one_section in all_sections:
            if one_section == section:
                section_found = True
                if events["events"][section]["type"] == "item_check":
                    events["events"][section]["func"](self)
                    self.item_checker(events["events"][section]["related_section"])
                elif events["events"][section]["type"] == "test":
                    events["events"][section]["func"](section)
                    self.item_checker(events["events"][section]["related_section"])
                elif events["events"][section]["type"] == "fight":
                    attack = events["events"][section]["enemy"]["attack"]
                    defence = events["events"][section]["enemy"]["defence"]
                    resistence = events["events"][section]["enemy"]["resistence"]
                    events["events"][section]["func"](attack, defence, resistence)
                    self.item_checker(events["events"][section]["related_section"])
        if section_found == False:
            self.len_checker(self.current_path['path'])






    def next(self):
        header = self.current_path['path'][0]
        text = self.book["Sections"][self.current_path['path'][0]]['text']
        self.current_path = self.book["Sections"][self.current_path['path'][0]]

        return self.update_text(text), self.current_path, self.update_header(header), self.event_checker(header)

    def alt_next(self):
        text = f"{self.book["Sections"][self.current_path['path'][1]]['text']}"
        header = self.current_path['path'][1]
        self.current_path = self.book["Sections"][self.current_path['path'][1]]

        return self.update_text(text), self.current_path, self.update_header(header), self.event_checker(header),

    def second_alt_next(self):
        text = f"{self.book["Sections"][self.current_path['path'][2]]['text']}"
        header = self.current_path['path'][2]
        self.current_path = self.book["Sections"][self.current_path['path'][2]]

        return self.update_text(text), self.current_path, self.event_checker(header), self.update_header(header),