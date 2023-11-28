# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class TblAcordos(models.Model):
    acor_id = models.AutoField(db_column='acor_ID', primary_key=True)  # Field name made lowercase.
    acor_plan = models.ForeignKey('TblPlano', models.DO_NOTHING, db_column='acor_plan_ID')  # Field name made lowercase.
    acor_fid = models.ForeignKey('TblFidelidade', models.DO_NOTHING, db_column='acor_fid_ID')  # Field name made lowercase.
    acor_valor = models.FloatField(db_column='acor_Valor')  # Field name made lowercase.
    acor_sla = models.CharField(db_column='acor_SLA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    acor_padrao = models.IntegerField(db_column='acor_Padrao')  # Field name made lowercase.
    acor_ativo = models.IntegerField(db_column='acor_Ativo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_acordos'


class TblCidade(models.Model):
    cdd_id = models.AutoField(db_column='cdd_ID', primary_key=True)  # Field name made lowercase.
    cdd_nome = models.CharField(db_column='cdd_Nome', max_length=100)  # Field name made lowercase.
    cdd_uf = models.CharField(db_column='cdd_UF', max_length=45)  # Field name made lowercase.
    cdd_ativo = models.IntegerField(db_column='cdd_Ativo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_cidade'


class TblCiddplan(models.Model):
    cdd = models.ForeignKey(TblCidade, models.DO_NOTHING, db_column='cdd_ID')  # Field name made lowercase.
    plan = models.ForeignKey('TblPlano', models.DO_NOTHING, db_column='plan_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_ciddplan'


class TblFidelidade(models.Model):
    fid_id = models.AutoField(db_column='fid_ID', primary_key=True)  # Field name made lowercase.
    fid_qtdemeses = models.IntegerField(db_column='fid_QtdeMeses', unique=True)  # Field name made lowercase.
    fid_ativo = models.IntegerField(db_column='fid_Ativo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_fidelidade'


class TblItens(models.Model):
    item_id = models.AutoField(db_column='item_ID', primary_key=True)  # Field name made lowercase.
    item_nome = models.CharField(db_column='item_Nome', max_length=25)  # Field name made lowercase.
    item_ordem = models.IntegerField(db_column='item_Ordem', unique=True, blank=True, null=True, db_comment='Cadastre os itens que agrega maior valor no topo da lista')  # Field name made lowercase.
    item_icone = models.CharField(db_column='item_Icone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    item_detalhe = models.TextField(db_column='item_Detalhe', blank=True, null=True)  # Field name made lowercase.
    item_linkexterno = models.CharField(db_column='item_LinkExterno', max_length=45, blank=True, null=True)  # Field name made lowercase.
    item_ativo = models.IntegerField(db_column='item_Ativo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_itens'


class TblPlaniten(models.Model):
    item = models.ForeignKey(TblItens, models.DO_NOTHING, db_column='item_ID')  # Field name made lowercase.
    plan = models.ForeignKey('TblPlano', models.DO_NOTHING, db_column='plan_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_planiten'


class TblPlano(models.Model):
    plan_id = models.AutoField(db_column='plan_ID', primary_key=True)  # Field name made lowercase.
    plan_nome = models.CharField(db_column='plan_Nome', max_length=100, blank=True, null=True)  # Field name made lowercase.
    plan_valor = models.FloatField(db_column='plan_Valor', blank=True, null=True)  # Field name made lowercase.
    plan_ordem = models.IntegerField(db_column='plan_Ordem', unique=True, blank=True, null=True)  # Field name made lowercase.
    plan_taxaup = models.FloatField(db_column='plan_TaxaUp', blank=True, null=True)  # Field name made lowercase.
    plan_taxadown = models.FloatField(db_column='plan_TaxaDown', blank=True, null=True)  # Field name made lowercase.
    plan_destacarplano = models.IntegerField(db_column='plan_DestacarPlano')  # Field name made lowercase.
    plan_textdestaque = models.CharField(db_column='plan_TextDestaque', max_length=20, blank=True, null=True)  # Field name made lowercase.
    plan_tipocliente = models.CharField(db_column='plan_TipoCliente', max_length=11)  # Field name made lowercase.
    plan_tipolink = models.CharField(db_column='plan_TipoLink', max_length=13)  # Field name made lowercase.
    plan_combo = models.IntegerField(db_column='plan_Combo')  # Field name made lowercase.
    plan_icon = models.CharField(db_column='plan_Icon', max_length=255, blank=True, null=True)  # Field name made lowercase.
    plan_ativo = models.IntegerField(db_column='plan_Ativo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_plano'
