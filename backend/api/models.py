from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator
# Create your models here.

def makeChoices(*choices):
    out = []
    for choice in range(len(choices)):
        out.append((choice, choices[choice]))
    return out

HUE_CHOICES = makeChoices(
    'Branco-papel',
    'Verdeal',
    'Amarelo-alpha',
    'Amarelo-ouro',
    'Amarelo-âmbar',
    'Rosado',
    'Cereja',
    'Clarete',
    'Vermelho-púrpura',
    'Vermelho-rubí',
    'Vermelho-granada',
    'Vermelho-alaranjado'
)

INTENSITY_CHOICES = makeChoices(
    'Claro',
    'Escuro'
)

FLUIDITY_CHOICES = makeChoices(
    'Muito escorregadio',
    'Escorregadio',
    'Denso',
    'Xaroposo',
    'Fiadeiro'
)
REFLEXES_CHOICES= makeChoices(
    'Âmbar',
    'Alaranjados',
    'Violáceos',
    'Esverdeados',
    'Granada',
    'Outros'
)

LUCIDITY_CHOICES = makeChoices(
    'Muito transparente',
    'Transparente',
    'Regular',
    'Leve opacidade',
    'Opaco'
)

SUGARS_CHOICES = makeChoices(
    'Seco',
    'Suave',
    'Meio-doce',
    'Doce',
    'Licoroso'
)

ACIDITY_CHOICES = makeChoices(
    'Mole',
    'Chato',
    'Sápio',
    'Fresco, vivo, nervoso',
    'Aciduloso, Áspero'
)

ALCOHOL_CHOICES = makeChoices(
    'Fraco',
    'Pouco Alcoólico',
    'Equilibrado',
    'Quente',
    'Muito Quente'
)


SOFTNESS_CHOICES = makeChoices(
    'Carente',
    'Um pouco carente',
    'Macio',
    'Redondo',
    'Pastoso, untoso'
)

BODY_CHOICES = makeChoices(
    'Magro',
    'Pouco encorpado',
    'Bom corpo',
    'Muito encorpado',
    'Massudo'
)

TANACITY_CHOICES = makeChoices(
    'Carente',
    'Pouco tânico',
    'Equilibrado',
    'Tânico',
    'Muito tânico'
)

MOUTH_CHOICES = makeChoices(
    'Fresca',
    'Limpa',
    'Enxuta',
    'Árida',
    'Com Fundo'
)

EVOLUTION_CHOICES = makeChoices(
    'Jovem',
    'Pronto',
    'Maduro',
    'Ligeiramente envelhecimento',
    'Envelhecido',
    'Decrépito'
)


class Wine(models.Model):

    name        = models.CharField( verbose_name='Vinho' , max_length=100)
    harvest     = models.IntegerField(
                                        verbose_name='Safra', 
                                        validators=[
                                                        MinValueValidator(0), 
                                                        #MaxLengthValidator(4) 
                                                    ]
                                    )
    local       = models.CharField( verbose_name='Local',max_length=100)
    prod        = models.CharField( verbose_name='Produtor',max_length=100)
    alc_cont    = models.DecimalField(
                                        verbose_name='Teor alc', 
                                        validators=[
                                                        MinValueValidator(0), 
                                                        MaxValueValidator(100)
                                                    ],
                                        max_digits=5, 
                                        decimal_places=2
                                    )
    serv_temp   = models.DecimalField(
                                        verbose_name='Temp serv', 
                                        max_digits=5, 
                                        decimal_places=2,
                                        validators=[
                                                        MinValueValidator(0),
                                                    ]
                                        
                                    )
    amb_temp    = models.DecimalField(
                                        verbose_name='Temb amb', 
                                        max_digits=5, 
                                        decimal_places=2,
                                        validators=[
                                                        MinValueValidator(0),
                                                    ]
                                    )


    def __str__(self):
        return f'{str(self.name).capitalize()} {self.harvest}'

