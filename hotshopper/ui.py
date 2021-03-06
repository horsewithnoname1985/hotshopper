import tkinter as tk
from tkinter import ttk


class View(tk.Tk):

    def __init__(self):
        super(View, self).__init__()
        self.title("Hotshopper")
        self.configure(background="#444")
        self.geometry("900x1000")
        self.controller = None
        self.frm_recipes = None
        self.frm_shopping_lists = None

    def initialize(self, controller, recipes):
        self.controller = controller
        self.frm_recipes = RecipeSelection(self, recipes)
        self.frm_recipes.grid(row=0, column=0, sticky="nw")

    def display_shopping_lists(self, shopping_lists):
        self.frm_shopping_lists = None
        frm_shopping_lists = ShoppingListsFrame(self, shopping_lists)
        frm_shopping_lists.grid(column=1, row=0, sticky="nw")
        frm_shopping_lists.add_shopping_list_frames()
        frm_shopping_lists.update_scroll_region()

    def add_frame(self, frame, row, column):
        frame.grid(column=column, row=row, sticky="nw")


class RecipeCheckbutton:

    def __init__(self, master, recipe, week):
        self.recipe = recipe
        self.week = week
        self.selected = tk.BooleanVar()
        self.button = tk.Checkbutton(master,
                                     variable=self.selected,
                                     onvalue=True,
                                     offvalue=False,
                                     command=self.set_selected,
                                     bg="#444",
                                     fg="white")

    def set_selected(self):
        self.recipe.set_selected(self.recipe, self.selected, self.week)

    def get(self):
        return self.button


class RecipeSelection(tk.Frame):

    def __init__(self, master, recipes):
        tk.Frame.__init__(self, master, bg="#444", padx=10)
        self.master = master
        self.recipes = recipes

        # create and position frames
        self.frame_header = tk.Frame(self, bg="#444")
        self.frame_canvas = tk.Frame(self, bg="#444")
        self.canvas_recipes = tk.Canvas(self.frame_canvas, width=500,
                                        height=900,
                                        bg="#444",
                                        scrollregion=(0, 0, 0, 900))
        self.frame_buttons = tk.Frame(self, bg="#444")
        self.frame_recipes = tk.Frame(self.canvas_recipes, bg="#444", padx=3)

        self.frame_header.grid(row=0, column=0, sticky="w")
        self.frame_canvas.grid(row=1, column=0, sticky="w")
        self.canvas_recipes.grid(row=0, column=0, sticky="ew")
        self.frame_buttons.grid(row=2, column=0, sticky="ew")

        # add content to frames
        self.fill_header()
        self.fill_recipes()
        self.add_buttons()

        self.update_scroll_region()

        # add scrollbar for recipes
        self.vsb = ttk.Scrollbar(self.frame_canvas, orient="vertical",
                                 command=self.canvas_recipes.yview)
        self.vsb.grid(row=0, column=4, sticky="ns")

        self.canvas_recipes.create_window((0, 0), width=500,
                                          window=self.frame_recipes,
                                          anchor="nw"
                                          )
        self.canvas_recipes.config(yscrollcommand=self.vsb.set)

    def fill_header(self):
        current_row = 0
        frame = self.frame_header

        tk.Label(frame, text="Woche", bg="#444", fg="white").grid(
            row=current_row,
            column=0,
            columnspan=4,
            sticky="ew")
        current_row += 1

        tk.Label(frame, text="1", bg="#444", fg="white", padx=5).grid(
            row=current_row, column=0, sticky="ew")
        tk.Label(frame, text="2", bg="#444", fg="white", padx=5).grid(
            row=current_row, column=1, sticky="ew")
        tk.Label(frame, text="3", bg="#444", fg="white", padx=5).grid(
            row=current_row, column=2, sticky="ew")

    def fill_recipes(self):
        current_row = 0
        frame = self.frame_recipes

        for recipe in self.recipes:
            checkbutton_week1 = RecipeCheckbutton(frame, recipe, 1)
            checkbutton_week2 = RecipeCheckbutton(frame, recipe, 2)
            checkbutton_week3 = RecipeCheckbutton(frame, recipe, 3)
            checkbutton_week1.get().grid(row=current_row, column=0, sticky="w")
            checkbutton_week2.get().grid(row=current_row, column=1, sticky="w")
            checkbutton_week3.get().grid(row=current_row, column=2, sticky="w")
            tk.Label(frame, text=recipe.name, bg="#444", fg="white").grid(
                row=current_row, column=3, sticky="w")
            current_row += 1

    def add_buttons(self):
        frame = self.frame_buttons

        tk.Button(frame,
                  text="Einkaufsliste erstellen",
                  fg="black",
                  relief="raised",
                  padx=3, pady=3,
                  highlightbackground='#444',
                  command=lambda: self.master.controller.display_shopping_lists()
                  ).grid(row=0, columnspan=4)

    def update_scroll_region(self):
        self.canvas_recipes.update_idletasks()
        self.canvas_recipes.config(scrollregion=self.frame_recipes.bbox())


class ShoppingListsFrame(tk.Frame):

    def __init__(self, master, shopping_lists: list):
        """
        :param shopping_lists: A list of ShoppingList objects
        """
        tk.Frame.__init__(self, master, bg="#444", )
        self.master = master
        self.shopping_lists = shopping_lists
        self.canvas_shopping_lists = tk.Canvas(self,
                                               width=300,
                                               height=950,
                                               bg="#444",
                                               scrollregion=(0, 0, 0, 900)
                                               )
        self.frame_shopping_lists = tk.Frame(self.canvas_shopping_lists,
                                             bg="#444")
        self.canvas_shopping_lists.create_window((0, 0),
                                                 width=300,
                                                 window=self.frame_shopping_lists,
                                                 anchor="nw"
                                                 )
        self.vsb = ttk.Scrollbar(self, orient="vertical",
                                 command=self.canvas_shopping_lists.yview)
        self.canvas_shopping_lists.grid(row=0, column=0, sticky="nw")
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.canvas_shopping_lists.config(yscrollcommand=self.vsb.set)

    def add_shopping_list_frames(self):
        current_row = 0

        for shopping_list in self.shopping_lists:
            frame = ShoppingListFrame(self.frame_shopping_lists, shopping_list)
            frame.grid(column=0, row=current_row, sticky="w")
            current_row += 1
            frame.add_ingredients()

    def update_scroll_region(self):
        self.canvas_shopping_lists.update_idletasks()
        self.canvas_shopping_lists.config(
            scrollregion=self.frame_shopping_lists.bbox())


class ShoppingListFrame(tk.Frame):

    def __init__(self, master, shopping_list):
        tk.Frame.__init__(self, master, bg="#444")
        self.master = master
        self.shopping_list = shopping_list

    def add_ingredients(self):
        current_row = 0
        tk.Label(self, text=self.shopping_list.get_name(), bg="#FFF").grid(
            row=current_row, column=0, sticky="nw")
        current_row += 1

        for ingredient in self.shopping_list:
            var = tk.StringVar()
            if ingredient.amount.num > 0.0 and ingredient.amount_piece.num == 0:
                var.set(f"{ingredient.amount} {ingredient.name}")
            elif ingredient.amount.num == 0.0 and ingredient.amount_piece.num >= 0:
                var.set(f"{ingredient.amount_piece} {ingredient.name}")
            else:
                var.set(f"{ingredient.amount} + {ingredient.amount_piece} "
                        f"{ingredient.name}")
            label = tk.Label(self,
                             textvariable=var,
                             state="disabled",
                             bg="#444")
            label.grid(column=0, row=current_row, sticky="nw")
            current_row += 1
