from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import pandas as pd
import logging

logging.basicConfig(filename="actions.log", level=logging.INFO)

logging.info('GUI initiated @ {0}.'.format(datetime.now()))

window = Tk()
window.title("Sourceographer")
window.geometry('650x600')
window.configure(background = "white")

effectiveness = Label(window ,text = "Effectiveness").grid(row = 0,column = 0)
effectiveness_text = Entry(window)
effectiveness_text.grid(row = 0, column = 1)

testing = Label(window ,text = "Testing process").grid(row = 1,column = 0)
testing_var = IntVar()
testing_R1 = Radiobutton(window, text="True", variable=testing_var, value=1).grid(row = 1, column = 1)
testing_R2 = Radiobutton(window, text="False", variable=testing_var, value=0).grid(row = 1, column = 2)

coverage = Label(window ,text = "Coverage").grid(row = 2,column = 0)
coverage_text = Entry(window)
coverage_text.grid(row = 2, column = 1)

licensing = Label(window ,text = "Licensing").grid(row = 3,column = 0)
licensing_var = IntVar()
licensing_R1 = Radiobutton(window, text="1", variable=licensing_var, value=1).grid(row = 3, column = 1)
licensing_R2 = Radiobutton(window, text="2", variable=licensing_var, value=2).grid(row = 3, column = 2)
licensing_R3 = Radiobutton(window, text="3", variable=licensing_var, value=3).grid(row = 3, column = 3)
licensing_R4 = Radiobutton(window, text="4", variable=licensing_var, value=4).grid(row = 3, column = 4)
licensing_R5 = Radiobutton(window, text="5", variable=licensing_var, value=5).grid(row = 3, column = 5)

dual_licensing = Label(window ,text = "Dual licensing").grid(row = 4,column = 0)
dual_var = IntVar()
dual_R1 = Radiobutton(window, text="True", variable=dual_var, value=1).grid(row = 4, column = 1)
dual_R2 = Radiobutton(window, text="False", variable=dual_var, value=0).grid(row = 4, column = 2)

comm_res = Label(window ,text = "Commercial resources").grid(row = 5,column = 0)
res_var = IntVar()
res_R1 = Radiobutton(window, text="True", variable=res_var, value=1).grid(row = 5, column = 1)
res_R2 = Radiobutton(window, text="False", variable=res_var, value=0).grid(row = 5, column = 2)

comm_training = Label(window ,text = "Commercial training").grid(row = 6,column = 0)
training_var = IntVar()
training_R1 = Radiobutton(window, text="True", variable=training_var, value=1).grid(row = 6, column = 1)
training_R2 = Radiobutton(window, text="False", variable=training_var, value=0).grid(row = 6, column = 2)

industry_adoption = Label(window ,text = "Industry adoption").grid(row = 7,column = 0)
adoption_var = IntVar()
adoption_R1 = Radiobutton(window, text="True", variable=adoption_var, value=1).grid(row = 7, column = 1)
adoption_R2 = Radiobutton(window, text="False", variable=adoption_var, value=0).grid(row = 7, column = 2)

non_profit = Label(window ,text = "Non profit support").grid(row = 8,column = 0)
non_var = IntVar()
non_R1 = Radiobutton(window, text="True", variable=non_var, value=1).grid(row = 8, column = 1)
non_R2 = Radiobutton(window, text="False", variable=non_var, value=0).grid(row = 8, column = 2)

for_profit = Label(window ,text = "For profit support").grid(row = 9,column = 0)
for_var = IntVar()
for_R1 = Radiobutton(window, text="True", variable=for_var, value=1).grid(row = 9, column = 1)
for_R2 = Radiobutton(window, text="False", variable=for_var, value=0).grid(row = 9, column = 2)

donations = Label(window ,text = "Donations").grid(row = 10,column = 0)
donations_var = IntVar()
donations_R1 = Radiobutton(window, text="True", variable=donations_var, value=1).grid(row = 10, column = 1)
donations_R2 = Radiobutton(window, text="False", variable=donations_var, value=0).grid(row = 10, column = 2)

governance = Label(window ,text = "Governance Model").grid(row = 11,column = 0)
gov_var = IntVar()
gov_R1 = Radiobutton(window, text="True", variable=gov_var, value=1).grid(row = 11, column = 1)
gov_R2 = Radiobutton(window, text="False", variable=gov_var, value=0).grid(row = 11, column = 2)

roadmap = Label(window ,text = "Project Road-map").grid(row = 12,column = 0)
roadmap_var = IntVar()
roadmap_R1 = Radiobutton(window, text="True", variable=roadmap_var, value=1).grid(row = 12, column = 1)
roadmap_R2 = Radiobutton(window, text="False", variable=roadmap_var, value=0).grid(row = 12, column = 2)

coc = Label(window ,text = "Code of Conduct").grid(row = 13,column = 0)
coc_var = IntVar()
coc_R1 = Radiobutton(window, text="True", variable=coc_var, value=1).grid(row = 13, column = 1)
coc_R2 = Radiobutton(window, text="False", variable=coc_var, value=0).grid(row = 13, column = 2)

