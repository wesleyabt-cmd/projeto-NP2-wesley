
# app_graph.py — UI travada (não alterar)
import tkinter as tk
from tkinter import messagebox
from math import cos, sin, pi
from graph_logic import connected


# Grafo simples de amizades (não direcionado) em lista de adjacência
GRAPH = {
    # Grupo 1
    "Ana": ["Beto", "Carlos"],
    "Beto": ["Ana", "Duda"],
    "Carlos": ["Ana", "Eva"],
    "Duda": ["Beto", "Felipe"],
    "Eva": ["Carlos"],
    "Felipe": ["Duda"],

    # Grupo 2 — sem conexões com o grupo 1
    "Gustavo": ["Helena", "Igor"],
    "Helena": ["Gustavo", "Igor"],
    "Igor": ["Helena"],

    # Grupo 3 — nó isolado
    "Julia": []
}


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Grafo de Contatos — Introdução")
        self.geometry("760x560")

        top = tk.Frame(self); top.pack(fill="x", padx=10, pady=10)
        tk.Label(top, text="Pessoa A:").grid(row=0, column=0, sticky="e", padx=4)
        tk.Label(top, text="Pessoa B:").grid(row=1, column=0, sticky="e", padx=4)
        self.a_entry = tk.Entry(top, width=20); self.a_entry.grid(row=0, column=1, padx=4)
        self.b_entry = tk.Entry(top, width=20); self.b_entry.grid(row=1, column=1, padx=4)
        tk.Button(top, text="Conectados?", command=self.on_check).grid(row=0, column=2, rowspan=2, padx=8)

        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill="both", expand=True, padx=10, pady=10)

        self.draw_graph(GRAPH)

    def on_check(self):
        a = self.a_entry.get().strip()
        b = self.b_entry.get().strip()
        try:
            ok = connected(GRAPH, a, b)
            if ok:
                messagebox.showinfo("Resultado", f"{a} e {b} estão conectados por algum caminho.")
            else:
                messagebox.showinfo("Resultado", f"{a} e {b} NÃO estão conectados.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def draw_graph(self, graph):
        self.canvas.delete("all")
        nodes = list(graph.keys())
        n = max(1, len(nodes))
        W = self.canvas.winfo_width() or 720
        H = self.canvas.winfo_height() or 460
        cx, cy, r = W/2, H/2, min(W,H)*0.35

        pos = {}
        for i, name in enumerate(nodes):
            ang = (2*pi*i)/n
            x = cx + r*cos(ang)
            y = cy + r*sin(ang)
            pos[name] = (x, y)

        # arestas
        for u, neigh in graph.items():
            for v in neigh:
                if v in pos:
                    x1,y1 = pos[u]; x2,y2 = pos[v]
                    self.canvas.create_line(x1,y1,x2,y2)

        # nós
        R = 18
        for name, (x,y) in pos.items():
            self.canvas.create_oval(x-R, y-R, x+R, y+R, fill="#eef5ff", outline="#335")
            self.canvas.create_text(x, y, text=name)

if __name__ == "__main__":
    App().mainloop()
