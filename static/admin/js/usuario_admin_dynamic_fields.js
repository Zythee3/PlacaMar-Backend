(function($) {
    $(document).ready(function() {
        var paisOrigemField = $('#id_pais_origem');
        var estadoOrigemField = $('#id_estado_origem');
        var cidadeOrigemField = $('#id_cidade_origem');

        var estadosBrasileiros = [
            {value: 'AC', text: 'Acre'}, {value: 'AL', text: 'Alagoas'}, {value: 'AP', text: 'Amapá'},
            {value: 'AM', text: 'Amazonas'}, {value: 'BA', text: 'Bahia'}, {value: 'CE', text: 'Ceará'},
            {value: 'DF', text: 'Distrito Federal'}, {value: 'ES', text: 'Espírito Santo'}, {value: 'GO', text: 'Goiás'},
            {value: 'MA', text: 'Maranhão'}, {value: 'MT', text: 'Mato Grosso'}, {value: 'MS', text: 'Mato Grosso do Sul'},
            {value: 'MG', text: 'Minas Gerais'}, {value: 'PA', text: 'Pará'}, {value: 'PB', text: 'Paraíba'},
            {value: 'PR', text: 'Paraná'}, {value: 'PE', text: 'Pernambuco'}, {value: 'PI', text: 'Piauí'},
            {value: 'RJ', text: 'Rio de Janeiro'}, {value: 'RN', text: 'Rio Grande do Norte'}, {value: 'RS', text: 'Rio Grande do Sul'},
            {value: 'RO', text: 'Rondônia'}, {value: 'RR', text: 'Roraima'}, {value: 'SC', text: 'Santa Catarina'},
            {value: 'SP', text: 'São Paulo'}, {value: 'SE', text: 'Sergipe'}, {value: 'TO', text: 'Tocantins'}
        ];

        var cidadesPorEstado = {
            'AC': ['Rio Branco', 'Cruzeiro do Sul', 'Sena Madureira', 'Tarauacá'],
            'AL': ['Maceió', 'Arapiraca', 'Palmeira dos Índios', 'Rio Largo'],
            'AP': ['Macapá', 'Santana', 'Laranjal do Jari', 'Oiapoque'],
            'AM': ['Manaus', 'Parintins', 'Itacoatiara', 'Coari'],
            'BA': ['Salvador', 'Feira de Santana', 'Vitória da Conquista', 'Camaçari', 'Itabuna'],
            'CE': ['Fortaleza', 'Juazeiro do Norte', 'Sobral', 'Caucaia', 'Maracanaú'],
            'DF': ['Brasília', 'Ceilândia', 'Taguatinga', 'Samambaia'],
            'ES': ['Vitória', 'Vila Velha', 'Serra', 'Cariacica', 'Linhares'],
            'GO': ['Goiânia', 'Aparecida de Goiânia', 'Anápolis', 'Rio Verde', 'Luziânia'],
            'MA': ['São Luís', 'Imperatriz', 'Caxias', 'Timon'],
            'MT': ['Cuiabá', 'Várzea Grande', 'Rondonópolis', 'Sinop'],
            'MS': ['Campo Grande', 'Dourados', 'Três Lagoas', 'Corumbá'],
            'MG': ['Belo Horizonte', 'Uberlândia', 'Contagem', 'Juiz de Fora', 'Betim', 'Montes Claros'],
            'PA': ['Belém', 'Ananindeua', 'Santarém', 'Marabá', 'Parauapebas'],
            'PB': ['João Pessoa', 'Campina Grande', 'Patos', 'Santa Rita'],
            'PR': ['Curitiba', 'Londrina', 'Maringá', 'Ponta Grossa', 'Cascavel'],
            'PE': ['Recife', 'Jaboatão dos Guararapes', 'Olinda', 'Caruaru', 'Petrolina'],
            'PI': ['Teresina', 'Parnaíba', 'Picos', 'Floriano'],
            'RJ': ['Rio de Janeiro', 'Niterói', 'Duque de Caxias', 'Nova Iguaçu', 'São Gonçalo', 'Petrópolis'],
            'RN': ['Natal', 'Mossoró', 'Parnamirim', 'Caicó'],
            'RS': ['Porto Alegre', 'Caxias do Sul', 'Pelotas', 'Canoas', 'Santa Maria'],
            'RO': ['Porto Velho', 'Ji-Paraná', 'Ariquemes', 'Cacoal'],
            'RR': ['Boa Vista', 'Rorainópolis', 'Caracaraí'],
            'SC': ['Florianópolis', 'Joinville', 'Blumenau', 'Chapecó', 'Criciúma'],
            'SP': ['São Paulo', 'Campinas', 'Santos', 'São Bernardo do Campo', 'Guarulhos', 'Ribeirão Preto', 'Sorocaba', 'São José dos Campos'],
            'SE': ['Aracaju', 'Nossa Senhora do Socorro', 'Lagarto', 'Itabaiana'],
            'TO': ['Palmas', 'Araguaína', 'Gurupi', 'Porto Nacional']
        };

        function atualizarCidades() {
            var estado = estadoOrigemField.val();
            cidadeOrigemField.empty();

            if (paisOrigemField.val() !== 'Brasil') {
                cidadeOrigemField.append($('<option></option>').attr('value', 'Outro').text('Outro'));
                cidadeOrigemField.val('Outro');
                return;
            }

            if (cidadesPorEstado.hasOwnProperty(estado)) {
                cidadeOrigemField.append($('<option></option>').attr('value', '').text('---------'));
                $.each(cidadesPorEstado[estado], function(i, cidade) {
                    cidadeOrigemField.append($('<option></option>').attr('value', cidade).text(cidade));
                });
            } else {
                cidadeOrigemField.append($('<option></option>').attr('value', 'Outro').text('Outro'));
            }
        }

        function toggleEstadoCidadeFields() {
            estadoOrigemField.empty();
            cidadeOrigemField.empty();

            if (paisOrigemField.val() === 'Brasil') {
                estadoOrigemField.append($('<option></option>').attr('value', '').text('---------'));
                $.each(estadosBrasileiros, function(i, estado) {
                    estadoOrigemField.append($('<option></option>').attr('value', estado.value).text(estado.text));
                });
                cidadeOrigemField.closest('.form-row').show();
                atualizarCidades();
            } else {
                estadoOrigemField.append($('<option></option>').attr('value', 'Outro').text('Outro'));
                estadoOrigemField.val('Outro');
                cidadeOrigemField.append($('<option></option>').attr('value', 'Outro').text('Outro'));
                cidadeOrigemField.val('Outro');
                cidadeOrigemField.closest('.form-row').show();
            }

            estadoOrigemField.closest('.form-row').show();
        }

        // Inicializa
        toggleEstadoCidadeFields();

        // Eventos
        paisOrigemField.change(toggleEstadoCidadeFields);
        estadoOrigemField.change(atualizarCidades);
    });
})(django.jQuery);