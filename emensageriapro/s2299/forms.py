# coding: utf-8
from django import forms
from emensageriapro.s2299.models import * 
from emensageriapro.controle_de_acesso.models import Usuarios 
from emensageriapro.esocial.models import s2299evtDeslig 


__author__ = 'marcelovasconcellos'



#custom_forms#



class form_s2299_infotrabinterm_consigfgts(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infotrabinterm_consigfgts,self ).__init__(*args,**kwargs)
        
        self.fields['nrcontr'].widget.attrs['required'] = True
        
        self.fields['insconsig'].widget.attrs['required'] = True
        self.fields['s2299_evtdeslig'].queryset = s2299evtDeslig.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoTrabIntermconsigFGTS
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infotrabinterm_quarentena(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infotrabinterm_quarentena,self ).__init__(*args,**kwargs)
        
        self.fields['dtfimquar'].widget.attrs['required'] = True
        
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoTrabIntermquarentena
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infotrabinterm_proccs(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infotrabinterm_proccs,self ).__init__(*args,**kwargs)
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        
        self.fields['s2299_verbasresc'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoTrabIntermprocCS
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infotrabinterm_remunoutrempr(forms.ModelForm):
    vlrremunoe = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infotrabinterm_remunoutrempr,self ).__init__(*args,**kwargs)
        
        self.fields['vlrremunoe'].widget.attrs['required'] = True
        
        self.fields['codcateg'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        self.fields['s2299_infotrabinterm_infomv'].queryset = s2299infoTrabInterminfoMV.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infotrabinterm_infomv'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoTrabIntermremunOutrEmpr
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infotrabinterm_infomv(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infotrabinterm_infomv,self ).__init__(*args,**kwargs)
        
        self.fields['indmv'].widget.attrs['required'] = True
        
        self.fields['s2299_verbasresc'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoTrabInterminfoMV
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infotrabinterm_procjudtrab(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infotrabinterm_procjudtrab,self ).__init__(*args,**kwargs)
        
        self.fields['nrprocjud'].widget.attrs['required'] = True
        
        self.fields['tptrib'].widget.attrs['required'] = True
        self.fields['s2299_verbasresc'].queryset = s2299verbasResc.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_verbasresc'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoTrabIntermprocJudTrab
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infotrabinterm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infotrabinterm,self ).__init__(*args,**kwargs)
        
        self.fields['codconv'].widget.attrs['required'] = True
        self.fields['s2299_dmdev'].queryset = s2299dmDev.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_dmdev'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoTrabInterm
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperant_infosimples(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperant_infosimples,self ).__init__(*args,**kwargs)
        
        self.fields['indsimples'].widget.attrs['required'] = True
        
        self.fields['s2299_infoperant_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerAntinfoSimples
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperant_infoagnocivo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperant_infoagnocivo,self ).__init__(*args,**kwargs)
        
        self.fields['grauexp'].widget.attrs['required'] = True
        
        self.fields['s2299_infoperant_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerAntinfoAgNocivo
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperant_detverbas(forms.ModelForm):
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperant_detverbas,self ).__init__(*args,**kwargs)
        
        self.fields['vrrubr'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        self.fields['s2299_infoperant_ideestablot'].queryset = s2299infoPerAntideEstabLot.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperant_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerAntdetVerbas
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperant_ideestablot(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperant_ideestablot,self ).__init__(*args,**kwargs)
        
        self.fields['codlotacao'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        self.fields['s2299_infoperant_ideperiodo'].queryset = s2299infoPerAntidePeriodo.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperant_ideperiodo'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerAntideEstabLot
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperant_ideperiodo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperant_ideperiodo,self ).__init__(*args,**kwargs)
        
        self.fields['perref'].widget.attrs['required'] = True
        self.fields['s2299_infoperant_ideadc'].queryset = s2299infoPerAntideADC.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperant_ideadc'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerAntidePeriodo
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperant_ideadc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperant_ideadc,self ).__init__(*args,**kwargs)
        
        self.fields['dsc'].widget.attrs['required'] = True
        
        self.fields['dtefacconv'].widget.attrs['required'] = True
        
        self.fields['tpacconv'].widget.attrs['required'] = True
        
        self.fields['dtacconv'].widget.attrs['required'] = True
        self.fields['s2299_infoperant'].queryset = s2299infoPerAnt.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperant'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerAntideADC
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperant(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperant,self ).__init__(*args,**kwargs)
        
        self.fields['s2299_dmdev'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerAnt
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperapur_infosimples(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperapur_infosimples,self ).__init__(*args,**kwargs)
        
        self.fields['indsimples'].widget.attrs['required'] = True
        
        self.fields['s2299_infoperapur_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerApurinfoSimples
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperapur_infoagnocivo(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperapur_infoagnocivo,self ).__init__(*args,**kwargs)
        
        self.fields['grauexp'].widget.attrs['required'] = True
        
        self.fields['s2299_infoperapur_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerApurinfoAgNocivo
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperapur_detplano(forms.ModelForm):
    vlrpgdep = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperapur_detplano,self ).__init__(*args,**kwargs)
        
        self.fields['vlrpgdep'].widget.attrs['required'] = True
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['nmdep'].widget.attrs['required'] = True
        
        self.fields['tpdep'].widget.attrs['required'] = True
        self.fields['s2299_infoperapur_detoper'].queryset = s2299infoPerApurdetOper.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperapur_detoper'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerApurdetPlano
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperapur_detoper(forms.ModelForm):
    vrpgtit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperapur_detoper,self ).__init__(*args,**kwargs)
        
        self.fields['vrpgtit'].widget.attrs['required'] = True
        
        self.fields['regans'].widget.attrs['required'] = True
        
        self.fields['cnpjoper'].widget.attrs['required'] = True
        self.fields['s2299_infoperapur_infosaudecolet'].queryset = s2299infoPerApurinfoSaudeColet.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperapur_infosaudecolet'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerApurdetOper
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperapur_infosaudecolet(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperapur_infosaudecolet,self ).__init__(*args,**kwargs)
        
        self.fields['s2299_infoperapur_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerApurinfoSaudeColet
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperapur_detverbas(forms.ModelForm):
    vrrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    vrunit = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    fatorrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)
    qtdrubr = forms.DecimalField(max_digits=15, decimal_places=2, localize=True)

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperapur_detverbas,self ).__init__(*args,**kwargs)
        
        self.fields['vrrubr'].widget.attrs['required'] = True
        
        self.fields['idetabrubr'].widget.attrs['required'] = True
        
        self.fields['codrubr'].widget.attrs['required'] = True
        self.fields['s2299_infoperapur_ideestablot'].queryset = s2299infoPerApurideEstabLot.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperapur_ideestablot'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerApurdetVerbas
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperapur_ideestablot(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperapur_ideestablot,self ).__init__(*args,**kwargs)
        
        self.fields['codlotacao'].widget.attrs['required'] = True
        
        self.fields['nrinsc'].widget.attrs['required'] = True
        
        self.fields['tpinsc'].widget.attrs['required'] = True
        self.fields['s2299_infoperapur'].queryset = s2299infoPerApur.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_infoperapur'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerApurideEstabLot
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_infoperapur(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_infoperapur,self ).__init__(*args,**kwargs)
        
        self.fields['s2299_dmdev'].widget.attrs['required'] = True

    class Meta:
        model = s2299infoPerApur
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_dmdev(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_dmdev,self ).__init__(*args,**kwargs)
        
        self.fields['idedmdev'].widget.attrs['required'] = True
        self.fields['s2299_verbasresc'].queryset = s2299verbasResc.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_verbasresc'].widget.attrs['required'] = True

    class Meta:
        model = s2299dmDev
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_verbasresc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_verbasresc,self ).__init__(*args,**kwargs)
        
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True

    class Meta:
        model = s2299verbasResc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_transftit(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_transftit,self ).__init__(*args,**kwargs)
        
        self.fields['dtnascto'].widget.attrs['required'] = True
        
        self.fields['cpfsubstituto'].widget.attrs['required'] = True
        
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True

    class Meta:
        model = s2299transfTit
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_sucessaovinc(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_sucessaovinc,self ).__init__(*args,**kwargs)
        
        self.fields['cnpjsucessora'].widget.attrs['required'] = True
        
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True

    class Meta:
        model = s2299sucessaoVinc
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]


class form_s2299_observacoes(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        slug = kwargs.pop('slug')
        super (form_s2299_observacoes,self ).__init__(*args,**kwargs)
        
        self.fields['observacao'].widget.attrs['required'] = True
        self.fields['s2299_evtdeslig'].queryset = s2299evtDeslig.objects.using( slug ).filter(excluido=False).all()
        self.fields['s2299_evtdeslig'].widget.attrs['required'] = True

    class Meta:
        model = s2299observacoes
        exclude = [ 
            'excluido',
            'modificado_por',
            'modificado_em',
            'criado_por',
            'criado_em',
 
        ]
