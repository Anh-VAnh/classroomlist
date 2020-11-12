import os
# creating .tex file from with python
import sys

def import_student_data(filename):
    """This function will import student data from a csv file(classlist.dat)"""
    print(f"Importing student data from file '{filename}'")
    datafile = open(filename,'r')
    lines = datafile.readlines()
    for line in lines:
        print(line)
        student_id, student_name, student_date_of_birtj, student_training_program
        
#    print(lines)
program = line.split(',')
    student_name = student_name.strip()
    student_date_of_birth = student_date of birt.strip()
    student_training_program = student_training_program.strip()
    datafile.close()
    return

script = sys.argv
textfilename = "newclasslist.tex"
fout = open(textfilename,"w")
content = r"""\documentclass[12pt,a4paper]{book}
\usepackage[utf8]{vietnam}
\usepackage[left=0.2cm, right=1cm, top=1cm, bottom=2.00cm]{geometry} %%Set border
\newcommand\tab[1][1cm]{\hspace*{#1}} %% Creat tab
\setlength{\parindent}{0pt}
\usepackage{scrextend}
\changefontsizes{8pt}
\usepackage{setspace} %% Paragraph 2
\usepackage{xhfill} %% Dong ngang
\usepackage{array} 
\usepackage{multirow} %% Merge
\usepackage{booktabs} %%Change width line in table
\usepackage{blindtext}
\begin{document}
\centerline{\textbf{%s %s}}
\pagenumbering{gobble} %% No number this page
\newcommand{\xfill}[2][1ex]{{
		\dimen0=#2\advance\dimen0 by #1
		\leaders\hrule height \dimen0 depth -#1\hfill
}}
\textbf{Học phần: Nhập môn Internet kết nối vạn vật}\tab[3cm]Lớp HP: \textbf{PHY1070 3}\tab[2cm]Số tín chỉ: 2\\
Thứ: 4\tab[9.1cm]Tiết: 9 - 11\tab[3.45cm]Giảng đường: 201T5\\
\begin{tabular}{ m{0.7cm} | m{2cm}| m{4cm} | m{2cm} | m{2.5cm} | m{1.2cm} | m{1.5cm} | m{1cm} | m{1.6cm} | }
		\toprule[0.4mm]
		\begin{center}\textbf{STT }\end{center}&\begin{center}\textbf{Mã SV}\end{center} &\begin{center}\textbf{Họ và tên}\end{center} &\begin{center} \textbf{Ngày sinh}\end{center} &\begin{center} \textbf{Lớp}\end{center} &\vspace{-0.2cm}\begin{center} \textbf{Thường\vspace{-0.2cm}\\xuyên\vspace{-0.2cm}\\(...\%%)\vspace{-0.6cm} }\end{center} & \begin{center} \textbf{Ký nộp }\end{center}&\vspace{-0.2cm}\begin{center} \textbf{Giữa\vspace{-0.2cm}\\kỳ\vspace{-0.2cm}\\(...\%%)\vspace{-0.6cm} }\end{center} &\begin{center} \textbf{Ghi chú}\vspace{-0cm}\end{center}\\
		\hline
		1 & 12345678 & Nguyễn Y Vân & 21/10/1997 & 28CLCMTTT & 1 & $ \gamma\upsilon $ & 2 & MẤT TÍCH\\
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 & note1\\
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 & note1\\
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 & note1\\
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 & note1\\
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 & note1\\
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 &
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 & note1\\
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 & note1\\
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 & note1\\
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 & note1\\
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 & note1\\
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 & note1\\
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 & note1\\
		\hline
		stt1 & mssv1 & name1 & birth1 & class1 & often1 & sign1 & mid1 & note1\\
		\bottomrule[0.4mm]
\end{tabular}
\end{document}
""" %(semester, academic_year)
fout.write(content)
fout.close()
# creating .pdf file from .tex file with xelatex
cmd = f"pdflatex {textfilename}"
failure = os.system(cmd)
if failure:
    print(f'Creating {textfilename} failure!!!')
else:
    print(f'Creating {textfilename} successfully!!!')

pdffilename = textfilename[:-3]+'pdf'
print(pdffilename)
# Viewing classlist.pdf
cmd = f"evince {pdffilename} &"
failure = os.system(cmd)
if failure:
    print(f'Viewing {pdffilename} failed!!!')
else:
    print(f'Viewing {pdffilename} successfully!!!')
print(sys.argv)
print("Chuong trinh la %s abcd %s cdf %s"%(script, semester, academic_year))

filename = 'classlist.dat'
import_student_data(filename)
