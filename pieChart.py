import matplotlib.pyplot as plotter

def drawPieChart(Labels,Share,Name):
    figureObject, axesObject = plotter.subplots()

    # Draw the pie chart

    axesObject.pie(Share,labels=Labels,autopct='%1.2f',startangle=90)
 
    # Aspect ratio - equal means pie is a circle

    axesObject.axis('equal')
    plotter.savefig(Name)
plotter.show()
