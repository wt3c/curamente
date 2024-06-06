class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(allow_null=True, required=False)
    contatos = ContatosSerializer()
    sessao = SessaoSerializer(many=True)

    class Meta:
        model = Profile
        fields = ["user", "tipo", "foto", "contatos", "sessao"]

    def create(self, validated_data):
        user = self.create_user(validated_data)
        contatos = self.create_contatos(validated_data)
        validated_data["contatos"] = contatos
        profile = self.create_profile(validated_data, user)
        self.create_sessao(validated_data, profile)
        return profile

    def update(self, instance, validated_data):
        self.update_user(instance, validated_data)
        self.update_profile(instance, validated_data)
        self.update_contatos(instance, validated_data)
        self.update_sessao(instance, validated_data)
        instance.save()
        return instance

    # Helper Methods
    def create_user(self, validated_data):
        fields_user = validated_data.pop("user")
        return User.objects.create_user(
            password=make_password(fields_user.pop("password")),
            **fields_user
        )

    def create_contatos(self, validated_data):
        contatos_data = validated_data.pop("contatos")
        return Contatos.objects.create(**contatos_data)

    def create_profile(self, validated_data, user):
        sessao_list = validated_data.pop("sessao")
        return Profile.objects.create(user=user, **validated_data)

    def create_sessao(self, validated_data, profile):
        sessao_list = validated_data.pop("sessao")
        for sessao in sessao_list:
            sessao_id = Sessao.objects.create(**sessao)
            profile.sessao.add(sessao_id)

    def update_user(self, instance, validated_data):
        fields_user = validated_data.pop("usuario")
        instance.user.first_name = fields_user.get("first_name")
        instance.user.last_name = fields_user.get("last_name")
        instance.user.save()

    def update_profile(self, instance, validated_data):
        instance.tipo = validated_data.get("tipo")
        instance.foto = validated_data.get("foto")

    def update_contatos(self, instance, validated_data):
        instance.contatos.telefone = validated_data.get("contatos").get("telefone")
        instance.contatos.email = validated_data.get("contatos").get("email")
        instance.contatos.save()

    def update_sessao(self, instance, validated_data):
        instance.sessao.clear()
        for sessao in validated_data.get("sessao"):
            updated, created = Sessao.objects.update_or_create(
                horario=sessao.get("horario"),
                defaults={**sessao}
            )
            instance.sessao.add(updated)