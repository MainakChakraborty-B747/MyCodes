import matplotlib.pyplot as plt
import os
def lineplot():
    x=[]
    y=[]
    xno=int(input("Enter the number of elements in X axis: "))
    yno=int(input("Enter the number of elements in Y axis: "))
    if xno!=yno:
        print("Can't plot ....")
        main()
    else:
        print("Enter the datapoints for X axis---->")
        for i in range(0, xno):
            temp=int(input(f"Enter the {i+1} element: "))
            x.append(temp)
        print("Enter the datapoints for Y axis---->")
        for i in range(0, yno):
            temp=int(input(f"Enter the {i+1} element: "))
            y.append(temp)
        os.system('cls')
        xtitle=input("Enter the title of the X axis: ")
        ytitle=input("Enter the title of the Y axis: ")
        font=int(input("Enter the font size for labels(1-50): "))
        plt.xlabel(xtitle, fontsize=font)
        plt.ylabel(ytitle, fontsize=font)
        Title=input("Enter the title of the plot: ")
        plt.title(Title)
        ls=input("Choose linestyle(Available options are -,--,-.,:) : ")
        c=input("Choose color(supported: red, blue, green, yellow, orange): ")
        mark=input("Choose marker style(supported:*,+,. ; enter a space if no marker needed): ")
        ms=float(input("Enter marker size(recommended: 5-15): "))
        plt.plot(x,y,color=c,linestyle=ls,marker=mark,markersize=ms)
        plt.grid(True)
        plt.show()
#lineplot()
def barplot():
    x=[]
    y=[]
    xno=int(input("Enter the number of elements in X axis: "))
    yno=int(input("Enter the number of elements in Y axis: "))
    if xno!=yno:
        print("Can't plot ....")
        main()
    else:
        print("Enter the datapoints for X axis---->")
        for i in range(0, xno):
            temp=int(input(f"Enter the {i+1} element: "))
            x.append(temp)
        print("Enter the datapoints for Y axis---->")
        for i in range(0, yno):
            temp=int(input(f"Enter the {i+1} element: "))
            y.append(temp)
        os.system('cls')
        xtitle=input("Enter the title of the X axis: ")
        ytitle=input("Enter the title of the Y axis: ")
        font=int(input("Enter the font size for labels(1-50): "))
        plt.xlabel(xtitle, fontsize=font)
        plt.ylabel(ytitle, fontsize=font)
        Title=input("Enter the title of the plot: ")
        plt.title(Title)
        w=float(input("Enter the width of the bars(recommended: 0.1-0.5) : "))
        c=input("Choose color(supported: red, blue, green, yellow, orange): ")
        plt.bar(x,y,color=c,width=w,align='edge')
        plt.grid(True)
        plt.show()
#barplot()
def piechart():
    x=[]
    xno=int(input("Enter the number of elements in X axis: "))
    print("Enter the datapoints ---->")
    for i in range(0, xno):
        temp=int(input(f"Enter the {i+1} element: "))
        x.append(temp)
    label=input("Enter the name of the labels: ")
    label=list(label.split(','))
    #the above 2 lines of code take a string separated by comma an then in next line , taking comma as the delimiter , a list of inputs is name of string data type 
    plt.pie(x,labels=label, colors=['red', 'blue', 'green', 'yellow', 'orange','cyan','magenta'])
    plt.show()
#piechart()    
def scatter():
    x=[]
    y=[]
    xno=int(input("Enter the number of elements in X axis: "))
    yno=int(input("Enter the number of elements in Y axis: "))
    if xno!=yno:
        print("Can't plot ....")
        main()
    else:
        print("Enter the datapoints for X axis---->")
        for i in range(0, xno):
            temp=int(input(f"Enter the {i+1} element: "))
            x.append(temp)
        print("Enter the datapoints for Y axis---->")
        for i in range(0, yno):
            temp=int(input(f"Enter the {i+1} element: "))
            y.append(temp)
        os.system('cls')
        xtitle=input("Enter the title of the X axis: ")
        ytitle=input("Enter the title of the Y axis: ")
        font=int(input("Enter the font size for labels(1-50): "))
        plt.xlabel(xtitle, fontsize=font)
        plt.ylabel(ytitle, fontsize=font)
        Title=input("Enter the title of the plot: ")
        plt.title(Title)
        print("Choose colors(Recommended: red, blue, green, yellow, orange,cyan,magenta)")
        c=input("if colour exceeds the no. of datapoints, program will result in error: ")
        c=list(c.split(','))
        plt.scatter(x,y,color=c)
        plt.grid(True)
        plt.show()
#scatter()
def main():
    print("____Welcome to simple graph plotter____")
    c=int(input('''
                    1.line plot
                    2.bar plot
                    3.pie chart
                    4.scatter plot
                    Please select your choice: '''))
    os.system('cls')
    if c==1:
        lineplot()
        os.system('cls')
    elif c==2:
        barplot()
        os.system('cls')
    elif c==3:
        piechart()
        os.system('cls')
    elif c==4:
        scatter()
        os.system('cls')
    else:
        print("Wrong Choice...")
        main()
main()
    
    
    

    
        

        
