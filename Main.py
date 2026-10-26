
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json

class EstudeComAlessa:
    def __init__(self, root):
        self.root = root
        root.title("Estude com Alessa - Todo mérito é de Deus")
        root.geometry("900x650")
        root.minsize(800, 600)

        # Estilo acessível
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=8)
        style.configure("TLabel", font=("Arial", 12))

        # Título
        topo = tk.Frame(root, bg="#6A1B9A", height=70)
        topo.pack(fill="x")
        tk.Label(topo, text="Estude com Alessa", fg="white", bg="#6A1B9A", font=("Arial", 20, "bold")).pack(pady=5)
        tk.Label(topo, text="Pacote de escritório acessível, brasileiro e com propósito", fg="#E1BEE7", bg="#6A1B9A", font=("Arial", 11)).pack()

        # Abas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.criar_aba_texto()
        self.criar_aba_planilha()
        self.criar_aba_slides()

        # Rodapé
        rodape = tk.Label(root, text="Todo mérito é de Deus - Criado por Alessandra com Alessa TTS | Deus segura minhas mãos", 
                         bg="#F3E5F5", fg="#4A148C", font=("Arial", 9), pady=6)
        rodape.pack(fill="x", side="bottom")

    def criar_aba_texto(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="  📝 Editor de Texto  ")

        barra = ttk.Frame(frame)
        barra.pack(fill="x", pady=5)
        ttk.Button(barra, text="Negrito (Ctrl+B)", command=self.toggle_negrito).pack(side="left", padx=5)
        ttk.Button(barra, text="Salvar (Ctrl+S)", command=self.salvar_texto).pack(side="left", padx=5)
        ttk.Button(barra, text="Ler com Alessa TTS", command=lambda: messagebox.showinfo("Alessa TTS", "Aqui vai integrar com a voz da Jaíne/Caleb/Ingrid!")).pack(side="left", padx=5)

        self.texto = tk.Text(frame, font=("Arial", 14), wrap="word", undo=True, padx=10, pady=10)
        self.texto.pack(fill="both", expand=True, padx=5, pady=5)
        self.texto.insert("1.0", "Digite seu texto aqui... Deus te capacita para escrever!\n\nDica: Use Tab para navegar e o NVDA vai ler tudo.")
        # Acessibilidade
        self.texto.focus_set()

    def criar_aba_planilha(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="  📊 Planilha  ")

        topo = ttk.Frame(frame)
        topo.pack(fill="x", pady=5)
        ttk.Label(topo, text="Célula:").pack(side="left", padx=5)
        self.cell_entry = ttk.Entry(topo, width=10)
        self.cell_entry.insert(0, "A1")
        self.cell_entry.pack(side="left")
        ttk.Label(topo, text="Conteúdo / Fórmula (ex: =SOMA(B2:B3)):").pack(side="left", padx=10)
        self.formula_entry = ttk.Entry(topo, width=35)
        self.formula_entry.pack(side="left", padx=5)
        ttk.Button(topo, text="Aplicar").pack(side="left", padx=5)

        # Grade simples 10x6 para começar
        grade_frame = ttk.Frame(frame)
        grade_frame.pack(fill="both", expand=True)

        cols = ["", "A", "B", "C", "D", "E", "F"]
        for c, nome in enumerate(cols):
            ttk.Label(grade_frame, text=nome, font=("Arial", 11, "bold"), width=12, borderwidth=1, relief="solid").grid(row=0, column=c, sticky="nsew")

        self.celulas = {}
        for l in range(1, 11):
            ttk.Label(grade_frame, text=str(l), font=("Arial", 11, "bold"), width=4, borderwidth=1, relief="solid").grid(row=l, column=0, sticky="nsew")
            for c in range(1, 7):
                nome = f"{chr(64+c)}{l}"
                e = ttk.Entry(grade_frame, width=12, font=("Arial", 11))
                e.grid(row=l, column=c, sticky="nsew", padx=1, pady=1)
                e.bind("<FocusIn>", lambda ev, n=nome: self.cell_entry.delete(0, tk.END) or self.cell_entry.insert(0, n))
                self.celulas[nome] = e

        ttk.Label(frame, text="Dica NVDA: Use Tab para navegar entre células. Cada célula fala seu endereço, ex: B2. Digite números ou =SOMA").pack(pady=5)

    def criar_aba_slides(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="  🎤 Slides  ")

        paned = ttk.PanedWindow(frame, orient="horizontal")
        paned.pack(fill="both", expand=True)

        left = ttk.Frame(paned)
        paned.add(left, weight=1)
        ttk.Label(left, text="Lista de Slides", font=("Arial", 12, "bold")).pack(pady=5)
        self.lista_slides = tk.Listbox(left, font=("Arial", 12), height=15)
        self.lista_slides.pack(fill="both", expand=True, padx=5)
        for i in range(1, 4):
            self.lista_slides.insert("end", f"Slide {i} - Clique para editar")
        ttk.Button(left, text="+ Novo Slide", command=self.novo_slide).pack(pady=10, fill="x", padx=10)

        right = ttk.Frame(paned)
        paned.add(right, weight=3)
        ttk.Label(right, text="Conteúdo do Slide Atual", font=("Arial", 12, "bold")).pack(pady=5)
        self.slide_text = tk.Text(right, font=("Arial", 16), wrap="word", padx=15, pady=15)
        self.slide_text.pack(fill="both", expand=True, padx=10, pady=10)
        self.slide_text.insert("1.0", "Título do Slide\n\nDigite aqui seu conteúdo. Simples, sem caixas invisíveis. O NVDA lê tudo!")

    def toggle_negrito(self):
        messagebox.showinfo("Negrito", "Negrito ativado! (Na versão completa vai mudar a formatação e o NVDA vai falar 'negrito')")

    def salvar_texto(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Texto", "*.txt")])
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.texto.get("1.0", tk.END))
            messagebox.showinfo("Salvo", f"Salvo em {path} - Glória a Deus!")

    def novo_slide(self):
        n = self.lista_slides.size()+1
        self.lista_slides.insert("end", f"Slide {n} - Novo")

if __name__ == "__main__":
    root = tk.Tk()
    app = EstudeComAlessa(root)
    root.mainloop()
