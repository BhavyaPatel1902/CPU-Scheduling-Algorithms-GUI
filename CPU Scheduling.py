from tkinter import *
import sys
import os

clear_widget=[]
def algo_FCFS(burst_time,arrival_time):
    n = len(burst_time)
    processes = list(range(1, n+1))
    wt = FCFS_findWaitingTime(processes, n, burst_time, arrival_time)
    tat = FCFS_findTurnAroundTime(processes, n, burst_time, wt)
    compl_time = FCFS_findavgTime(processes, n, burst_time, arrival_time, wt, tat)
    show(wt, tat, compl_time,n)


def FCFS_findWaitingTime(processes, n, bt, at):
    service_time = [0] * n
    service_time[0] = at[0]
    wt = [0] * n
    wt[0] = 0
    for i in range(1, n):
        service_time[i] = (service_time[i - 1] +
                           bt[i - 1])
        wt[i] = service_time[i] - at[i]
        if (wt[i] < 0):
            wt[i] = 0

    return wt


def FCFS_findTurnAroundTime(processes, n, bt, wt):
    tat = [0] * n
    for i in range(n):
        tat[i] = bt[i] + wt[i]
    return tat


def FCFS_findavgTime(processes, n, bt, at, wt, tat):
    total_wt = 0
    total_tat = 0
    compl_time = [0] * n
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time[i] = tat[i] + at[i]
    Avg_Turn_around_Time = Label(text="Average turn around time  " + ": " + str((total_tat / n)),bg="light green")

    Avg_Turn_around_Time.place(x=20, y=120+(n+1)*20)
    Avg_Waiting_time = Label(text="Average waiting time " + ": " + str((total_wt / n)),bg="light green")
    Avg_Waiting_time.place(x=20, y=200+(n+1)*20)
    clear_widget.append(Avg_Turn_around_Time)
    clear_widget.append(Avg_Waiting_time)

    return compl_time


def algo_SRTF(burst_time,arrival_time):
    n = len(burst_time)
    processes = list(range(1, n+1))
    wt = SRTF_findWaitingTime(arrival_time, burst_time, n)
    tat = SRTF_findTurnAroundTime(burst_time,arrival_time, n, wt)
    compl_time = SRTF_findavgTime(wt, tat, arrival_time, n)
    show(wt, tat, compl_time,n)


def SRTF_findWaitingTime(arrival_time, burst_time, n):
    rt = [0] * n
    wt = [0] * n
    for i in range(n):
        rt[i] = burst_time[i]

    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False
    while (complete != n):
        for j in range(n):
            if (arrival_time[j] <= t and (rt[j] > 0 and rt[j] < minm)):
                minm = rt[j]
                short = j
                check = True

        if (check == False):
            t += 1
            continue
        rt[short] -= 1

        minm = rt[short]
        if (minm == 0):
            minm = 999999999

        if (rt[short] == 0):

            complete += 1
            check = False
            fint = t + 1

            wt[short] = (fint - arrival_time[short] -
                         burst_time[short])

            if (wt[short] < 0):
                wt[short] = 0
        t += 1
    return wt


def SRTF_findTurnAroundTime(burst_time,arrival_time, n, wt):
    tat = [0] * n
    for i in range(n):
        tat[i] = burst_time[i] + wt[i]
    return tat


def SRTF_findavgTime(wt, tat, at, n):
    total_wt = 0
    total_tat = 0
    compl_time = [0] * n
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time[i] = tat[i] + at[i]

    Avg_Turn_around_Time = Label(text="Average turn around time  " + ": " + str((total_tat / n)),bg="light green")
    Avg_Turn_around_Time.place(x=20, y=120+(n+1)*20)
    Avg_Waiting_time = Label(text="Average waiting time " + ": " + str((total_wt / n)),bg="light green")
    Avg_Waiting_time.place(x=20, y=200++(n+1)*20)
    clear_widget.append(Avg_Turn_around_Time)
    clear_widget.append(Avg_Waiting_time)

    return compl_time


