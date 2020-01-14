# Generated by Django 2.2.5 on 2020-01-14 13:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Vinho')),
                ('harvest', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxLengthValidator(4)], verbose_name='Safra')),
                ('local', models.CharField(max_length=100, verbose_name='Local')),
                ('prod', models.CharField(max_length=100, verbose_name='Produtor')),
                ('alc_cont', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)], verbose_name='Teor alc')),
                ('serv_temp', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Temp serv')),
                ('amb_temp', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Temb amb')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taster', models.CharField(default='ANONIMO', max_length=100, verbose_name='Degustador')),
                ('date', models.DateField(default='2019-12-19', verbose_name='Data')),
                ('I_hue', models.IntegerField(choices=[(0, 'Branco-papel'), (1, 'Verdeal'), (2, 'Amarelo-alpha'), (3, 'Amarelo-ouro'), (4, 'Amarelo-âmbar'), (5, 'Rosado'), (6, 'Cereja'), (7, 'Clarete'), (8, 'Vermelho-púrpura'), (9, 'Vermelho-rubí'), (10, 'Vermelho-granada'), (11, 'Vermelho-alaranjado')], verbose_name='Tonalidade')),
                ('I_intensity', models.IntegerField(choices=[(0, 'Claro'), (1, 'Escuro')], verbose_name='Intensidade')),
                ('I_fluidity', models.IntegerField(choices=[(0, 'Muito escorregadio'), (1, 'Escorregadio'), (2, 'Denso'), (3, 'Xaroposo'), (4, 'Fiadeiro')], verbose_name='Fluidez')),
                ('I_reflex', models.IntegerField(choices=[(0, 'Âmbar'), (1, 'Alaranjados'), (2, 'Violáceos'), (3, 'Esverdeados'), (4, 'Granada'), (5, 'Outros')], verbose_name='Reflexos')),
                ('I_lucidity', models.IntegerField(choices=[(0, 'Muito transparente'), (1, 'Transparente'), (2, 'Regular'), (3, 'Leve opacidade'), (4, 'Opaco')], verbose_name='Fluidez')),
                ('I_clarity', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MinValueValidator(8)], verbose_name='Limpidez')),
                ('I_color', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MinValueValidator(8)], verbose_name='Cor')),
                ('II_general_features_frank', models.BooleanField(default=False, verbose_name='Franco')),
                ('II_general_features_broad', models.BooleanField(default=False, verbose_name='Amplo')),
                ('II_general_features_flagrant', models.BooleanField(default=False, verbose_name='Flagrante')),
                ('II_general_features_fruity', models.BooleanField(default=False, verbose_name='Frutado')),
                ('II_general_features_vinous', models.BooleanField(default=False, verbose_name='Vinoso')),
                ('II_general_features_defective', models.BooleanField(default=False, verbose_name='Defeituoso')),
                ('II_general_features_ethereal', models.BooleanField(default=False, verbose_name='Etereo')),
                ('II_general_features_floral', models.BooleanField(default=False, verbose_name='Floral')),
                ('II_general_features_vegetal', models.BooleanField(default=False, verbose_name='Vegetal')),
                ('II_general_features_other', models.TextField(verbose_name='Outros Carecteres')),
                ('II_quality', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MinValueValidator(12)], verbose_name='Qualidade')),
                ('II_intensity', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MinValueValidator(4)], verbose_name='Intensidade')),
                ('II_persistence', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MinValueValidator(8)], verbose_name='Persistencia')),
                ('II_perseptive_traces', models.TextField(verbose_name='Traços Percepitivos')),
                ('III_sugars', models.IntegerField(choices=[(0, 'Seco'), (1, 'Suave'), (2, 'Meio-doce'), (3, 'Doce'), (4, 'Licoroso')], verbose_name='Açucares')),
                ('III_acidity', models.IntegerField(choices=[(0, 'Mole'), (1, 'Chato'), (2, 'Sápio'), (3, 'Fresco, vivo, nervoso'), (4, 'Aciduloso, Áspero')], verbose_name='Acidez')),
                ('III_alcohol', models.IntegerField(choices=[(0, 'Fraco'), (1, 'Pouco Alcoólico'), (2, 'Equilibrado'), (3, 'Quente'), (4, 'Muito Quente')], verbose_name='Alcool')),
                ('III_softness', models.IntegerField(choices=[(0, 'Carente'), (1, 'Um pouco carente'), (2, 'Macio'), (3, 'Redondo'), (4, 'Pastoso, untoso')], verbose_name='Maciez')),
                ('III_body', models.IntegerField(choices=[(0, 'Magro'), (1, 'Pouco encorpado'), (2, 'Bom corpo'), (3, 'Muito encorpado'), (4, 'Massudo')], verbose_name='Corpo')),
                ('III_tanacity', models.IntegerField(choices=[(0, 'Carente'), (1, 'Pouco tânico'), (2, 'Equilibrado'), (3, 'Tânico'), (4, 'Muito tânico')], verbose_name='Tenacidade')),
                ('III_balanced', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MinValueValidator(16)], verbose_name='Equilíbrio')),
                ('III_quality', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MinValueValidator(16)], verbose_name='Qualidade')),
                ('III_aromatic_persist', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MinValueValidator(12)], verbose_name='Persistencia aromatica')),
                ('ends_well', models.BooleanField(default=False, verbose_name='Termina bem')),
                ('leave_mouth', models.IntegerField(choices=[(0, 'Fresca'), (1, 'Limpa'), (2, 'Enxuta'), (3, 'Árida'), (4, 'Com Fundo')], verbose_name='Deixa a Boca')),
                ('leave_mouth_outher', models.CharField(max_length=100)),
                ('evolution', models.IntegerField(choices=[(0, 'Fresca'), (1, 'Limpa'), (2, 'Enxuta'), (3, 'Árida'), (4, 'Com Fundo')], verbose_name='Evolução')),
                ('final_obs', models.TextField(verbose_name='Observações Finais')),
                ('wine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Wine')),
            ],
        ),
    ]