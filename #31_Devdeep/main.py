from basic_plot import BasicPlot

if __name__ == '__main__':
    qr_size = int(input("enter the size of the QR : "))
    size_factor = int(input("enter the size factor for the recog. pattern : "))
    ploter = BasicPlot()
    ploter.plot(qr_size, size_factor)