(function($) {
    $(document).ready(function() {
        var paisOrigemField = $('#id_pais_origem');
        var estadoOrigemField = $('#id_estado_origem');
        var cidadeOrigemField = $('#id_cidade_origem');
        var sexoField = $('#id_sexo');

        var estadosBrasileiros = [];
        var cidadesPorEstado = {};
        var sexoChoices = [];

        // Fetch choices from backend
        $.ajax({
            url: '/api/choices/',
            method: 'GET',
            success: function(data) {
                estadosBrasileiros = data.estados_brasileiros;
                sexoChoices = data.sexo;
                // Populate sexo field
                sexoField.empty();
                sexoField.append($('<option></option>').attr('value', '').text('Selecione'));
                $.each(sexoChoices, function(i, opcao) {
                    sexoField.append($('<option></option>').attr('value', opcao).text(opcao));
                });
                // Initialize dynamic fields after data is loaded
                toggleEstadoCidadeFields();
                // Trigger change event to ensure initial population if a country is already selected
                paisOrigemField.trigger('change');
            },
            error: function(error) {
                console.error('Erro ao buscar opções do backend:', error);
            }
        });

        function atualizarCidades() {
            var estadoId = estadoOrigemField.val();
            console.log('atualizarCidades: País selecionado:', paisOrigemField.val());
            console.log('atualizarCidades: Estado selecionado (ID):', estadoId);

            cidadeOrigemField.empty();
            cidadeOrigemField.append($('<option></option>').attr('value', '').text('---------'));

            if (paisOrigemField.val() !== 'Brasil' || !estadoId) {
                console.log('atualizarCidades: País não é Brasil ou estadoId vazio. Adicionando "Outro".');
                cidadeOrigemField.append($('<option></option>').attr('value', 'Outro').text('Outro'));
                cidadeOrigemField.val('Outro');
                return;
            }

            $.ajax({
                url: '/api/cidades-por-estado/' + estadoId + '/',
                method: 'GET',
                success: function(data) {
                    console.log('Cidades recebidas:', data.cidades);
                    $.each(data.cidades, function(i, cidade) {
                        cidadeOrigemField.append($('<option></option>').attr('value', cidade.id).text(cidade.nome));
                    });
                },
                error: function(error) {
                    console.error('Erro ao buscar cidades:', error);
                    cidadeOrigemField.append($('<option></option>').attr('value', 'Outro').text('Outro'));
                    cidadeOrigemField.val('Outro');
                }
            });
        }

        function toggleEstadoCidadeFields() {
            estadoOrigemField.empty();
            cidadeOrigemField.empty();

            if (paisOrigemField.val() === 'Brasil') {
                estadoOrigemField.append($('<option></option>').attr('value', '').text('---------'));
                $.each(estadosBrasileiros, function(i, estado) {
                    estadoOrigemField.append($('<option></option>').attr('value', estado.value).text(estado.text));
                });
                estadoOrigemField.trigger('change'); // Trigger change to update cities
                cidadeOrigemField.closest('.form-row').show();
            } else {
                estadoOrigemField.append($('<option></option>').attr('value', 'Outro').text('Outro'));
                estadoOrigemField.val('Outro');
                cidadeOrigemField.append($('<option></option>').attr('value', 'Outro').text('Outro'));
                cidadeOrigemField.val('Outro');
                cidadeOrigemField.closest('.form-row').show();
            }

            estadoOrigemField.closest('.form-row').show();
        }

        // Eventos
        paisOrigemField.change(toggleEstadoCidadeFields);
        estadoOrigemField.change(atualizarCidades);
    });
})(django.jQuery);