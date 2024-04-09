from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
from misitioweb.settings import EMAIL_HOST_USER


def contact(request):    
    if request.method == 'POST':            # En este caso procesaremos el formulario
        form = ContactForm(request.POST)    # Almacenamos los datos del formulario
        if form.is_valid():                 # Comprobamos que los datos del formulario son válidos
            cd = form.cleaned_data

            # Enviaremos el email y redireccionamos
            email = EmailMessage (
                'Nuevo mensaje de MISITIOWEB',  # Asunto del mensaje
                'De {} <{}>\n {}'.format(cd['name'],cd['email'],cd['content']), # Datos del mensaje
                EMAIL_HOST_USER, # Origen del email que nosotros enviamos
                ['iban.formoso@entelgy.com'], # Destino principal de nuestro email(nosotros)
                reply_to=[cd['email']], # Email de replica, para contestar
            )
            try:
                email.send()
                # Si va todo bien
                return redirect(reverse('contact')+'?ok')
            except:
                # Si algo va mal
                return redirect(reverse('contact')+'?fail')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

# Forma manual de formularios
"""
def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('nombre', ''):
            errors.append('Por favor introduce el nombre.')
        if not request.POST.get('mensaje', ''):
            errors.append('Por favor introduce un mensaje.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Por favor introduce una direccion de e­mail valida.')
        if not errors:
            #enviaremos el email y redireccionamos
             return redirect(reverse('contact')+'?ok')
    return render(request, 'contact/contact.html', {'errors': errors,
        'asunto': request.POST.get('asunto', ''),
        'mensaje': request.POST.get('mensaje', ''),
        'email': request.POST.get('email', ''),
    })
"""