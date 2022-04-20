from claseEmail import Email
from claseManejadorEmails import ManejadorEmails

if __name__ == '__main__':
    ### Inciso 1
    nombre = input('Ingrese su nombre:')
    print('Ingrese su email por partes.')
    idc = input('Ingrese id de cuenta:')
    dom = input('Ingrese dominio:')
    tipodom = input('Ingrese tipo de dominio:')
    contra = input('Ingrese contrasenha:')
    unEmail = Email(idc, dom, tipodom, contra) ### Crea la instancia con los datos
    print('Estimado/a {} te enviaremos tus mensajes a la direccion {}'.format(nombre, unEmail.retornaEmail()))
    ### Inciso 2
    unEmail.modificaContrasenha()
    ### Inciso 3
    em = input('Ingrese su email:')
    otroEmail = Email('', '', '', '') ### Nota: se puede enviar palabras en blanco (entre comillas simples)
    otroEmail.crearCuenta(em)
    print('Email: {}'.format(otroEmail.retornaEmail()))
    ### Inciso 4
    me = ManejadorEmails()
    me.CargaEmails()
    idc = input('Ingrese id de cuenta a buscar:')
    me.IndicaRepetido(idc)