class Review(models.Model):

    wine =  models.ForeignKey(Wine, null=False, on_delete=models.CASCADE)
    taster      = models.CharField( verbose_name='Degustador',max_length=100, default='ANONIMO')
    date        = models.DateField( verbose_name='Data', default='2019-12-19')

    I_hue       = models.IntegerField( verbose_name='Tonalidade', choices = HUE_CHOICES)
    I_intensity = models.IntegerField(verbose_name='Intensidade', choices = INTENSITY_CHOICES)
    I_fluidity  = models.IntegerField( verbose_name='Fluidez', choices = FLUIDITY_CHOICES)
    I_reflex    = models.IntegerField(verbose_name='Reflexos', choices = REFLEXES_CHOICES)
    I_lucidity  = models.IntegerField(verbose_name='Fluidez', choices = LUCIDITY_CHOICES)
    I_clarity   = models.DecimalField(
                                        verbose_name='Limpidez', 
                                        max_digits=3, 
                                        decimal_places=2,
                                        validators=[
                                                        MinValueValidator(0),
                                                        MaxValueValidator(8)
                                                    ]    
                                    )
    I_color     = models.DecimalField( 
                                        verbose_name='Cor', 
                                        validators=[
                                                        MinValueValidator(0),
                                                        MaxValueValidator(8)
                                                    ],
                                        max_digits=3, 
                                        decimal_places=2)

    II_general_features_frank       = models.BooleanField(verbose_name='Franco', default=False)
    II_general_features_broad       = models.BooleanField(verbose_name='Amplo', default=False)
    II_general_features_flagrant    = models.BooleanField(verbose_name='Flagrante', default=False)
    II_general_features_fruity      = models.BooleanField(verbose_name='Frutado', default=False)
    II_general_features_vinous      = models.BooleanField(verbose_name='Vinoso', default=False)
    II_general_features_defective   = models.BooleanField(verbose_name='Defeituoso', default=False)
    II_general_features_ethereal    = models.BooleanField(verbose_name='Etereo', default=False)
    II_general_features_floral      = models.BooleanField(verbose_name='Floral', default=False)
    II_general_features_vegetal     = models.BooleanField(verbose_name='Vegetal', default=False)
    II_general_features_other       = models.TextField( verbose_name='Outros Carecteres', blank=True)
    
    II_quality           = models.DecimalField(
                                                    verbose_name='Qualidade',
                                                    validators=[
                                                        MinValueValidator(0),
                                                        MaxValueValidator(12)
                                                    ],
                                                    max_digits=4, 
                                                    decimal_places=2
                                            )
    II_intensity         = models.DecimalField(
                                                    verbose_name='Intensidade',
                                                    validators=[
                                                        MinValueValidator(0),
                                                        MaxValueValidator(4)
                                                    ],
                                                    max_digits=3, 
                                                    decimal_places=2
                                            )
    II_persistence       = models.DecimalField(
                                                    verbose_name='Persistencia', 
                                                    validators=[
                                                        MinValueValidator(0),
                                                        MaxValueValidator(8)
                                                    ], 
                                                    max_digits=3, 
                                                    decimal_places=2
                                                    )
    II_perseptive_traces = models.TextField( verbose_name='Traços Percepitivos',blank=True)

    III_sugars      = models.IntegerField( verbose_name='Açucares', choices = SUGARS_CHOICES)
    III_acidity     = models.IntegerField( verbose_name='Acidez', choices = ACIDITY_CHOICES)
    III_alcohol     = models.IntegerField( verbose_name='Alcool', choices = ALCOHOL_CHOICES)
    III_softness    = models.IntegerField( verbose_name='Maciez', choices = SOFTNESS_CHOICES)
    III_body        = models.IntegerField( verbose_name='Corpo', choices = BODY_CHOICES)
    III_tanacity    = models.IntegerField( verbose_name='Tenacidade', choices = TANACITY_CHOICES)

    III_balanced            = models.DecimalField(
                                                    verbose_name='Equilíbrio', 
                                                    validators=[
                                                        MinValueValidator(0),
                                                        MaxValueValidator(16)
                                                    ], 
                                                    max_digits=4, 
                                                    decimal_places=2
                                                )
    III_quality             = models.DecimalField(
                                                    verbose_name='Qualidade', 
                                                    validators=[
                                                        MinValueValidator(0),
                                                        MaxValueValidator(16)
                                                    ],
                                                    max_digits=4, 
                                                    decimal_places=2
                                                )
    III_aromatic_persist    = models.DecimalField(
                                                    verbose_name='Persistencia aromatica', 
                                                    validators=[
                                                        MinValueValidator(0),
                                                        MaxValueValidator(12)
                                                    ],
                                                    max_digits=4, 
                                                    decimal_places=2
                                                )

    ends_well           = models.BooleanField(verbose_name='Termina bem', default=False)
    leave_mouth         = models.IntegerField( verbose_name='Deixa a Boca', choices = MOUTH_CHOICES)
    leave_mouth_outher  = models.CharField(max_length=100)

    evolution = models.IntegerField( verbose_name='Evolução', choices = MOUTH_CHOICES)

    final_obs =  models.TextField( verbose_name='Observações Finais', blank=True)
    