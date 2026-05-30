import tkinter as tk
from tkinter import ttk, messagebox

FORM_BG   = "#FFFFFF"
HEADER_BG = "#1A1A1A"
HEADER_FG = "#FFFFFF"
LABEL_FG  = "#2D2D2D"
INPUT_BG  = "#EBEBEB"
SEP_COLOR = "#E0E0E0"
ACCENT    = "#E8445A"
ACCENT_HV = "#C9314A"
GREEN     = "#2ECC71"

F_BOLD   = ("Helvetica", 10, "bold")
F_HEADER = ("Helvetica", 13, "bold")
F_BODY   = ("Helvetica", 10)
F_SMALL  = ("Helvetica", 8)
F_BTN    = ("Helvetica", 10, "bold")

LABEL_W  = 10
PAD_X    = 48
PAD_Y    = 32
ROW_GAP  = 18


def draw_gradient(canvas, w, h):
    l, r = (91, 108, 240), (180, 79, 232)
    steps = 80
    for i in range(steps):
        rgb = tuple(int(l[c] + (r[c] - l[c]) * i / steps) for c in range(3))
        color = "#{:02x}{:02x}{:02x}".format(*rgb)
        canvas.create_rectangle(int(w*i/steps), 0, int(w*(i+1)/steps), h, fill=color, outline="")


def entry(parent, w=30):
    return tk.Entry(
        parent, font=F_BODY, bg=INPUT_BG, fg=LABEL_FG,
        relief="flat", bd=0, width=w,
        insertbackground=LABEL_FG, highlightthickness=0,
    )


def sublabel(parent, text):
    return tk.Label(parent, text=text, font=F_SMALL, bg=FORM_BG, fg="#AAAAAA", anchor="w")


def sep(parent):
    tk.Frame(parent, bg=SEP_COLOR, height=1).grid(
        row=sep.row, column=0, columnspan=2, sticky="ew", pady=(0, ROW_GAP)
    )
    sep.row += 1
sep.row = 0


def label_cell(parent, text, row):
    tk.Label(
        parent, text=text, font=F_BOLD, bg=FORM_BG, fg=LABEL_FG, anchor="w",
        width=11,
    ).grid(row=row, column=0, sticky="nw", padx=(0, 12), pady=(8, 0))