def show(wt, tat, compl_time,n):
    e = 120
    for i in range(n):
        t1 = Label(text=str(wt[i]),bg="light green")
        clear_widget.append(t1)
        t1.place(x=250, y=e)
        e += 20
    e = 120
    for i in range(n):
        t1 = Label(text=str(tat[i]),bg="light green")
        clear_widget.append(t1)
        t1.place(x=350, y=e)
        e += 20
    e = 120
    for i in range(n):
        t1 = Label(text=str(compl_time[i]),bg="light green")
        clear_widget.append(t1)
        t1.place(x=450, y=e)
        e += 20


screen = Tk()
screen['bg']="light green"
screen.geometry("1100x1100")
screen.title("OS")

heading = Label(text="Operating system", bg="dark green", fg="yellow", width="500", height="3",font="Helvetica 13 bold")
process_no = Label(text="Enter The Number of Process",bg="light green",font="Helvetica 10 bold")
Arriva_time = Label(text="Arrival_time",bg="light green",font="Helvetica 10 bold")
Brust_Time = Label(text="Brust_Time",bg="light green",font="Helvetica 10 bold")
Waiting_Time = Label(text="Waiting_Time",bg="light green",font="Helvetica 10 bold")
TAT_Time = Label(text="TAT_Time",bg="light green",font="Helvetica 10 bold")
complitation_Time = Label(text="complitation_Time",bg="light green",font="Helvetica 10 bold")

heading.pack()
process_no.place(x=50,y=70)
Arriva_time.place(x=20, y=100)
Brust_Time.place(x=150, y=100)
Waiting_Time.place(x=250, y=100)
TAT_Time.place(x=350, y=100)
complitation_Time.place(x=450, y=100)


bt=[]
at=[]
widget_list=[]
A1= IntVar()
a11 = Entry(textvariable=A1, width='10')
a11.place(x=250, y=70)
def start():

    for i in range(int(a11.get())):
        A21=IntVar()
        A22 = IntVar()
        a21 = Entry(textvariable=A21, width='10')
        a21.place(x=20, y=(120+20*i))
        a22 = Entry(textvariable=A22, width='10')
        a22.place(x=150, y=(120+20*i))

        at.append(a21)
        bt.append(a22)
def hallo_FCFS():
    widget_list.extend(at)
    widget_list.extend(bt)
    arrival_time=list([int(i.get()) for i in at])
    burst_time=list([int(i.get()) for i in bt])
    algo_FCFS(burst_time, arrival_time)
    burst_time.clear()
    arrival_time.clear()
    at.clear()
    bt.clear()

def hallo_SRTF():
    widget_list.extend(at)
    widget_list.extend(bt)
    arrival_time=list([int(i.get()) for i in at])
    burst_time=list([int(i.get()) for i in bt])
    algo_SRTF(burst_time, arrival_time)
    burst_time.clear()
    arrival_time.clear()
    at.clear()
    bt.clear()

def Reset():

    python = sys.executable
    print(python)
    os.execl(python, python, * sys.argv)

#    a11.delete(0, END)
#    for e in widget_list:
#        e.delete(0, END)
#    for i in clear_widget:
#        i['text']="   "
#    widget_list.clear()
#    clear_widget.clear()

print("started")

Submit = Button(screen, text="PROCEED",width='10', height='1', command=start,bg="Dark Blue",fg="white" )
Submit.place(x=350 ,y=70)

FCFS = Button(screen, text="FCFS", width='10', height='2', command=hallo_FCFS, bg="Dark Blue",fg="white" )
FCFS.place(x=80, y=600)

SRTF = Button(screen, text="SRTF", width='10', height='2', command=hallo_SRTF, bg="Dark Blue",fg="white" )
SRTF.place(x=200, y=600)

Clear = Button(screen, text="RESET", width='10', height='2', command=Reset, bg="Dark Blue",fg="white" )
Clear.place(x=320, y=600)

screen.mainloop()
