from django.db import models
from django.contrib.gis.db import models as gis_models

class GestorAmbiental(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    estado = models.CharField(max_length=2, default='PE')
    status_contrato = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome

class UsuarioGestor(models.Model):
    usuario = models.OneToOneField('usuarios.Usuario', on_delete=models.CASCADE, unique=True)
    gestor_ambiental = models.ForeignKey(GestorAmbiental, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.gestor_ambiental.nome}"

class RelatorioGestao(models.Model):
    gestor_ambiental = models.ForeignKey(GestorAmbiental, on_delete=models.CASCADE)
    tipo_relatorio = models.CharField(max_length=255)
    data_geracao = models.DateTimeField(auto_now_add=True)
    dados_json = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Relatório de {self.tipo_relatorio} - {self.data_geracao.strftime('%Y-%m-%d')}"

class AcessoQR(models.Model):
    qr_code = models.ForeignKey('zonas.QRCode', on_delete=models.CASCADE, related_name='acessos', null=True, blank=True)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.SET_NULL, null=True, blank=True)
    timestamp_acesso = models.DateTimeField(auto_now_add=True)
    latitude_dispositivo = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    longitude_dispositivo = models.DecimalField(max_digits=11, decimal_places=8, null=True, blank=True)
    info_dispositivo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Acesso QR {self.qr_code.code} por {self.usuario.username if self.usuario else 'Anônimo'}"

class HistoricoAcessoZona(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    zona = models.ForeignKey('zonas.Zona', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    via_qrcode = models.BooleanField(default=False)

    def __str__(self):
        return f"Acesso de {self.usuario.username} à {self.zona.nome}"

class HistoricoLocalizacao(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    timestamp_localizacao = models.DateTimeField(auto_now_add=True)
    coordenadas = gis_models.PointField(srid=4326)

    def __str__(self):
        return f"Localização de {self.usuario.username} em {self.timestamp_localizacao}"

class LogAcessoZonaRestrita(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    zona = models.ForeignKey('zonas.Zona', on_delete=models.CASCADE)
    timestamp_entrada = models.DateTimeField(auto_now_add=True)
    coordenada_entrada = gis_models.PointField(srid=4326, null=True, blank=True)
    notificacao_enviada = models.BooleanField(default=False)

    def __str__(self):
        return f"Log de acesso restrito de {self.usuario.username} à {self.zona.nome}"

class Feedback(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.SET_NULL, null=True, blank=True)
    ponto_interesse = models.ForeignKey('zonas.PontoDeInteresse', on_delete=models.SET_NULL, null=True, blank=True)
    tipo_feedback = models.CharField(max_length=255)
    mensagem = models.TextField()
    status = models.CharField(max_length=50, default='Recebido')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.tipo_feedback} de {self.usuario.username if self.usuario else 'Anônimo'}"

class UsuarioPontoFavorito(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    ponto_interesse = models.ForeignKey('zonas.PontoDeInteresse', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'ponto_interesse')

    def __str__(self):
        return f"{self.usuario.username} - {self.ponto_interesse.nome}"

class BoletimBalneabilidade(models.Model):
    ponto_interesse = models.ForeignKey('zonas.PontoDeInteresse', on_delete=models.CASCADE)
    data_emissao = models.DateField()
    status = models.CharField(max_length=255)
    fonte = models.CharField(max_length=255, default='CPRH')

    class Meta:
        unique_together = ('ponto_interesse', 'data_emissao')

    def __str__(self):
        return f"Boletim {self.status} para {self.ponto_interesse.nome} em {self.data_emissao}"

class InteracaoIA(models.Model):
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.SET_NULL, null=True, blank=True)
    timestamp_interacao = models.DateTimeField(auto_now_add=True)
    pergunta = models.TextField(blank=True, null=True)
    resposta_gerada = models.TextField(blank=True, null=True)
    contexto_localizacao = gis_models.PointField(srid=4326, null=True, blank=True)
    avaliacao_utilidade = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Interação IA por {self.usuario.username if self.usuario else 'Anônimo'} em {self.timestamp_interacao}"

class PerfilTuristaAnalytics(models.Model):
    usuario = models.OneToOneField('usuarios.Usuario', on_delete=models.CASCADE, unique=True)
    origem_cidade = models.CharField(max_length=255, blank=True, null=True)
    origem_pais = models.CharField(max_length=255, default='Brasil')
    interesses_declarados = models.JSONField(blank=True, null=True)
    total_acessos_qr = models.IntegerField(default=0)
    zonas_mais_visitadas = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"