def run():
    root = tk.Tk()
    root.title("Event Registration")
    root.resizable(False, False)
    W, H = 820, 650
    root.geometry(f"{W}x{H}")

    bg = tk.Canvas(root, width=W, height=H, highlightthickness=0)
    bg.place(x=0, y=0)
    draw_gradient(bg, W, H)

    outer = tk.Frame(root, bg=FORM_BG)
    outer.place(relx=0.5, rely=0.5, anchor="center", width=530)

    tk.Label(outer, text="EVENT REGISTRATION FORM", font=F_HEADER,
             bg=HEADER_BG, fg=HEADER_FG, pady=18).pack(fill="x")

    body = tk.Frame(outer, bg=FORM_BG, padx=PAD_X, pady=PAD_Y)
    body.pack(fill="both")
    body.columnconfigure(1, weight=1)

    fields = {}
    r = 0

    label_cell(body, "Name", r)
    name_col = tk.Frame(body, bg=FORM_BG)
    name_col.grid(row=r, column=1, sticky="ew", pady=(0, 6))
    name_col.columnconfigure(0, weight=1)
    name_col.columnconfigure(1, weight=1)

    for col, key, sub in [(0, "first_name", "First Name"), (1, "last_name", "Last Name")]:
        f = tk.Frame(name_col, bg=FORM_BG)
        f.grid(row=0, column=col, sticky="ew", padx=(0, 8) if col == 0 else (0, 0))
        e = entry(f, 16)
        e.pack(fill="x", ipady=7)
        sublabel(f, sub).pack(anchor="w", pady=(2, 0))
        fields[key] = e
    r += 1

    tk.Frame(body, bg=SEP_COLOR, height=1).grid(row=r, column=0, columnspan=2, sticky="ew", pady=(0, ROW_GAP))
    r += 1

    label_cell(body, "Company", r)
    cf = tk.Frame(body, bg=FORM_BG)
    cf.grid(row=r, column=1, sticky="ew", pady=(0, 6))
    e = entry(cf, 40)
    e.pack(fill="x", ipady=7)
    fields["company"] = e
    r += 1

    tk.Frame(body, bg=SEP_COLOR, height=1).grid(row=r, column=0, columnspan=2, sticky="ew", pady=(0, ROW_GAP))
    r += 1

    label_cell(body, "Email", r)
    ef = tk.Frame(body, bg=FORM_BG)
    ef.grid(row=r, column=1, sticky="ew", pady=(0, 6))
    e = entry(ef, 40)
    e.pack(fill="x", ipady=7)
    fields["email"] = e
    r += 1

    tk.Frame(body, bg=SEP_COLOR, height=1).grid(row=r, column=0, columnspan=2, sticky="ew", pady=(0, ROW_GAP))
    r += 1

    label_cell(body, "Phone", r)
    phone_col = tk.Frame(body, bg=FORM_BG)
    phone_col.grid(row=r, column=1, sticky="ew", pady=(0, 6))

    af = tk.Frame(phone_col, bg=FORM_BG)
    af.pack(side="left", padx=(0, 10))
    ea = entry(af, 7)
    ea.insert(0, "+7")
    ea.pack(fill="x", ipady=7)
    sublabel(af, "Area Code").pack(anchor="w", pady=(2, 0))
    fields["area_code"] = ea

    pf = tk.Frame(phone_col, bg=FORM_BG)
    pf.pack(side="left", fill="x", expand=True)
    ep = entry(pf, 28)
    ep.pack(fill="x", ipady=7)
    sublabel(pf, "Phone Number").pack(anchor="w", pady=(2, 0))
    fields["phone_number"] = ep
    r += 1

    tk.Frame(body, bg=SEP_COLOR, height=1).grid(row=r, column=0, columnspan=2, sticky="ew", pady=(0, ROW_GAP))
    r += 1

    label_cell(body, "Subject", r)
    sf = tk.Frame(body, bg=FORM_BG)
    sf.grid(row=r, column=1, sticky="ew", pady=(0, 6))

    subject_var = tk.StringVar(value="Choose option")
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("F.TCombobox",
        fieldbackground=INPUT_BG, background=INPUT_BG,
        foreground=LABEL_FG, bordercolor=SEP_COLOR,
        arrowcolor="#555", relief="flat", padding=7,
    )
    ttk.Combobox(
        sf, textvariable=subject_var,
        values=["Workshop", "Conference", "Seminar", "Networking Event", "Hackathon"],
        state="readonly", font=F_BODY, style="F.TCombobox",
    ).pack(fill="x")
    r += 1

    tk.Frame(body, bg=SEP_COLOR, height=1).grid(row=r, column=0, columnspan=2, sticky="ew", pady=(0, ROW_GAP))
    r += 1

    sec = tk.Frame(body, bg=FORM_BG)
    sec.grid(row=r, column=0, columnspan=2, sticky="w", pady=(0, ROW_GAP))

    tk.Label(sec, text="Are you an existing customer?",
             font=F_BODY, bg=FORM_BG, fg=LABEL_FG).pack(anchor="w", pady=(0, 8))

    radio_row = tk.Frame(sec, bg=FORM_BG)
    radio_row.pack(anchor="w")

    customer_var = tk.StringVar(value="Yes")
    canvases = {}

    def draw_radio(c, sel):
        c.delete("all")
        c.create_oval(1, 1, 15, 15, outline="#CCCCCC", width=2, fill="white")
        if sel:
            c.create_oval(4, 4, 12, 12, fill=GREEN, outline=GREEN)

    def make_sel(val):
        def select():
            customer_var.set(val)
            list(map(lambda kv: draw_radio(kv[1], kv[0] == val), canvases.items()))
        return select

    for val in ["Yes", "No"]:
        rf = tk.Frame(radio_row, bg=FORM_BG)
        rf.pack(side="left", padx=(0, 24))
        c = tk.Canvas(rf, width=16, height=16, bg=FORM_BG, highlightthickness=0)
        c.pack(side="left", padx=(0, 5))
        canvases[val] = c
        lbl = tk.Label(rf, text=val, font=F_BODY, bg=FORM_BG, fg=LABEL_FG)
        lbl.pack(side="left")
        sel = make_sel(val)
        c.bind("<Button-1>", lambda e, s=sel: s())
        lbl.bind("<Button-1>", lambda e, s=sel: s())
        rf.bind("<Button-1>", lambda e, s=sel: s())

    list(map(lambda kv: draw_radio(kv[1], kv[0] == "Yes"), canvases.items()))
    r += 1

    bf = tk.Frame(body, bg=FORM_BG)
    bf.grid(row=r, column=0, columnspan=2, sticky="w")

    def on_register():
        lines = [f"{k.replace('_',' ').title()}: {fields[k].get()}" for k in fields]
        lines += [f"Subject: {subject_var.get()}", f"Existing Customer: {customer_var.get()}"]
        messagebox.showinfo("Registered!", "\n".join(lines))

    btn = tk.Button(
        bf, text="REGISTER", font=F_BTN,
        bg=ACCENT, fg="white", relief="flat", bd=0,
        padx=30, pady=12, cursor="hand2",
        command=on_register,
        activebackground=ACCENT_HV, activeforeground="white",
    )
    btn.pack()
    btn.bind("<Enter>", lambda e: btn.config(bg=ACCENT_HV))
    btn.bind("<Leave>", lambda e: btn.config(bg=ACCENT))

    root.mainloop()


run()

