import PySimpleGUI as sg
import qrcode

sg.theme("PythonPlus")

qr_image= [sg.Image('',key ='Qr_CODE')]

layout = [
     [sg.Text('INPUT TEXT TO BE CONVERTED')],
     [sg.Input('',key='TEXT')],
     [sg.Text('QR code size:')],
     [sg.Slider(range=(100, 500), default_value=200,key='size')],
     [sg.Text('QR code color:')],
     [sg.ColorChooserButton('Choose color', key='color')],
     [sg.Button('CREATE', key='CREATE')],
     [sg.Column([qr_image], justification='center')]
             
]
 
window = sg.Window(" SENG207_3_QRCODE GENERATOR", layout)

while True:
    event, values = window.read()
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break
    elif event =='CREATE':
        text = values['TEXT']
        if text:
            img = qrcode.make(text)
            img.save('qr.png')
            window['Qr_CODE'].update('qr.png')

window.close()