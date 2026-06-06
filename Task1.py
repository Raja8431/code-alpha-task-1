from tkinter import *
from tkinter import messagebox
from sklearn.linear_model import LogisticRegression
import numpy as np

training_data = np.array([
    [50000, 10000, 1],
    [60000, 15000, 1],
    [25000, 20000, 0],
    [30000, 25000, 0],
    [80000, 10000, 1],
    [20000, 30000, 0],
    [90000, 5000, 1],
    [40000, 15000, 1]
])

labels = np.array([1, 1, 0, 0, 1, 0, 1, 1])

model = LogisticRegression()
model.fit(training_data, labels)

root = Tk()
root.title("AI Credit Scoring System")
root.geometry("950x700")
root.config(bg="#0f172a")

def predict_credit():

    try:

        income = int(income_entry.get())
        loan = int(loan_entry.get())
        history = int(history_entry.get())

        prediction = model.predict([
            [income, loan, history]
        ])

        if prediction[0] == 1:

            result_label.config(
                text="GOOD CREDIT SCORE ✅",
                fg="#22c55e"
            )

            status_label.config(
                text="Loan Approval Chance: HIGH",
                fg="#38bdf8"
            )

        else:

            result_label.config(
                text="BAD CREDIT SCORE ❌",
                fg="#ef4444"
            )

            status_label.config(
                text="Loan Approval Chance: LOW",
                fg="#f97316"
            )

    except:

        messagebox.showerror(
            "Error",
            "Please enter valid numeric values!"
        )

top_frame = Frame(
    root,
    bg="#111827",
    height=100
)

top_frame.pack(fill="x")

Label(
    top_frame,
    text="AI CREDIT SCORING MODEL",
    font=("Arial", 30, "bold"),
    bg="#111827",
    fg="#38bdf8"
).pack(pady=25)

main_frame = Frame(
    root,
    bg="#1e293b",
    bd=0
)

main_frame.pack(
    pady=40,
    ipadx=40,
    ipady=30
)
Label(
    main_frame,
    text="Enter Customer Financial Details",
    font=("Arial", 20, "bold"),
    bg="#1e293b",
    fg="white"
).grid(
    row=0,
    column=0,
    columnspan=2,
    pady=20
)


Label(
    main_frame,
    text="Monthly Income",
    font=("Arial", 15, "bold"),
    bg="#1e293b",
    fg="#cbd5e1"
).grid(
    row=1,
    column=0,
    padx=20,
    pady=15,
    sticky="w"
)

income_entry = Entry(
    main_frame,
    font=("Arial", 15),
    width=28,
    bg="#334155",
    fg="white",
    insertbackground="white",
    relief=FLAT
)

income_entry.grid(
    row=1,
    column=1,
    pady=15
)

Label(
    main_frame,
    text="Loan Amount",
    font=("Arial", 15, "bold"),
    bg="#1e293b",
    fg="#cbd5e1"
).grid(
    row=2,
    column=0,
    padx=20,
    pady=15,
    sticky="w"
)

loan_entry = Entry(
    main_frame,
    font=("Arial", 15),
    width=28,
    bg="#334155",
    fg="white",
    insertbackground="white",
    relief=FLAT
)

loan_entry.grid(
    row=2,
    column=1,
    pady=15
)

Label(
    main_frame,
    text="Credit History (1 = Good, 0 = Bad)",
    font=("Arial", 15, "bold"),
    bg="#1e293b",
    fg="#cbd5e1"
).grid(
    row=3,
    column=0,
    padx=20,
    pady=15,
    sticky="w"
)

history_entry = Entry(
    main_frame,
    font=("Arial", 15),
    width=28,
    bg="#334155",
    fg="white",
    insertbackground="white",
    relief=FLAT
)

history_entry.grid(
    row=3,
    column=1,
    pady=15
)

Button(
    root,
    text="CHECK CREDIT SCORE",
    command=predict_credit,
    font=("Arial", 16, "bold"),
    bg="#06b6d4",
    fg="black",
    padx=25,
    pady=12,
    bd=0,
    cursor="hand2",
    activebackground="#0891b2"
).pack(pady=20)

result_label = Label(
    root,
    text="",
    font=("Arial", 28, "bold"),
    bg="#0f172a"
)

result_label.pack(pady=15)

status_label = Label(
    root,
    text="",
    font=("Arial", 18, "bold"),
    bg="#0f172a"
)

status_label.pack(pady=10)

footer = Label(
    root,
    text="Developed Using Python, Tkinter & Machine Learning",
    font=("Arial", 12),
    bg="#0f172a",
    fg="#94a3b8"
)

footer.pack(side=BOTTOM, pady=15)
root.mainloop()