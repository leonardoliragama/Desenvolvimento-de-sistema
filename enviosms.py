from tkinter import *
from tkinter import messagebox
from telesign.messaging import MessagingClient

def EnvioSms():
    customer_id = "4BDCCE17-EDCF-4648-BDF5-68469D15D9D3"
    api_key = "GhjQwEhsuN83uxRvW5okv75dm9IC7JTpA85YfmHzmeSjaS54Z03JHLVDpTWrgQ2XV1/drejFNjLngT5k2xN/+Q==GhjQwEhsuN83uxRvW5okv75dm9IC7JTpA85YfmHzmeSjaS54Z03JHLVDpTWrgQ2XV1/drejFNjLngT5k2xN/+Q=="
    phone_number = "55" + txtNumero.get()
    message = txtMensagem.get()
    message_type = "ARN"
    messaging = MessagingClient(customer_id, api_key)
    response = messaging.message(phone_number, message, message_type)
    if response.status_code == 200:
        messagebox.showinfo("success", "SMS Enviado Com Sucesso")
    else:
        messagebox.showerror("error", "Falha ao enviar SMS, Verifique o Numero e tente novamente")

main = Tk()
main.title('Envio SMS ')
main.geometry('300x200')

flow = 0
while flow < 10:
    main.rowconfigure(flow, weight=1)
    main.columnconfigure(flow, weight=1)
    flow += 1

txtNumero = Entry(main)
txtNumero.insert(0, 'Digite seu Numero')
txtNumero.grid(row=3, column=5, sticky="NS")

txtMensagem = Entry(main)
txtMensagem.insert(0, 'Digite sua Mensagem')
txtMensagem.grid(row=4, column=5, sticky="NS")

btnEnviar = Button(main, text='Enviar', command=EnvioSms)
btnEnviar.grid(row=5, column=5, sticky='NESW')
main.mainloop()