coding_standards = Label(window ,text = "Coding standards").grid(row = 14,column = 0)
coding_var = IntVar()
coding_R1 = Radiobutton(window, text="True", variable=coding_var, value=1).grid(row = 14, column = 1)
coding_R2 = Radiobutton(window, text="False", variable=coding_var, value=0).grid(row = 14, column = 2)

documentation_standards = Label(window ,text = "Documentation standards").grid(row = 15,column = 0)
doc_var = IntVar()
doc_R1 = Radiobutton(window, text="True", variable=doc_var, value=1).grid(row = 15, column = 1)
doc_R2 = Radiobutton(window, text="False", variable=doc_var, value=0).grid(row = 15, column = 2)

localization = Label(window ,text = "Localization process").grid(row = 16,column = 0)
loc_var = IntVar()
loc_R1 = Radiobutton(window, text="True", variable=loc_var, value=1).grid(row = 16, column = 1)
loc_R2 = Radiobutton(window, text="False", variable=loc_var, value=0).grid(row = 16, column = 2)

user_guide = Label(window ,text = "User guide").grid(row = 17,column = 0)
guide_var = IntVar()
guide_R1 = Radiobutton(window, text="1", variable=guide_var, value=1).grid(row = 17, column = 1)
guide_R2 = Radiobutton(window, text="2", variable=guide_var, value=2).grid(row = 17, column = 2)
guide_R3 = Radiobutton(window, text="3", variable=guide_var, value=3).grid(row = 17, column = 3)
guide_R4 = Radiobutton(window, text="4", variable=guide_var, value=4).grid(row = 17, column = 4)
guide_R5 = Radiobutton(window, text="5", variable=guide_var, value=5).grid(row = 17, column = 5)

repo_author = Label(window ,text = "Repository name in author/repo format").grid(row = 18,column = 0)
repo_author_text = Entry(window)
repo_author_text.grid(row = 18, column = 1)

tag = Label(window ,text = "Version (repo specific tag name)").grid(row = 19,column = 0)
tag_text = Entry(window)
tag_text.grid(row = 19, column = 1)

url = Label(window ,text = "Repository URL").grid(row = 20,column = 0)
url_text = Entry(window)
url_text.grid(row = 20, column = 1)

start_d = Label(window ,text = "Version starting date (YYYY-MM-DD)").grid(row = 21,column = 0)
start_d_text = Entry(window)
start_d_text.grid(row = 21, column = 1)

end_d = Label(window ,text = "Version ending date (YYYY-MM-DD)").grid(row = 22,column = 0)
end_d_text = Entry(window)
end_d_text.grid(row = 22, column = 1)

def submit():
    df = pd.read_csv('input_metrics.csv', delimiter = ',')
    
    df['Effectiveness'] = df['Effectiveness'].fillna(effectiveness_text.get())
    df['Testing'] = df['Testing'].fillna(testing_var.get())
    df['Coverage'] = df['Coverage'].fillna(coverage_text.get())
    df['Licensing'] = df['Licensing'].fillna(licensing_var.get())
    df['Dual licensing model'] = df['Dual licensing model'].fillna(dual_var.get())
    df['Commercial resources'] = df['Commercial resources'].fillna(res_var.get())
    df['Commercial training'] = df['Commercial training'].fillna(training_var.get())
    df['Industry adoption'] = df['Industry adoption'].fillna(adoption_var.get())
    df['Non profit / Foundation attached'] = df['Non profit / Foundation attached'].fillna(non_var.get())
    df['For profit company attached'] = df['For profit company attached'].fillna(for_var.get())
    df['Donations'] = df['Donations'].fillna(donations_var.get())
    df['Governance model'] = df['Governance model'].fillna(gov_var.get())
    df['Project road-map'] = df['Project road-map'].fillna(roadmap_var.get())
    df['Code of conduct'] = df['Code of conduct'].fillna(coc_var.get())
    df['Coding standards'] = df['Coding standards'].fillna(coding_var.get())
    df['Documentation standards'] = df['Documentation standards'].fillna(doc_var.get())
    df['Localization Process'] = df['Localization Process'].fillna(loc_var.get())
    df['User guide'] = df['User guide'].fillna(guide_var.get())
    df['s_date'] = df['s_date'].fillna(start_d_text.get())
    df['e_date'] = df['e_date'].fillna(end_d_text.get())
    df['repo_author'] = df['repo_author'].fillna(repo_author_text.get())
    df['url'] = df['url'].fillna(url_text.get())
    df['tag'] = df['tag'].fillna(tag_text.get())
    df.to_csv('input_metrics.csv', index=False)

    messagebox.showinfo('Message', 'Metrics submitted. Exiting to continue.')
    logging.info('GUI exit @ {0}.'.format(datetime.now()))
    window.destroy()
    

btn = ttk.Button(window ,text="Submit", command=submit).grid(row=23,column=2)
window.mainloop()

