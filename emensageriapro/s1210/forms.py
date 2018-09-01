# coding: utf-8
from django import forms
from emensageriapro.s1210.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s1210evtPgtos 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s1210_idepgtoext(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_idepgtoext,self ).__init__(*args,**kwargs)
        
        self.fields['nmcid'].widget.attrs['required'] = True
        
        self.fields['dsclograd'].widget.attrs['required'] = True
        
        self.fields['indnif'].widget.attrs['required'] = True
        
        self.fields['codpais'].widget.attrs['required'] = True
        
        self.fields['s1210_infopgto'].widget.attrs['required'] = True

    class Meta:
        model = s1210idePgtoExt
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_detpgtoant_infopgtoant(forms.ModelForm):
    vrbcirrf = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_detpgtoant_infopgtoant,self ).__init__(*args,**kwargs)
        
        self.fields['vrbcirrf'].widget.attrs['required'] = True
        
        self.fields['tpbcirrf'].widget.attrs['required'] = True
        self.fields['s1210_detpgtoant'].queryset = s1210detPgtoAnt.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1210_detpgtoant'].widget.attrs['required'] = True

    class Meta:
        model = s1210detPgtoAntinfoPgtoAnt
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_detpgtoant(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_detpgtoant,self ).__init__(*args,**kwargs)
        
        self.fields['codcateg'].widget.attrs['required'] = True
        self.fields['s1210_infopgto'].queryset = s1210infoPgto.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1210_infopgto'].widget.attrs['required'] = True

    class Meta:
        model = s1210detPgtoAnt
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_detpgtofer_penalim(forms.ModelForm):
    vlrpensao = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_detpgtofer_penalim,self ).__init__(*args,**kwargs)
        
        self.fields['vlrpensao'].widget.attrs['required'] = True
        
        self.fields['nmbenefic'].widget.attrs['required'] = True
        
        self.fields['cpfbenef'].widget.attrs['required'] = True
        self.fields['s1210_detpgtofer_detrubrfer'].queryset = s1210detPgtoFerdetRubrFer.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1210_detpgtofer_detrubrfer'].widget.attrs['required'] = True

    class Meta:
        model = s1210detPgtoFerpenAlim
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_detpgtofer_detrubrfer(forms.ModelForm):
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_detpgtofer_detrubrfer,self ).__init__(*args,**kwargs)
        
        self.fields['vrrubr'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        self.fields['s1210_detpgtofer'].queryset = s1210detPgtoFer.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1210_detpgtofer'].widget.attrs['required'] = True

    class Meta:
        model = s1210detPgtoFerdetRubrFer
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_detpgtofer(forms.ModelForm):
    vrliq = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_detpgtofer,self ).__init__(*args,**kwargs)
        
        self.fields['vrliq'].widget.attrs['required'] = True
        
        self.fields['qtdias'].widget.attrs['required'] = True
        
        self.fields['dtinigoz'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        self.fields['s1210_infopgto'].queryset = s1210infoPgto.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1210_infopgto'].widget.attrs['required'] = True

    class Meta:
        model = s1210detPgtoFer
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_detpgtobenpr_infopgtoparc(forms.ModelForm):
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_detpgtobenpr_infopgtoparc,self ).__init__(*args,**kwargs)
        
        self.fields['vrrubr'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        self.fields['s1210_detpgtobenpr'].queryset = s1210detPgtoBenPr.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1210_detpgtobenpr'].widget.attrs['required'] = True

    class Meta:
        model = s1210detPgtoBenPrinfoPgtoParc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_detpgtobenpr_retpgtotot(forms.ModelForm):
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_detpgtobenpr_retpgtotot,self ).__init__(*args,**kwargs)
        
        self.fields['vrrubr'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        self.fields['s1210_detpgtobenpr'].queryset = s1210detPgtoBenPr.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1210_detpgtobenpr'].widget.attrs['required'] = True

    class Meta:
        model = s1210detPgtoBenPrretPgtoTot
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_detpgtobenpr(forms.ModelForm):
    vrliq = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_detpgtobenpr,self ).__init__(*args,**kwargs)
        
        self.fields['vrliq'].widget.attrs['required'] = True
        
        self.fields['indpgtott'].widget.attrs['required'] = True
        
        self.fields['idedmdev'].widget.attrs['required'] = True
        
        self.fields['perref'].widget.attrs['required'] = True
        
        self.fields['s1210_infopgto'].widget.attrs['required'] = True

    class Meta:
        model = s1210detPgtoBenPr
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_detpgtofl_infopgtoparc(forms.ModelForm):
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_detpgtofl_infopgtoparc,self ).__init__(*args,**kwargs)
        
        self.fields['vrrubr'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        self.fields['s1210_detpgtofl'].queryset = s1210detPgtoFl.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1210_detpgtofl'].widget.attrs['required'] = True

    class Meta:
        model = s1210detPgtoFlinfoPgtoParc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_detpgtofl_penalim(forms.ModelForm):
    vlrpensao = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_detpgtofl_penalim,self ).__init__(*args,**kwargs)
        
        self.fields['vlrpensao'].widget.attrs['required'] = True
        
        self.fields['nmbenefic'].widget.attrs['required'] = True
        
        self.fields['cpfbenef'].widget.attrs['required'] = True
        self.fields['s1210_detpgtofl_retpgtotot'].queryset = s1210detPgtoFlretPgtoTot.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1210_detpgtofl_retpgtotot'].widget.attrs['required'] = True

    class Meta:
        model = s1210detPgtoFlpenAlim
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_detpgtofl_retpgtotot(forms.ModelForm):
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_detpgtofl_retpgtotot,self ).__init__(*args,**kwargs)
        
        self.fields['vrrubr'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        self.fields['s1210_detpgtofl'].queryset = s1210detPgtoFl.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1210_detpgtofl'].widget.attrs['required'] = True

    class Meta:
        model = s1210detPgtoFlretPgtoTot
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_detpgtofl(forms.ModelForm):
    vrliq = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_detpgtofl,self ).__init__(*args,**kwargs)
        
        self.fields['vrliq'].widget.attrs['required'] = True
        
        self.fields['indpgtott'].widget.attrs['required'] = True
        
        self.fields['idedmdev'].widget.attrs['required'] = True
        self.fields['s1210_infopgto'].queryset = s1210infoPgto.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1210_infopgto'].widget.attrs['required'] = True

    class Meta:
        model = s1210detPgtoFl
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_infopgto(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_infopgto,self ).__init__(*args,**kwargs)
        
        self.fields['indresbr'].widget.attrs['required'] = True
        
        self.fields['tppgto'].widget.attrs['required'] = True
        
        self.fields['dtpgto'].widget.attrs['required'] = True
        self.fields['s1210_evtpgtos'].queryset = s1210evtPgtos.objects.using( slug ).filter(excluido=False).all()
        self.fields['s1210_evtpgtos'].widget.attrs['required'] = True

    class Meta:
        model = s1210infoPgto
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s1210_deps(forms.ModelForm):
    vrdeddep = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s1210_deps,self ).__init__(*args,**kwargs)
        
        self.fields['vrdeddep'].widget.attrs['required'] = True
        
        self.fields['s1210_evtpgtos'].widget.attrs['required'] = True

    class Meta:
        model = s1210deps
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]
