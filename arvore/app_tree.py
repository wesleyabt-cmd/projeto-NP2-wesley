
# app_tree.py — UI travada (não alterar)
import tkinter as tk
from tkinter import messagebox
from tree_logic import Node, navigate_tree

# Árvore de decisão de exemplo (pode ser lida pelo aluno ao abrir o arquivo, mas não precisa alterar)
# Perguntas binárias (sim/não). Folhas carregam a "decisão final".
# Q1: O animal voa?
#   sim -> Q2: É noturno?
#           sim -> "É um mocho/coruja"
#           não -> "É um pardal/pássaro diurno"
#   não -> Q3: Vive na água?
#           sim -> "É um peixe"
#           não -> "É um cão/gato (mamífero terrestre)"
root = Node("O animal voa?",
            yes=Node("É noturno?",
                     yes=Node("É um mocho/coruja"),
                     no=Node("É um pardal/pássaro diurno")),
            no=Node("Vive na água?",
                    yes=Node("É um peixe"),
                    no=Node("É um cão/gato (mamífero terrestre)")))

def parse_answers(s: str):
    # Aceita: "sim, não", "sim nao", "SIM;NAO" etc.
    raw = s.replace(",", " ").replace(";", " ").strip().split()
    ans = []
    for x in raw:
        x = x.strip().lower()
        if x in ("sim", "s"):
            ans.append("sim")
        elif x in ("nao", "não", "n"):
            ans.append("não")
        else:
            # deixa o navigate_tree validar também, mas já avisamos aqui
            ans.append(x)
    return ans

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Árvore de Decisão — Introdução")
        self.geometry("640x420")
        frame = tk.Frame(self); frame.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(frame, text="Responda à sequência de perguntas com 'sim' ou 'não'. Separe por vírgulas ou espaços.").pack(anchor="w")
        self.entry = tk.Entry(frame)
        self.entry.pack(fill="x", pady=6)
        tk.Button(frame, text="Decidir", command=self.on_decide).pack(pady=4)

        self.output = tk.Text(frame, height=10, state="disabled")
        self.output.pack(fill="both", expand=True, pady=6)

        # Mostra o roteiro de perguntas para orientar
        roteiro = (
            "Roteiro:\n"
            "1) O animal voa?\n"
            "   - sim -> 2) É noturno?\n"
            "            - sim -> É um mocho/coruja\n"
            "            - não -> É um pardal/pássaro diurno\n"
            "   - não -> 3) Vive na água?\n"
            "            - sim -> É um peixe\n"
            "            - não -> É um cão/gato (mamífero terrestre)\n"
        )
        self._append(roteiro)

    def _append(self, msg):
        self.output.configure(state="normal")
        self.output.insert("end", msg + "\n")
        self.output.configure(state="disabled")
        self.output.see("end")

    def on_decide(self):
        s = self.entry.get()
        answers = parse_answers(s)
        try:
            decision = navigate_tree(root, answers)
            self._append(f"Respostas: {answers} -> Resultado: {decision}")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    App().mainloop()
