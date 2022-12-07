from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms 
from .models import UserProfile
#from .models import RegisterUser


MEME_CATEGORIES = (
    ('animals','animals'),
    ('fail','fail'),
    ('confused','confused'),
    ('gaming','gaming'),

)
#################Normal User Form#############################
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2') #phone maybe?


    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    def CleanUserName(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)
        return username
    
    def GetUserName(self):
        return self.cleaned_data['username']

class UserUpdateForm(forms.ModelForm):

    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True,
                                widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','email')

#################Ext of User to pick Memes##################
class UserProfileForm(forms.ModelForm):
    meme_categories = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,
                       choices=MEME_CATEGORIES)

    class Meta:
        model = UserProfile
        fields = ('meme_categories',)

class ProfileUpdateForm(forms.ModelForm):
    meme_categories = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,
                      choices=MEME_CATEGORIES)
    class Meta:
        model = UserProfile
        fields = ('meme_categories', )

