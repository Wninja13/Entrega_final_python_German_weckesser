from django import forms
from .models import Repartidor, Tienda, Producto, Pago, Usuario, Cancelacion, Orden
from .models import MiUsuarioPersonalizado
from .models import Perfil

class RepartidorForm(forms.ModelForm):
    class Meta:
        model = Repartidor
        fields = '__all__'

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = '__all__'

class ProductoForm(forms.ModelForm): 
    class Meta: 
        model = Producto
        fields = '__all__'

class PagoForm(forms.ModelForm): 
    class Meta: 
        model = Pago
        fields = '__all__'

class UsuarioForm(forms.ModelForm): 
    class Meta:
        model = Usuario
        fields = '__all__'

class CancelacionForm(forms.ModelForm):
    class Meta: 
        model = Cancelacion
        fields = '__all__'
    
class OrdenForm(forms.ModelForm):
    class Meta: 
        model = Orden
        fields = '__all__'
    
class LoginForm(forms.Form):  # Utiliza forms.Form en lugar de forms.ModelForm
    login_username = forms.CharField(label="Nombre de usuario", max_length=100)
    login_password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class LoginForm(forms.ModelForm):
    class Meta:
        model = MiUsuarioPersonalizado  
        fields = ['username', 'email', 'password']  
        widgets = {
            'password': forms.PasswordInput(),  
        }
        
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre', 'fecha_nacimiento', 'biografia', 'avatar']