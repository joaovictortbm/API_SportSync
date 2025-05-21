from django.db import models


class Usuario(models.Model):

    STATUS_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    ]

    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(
        max_length=100)
    email = models.CharField(unique=True, max_length=100)
    senha = models.CharField(
        max_length=100)
    tipo_usuario = models.CharField(
        max_length=50, choices=STATUS_CHOICES)

    class Meta:
        db_table = 'Usuario'

    def __str__(self):
        return f"{self.nome} ({self.email})"


class Desempenho(models.Model):
    id_desempenho = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, db_column='id_aluno')
    indicador = models.CharField(
        max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_registro = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Desempenho'

    def __str__(self):
        return f"{self.indicador}: {self.valor} ({self.data_registro})"


class Plano(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]

    id_plano = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, db_column='id_aluno')
    nome_plano = models.CharField(
        max_length=100)
    descricao = models.TextField(
        blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES)

    class Meta:
        db_table = 'Plano'

    def __str__(self):
        return f"{self.nome_plano} ({self.status})"


class Treino(models.Model):
    STATUS_CHOICES = [
        ('concluido', 'Concluído'),
        ('pendente', 'Pendente'),
    ]

    id_treino = models.AutoField(primary_key=True)
    id_plano = models.ForeignKey(
        Plano, on_delete=models.CASCADE, db_column='id_plano')
    data_criacao = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES)
    nome_treino = models.CharField(
        max_length=100)
    descricao = models.TextField(
        blank=True, null=True)

    class Meta:
        db_table = 'Treino'

    def __str__(self):
        return f"{self.nome_treino} ({self.status})"


class Avaliacao(models.Model):
    id_avaliacao = models.AutoField(primary_key=True)
    id_treino = models.ForeignKey(
        Treino, on_delete=models.CASCADE, db_column='id_treino')
    nota = models.SmallIntegerField()
    comentario = models.TextField(
        blank=True, null=True)
    data_avaliacao = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Avaliacao'

    def __str__(self):
        return f"Nota {self.nota} em {self.data_avaliacao}"
