document.addEventListener('DOMContentLoaded', () => {
  const fabricantesSelect = document.getElementById('fabricantes');
  const modelosSelect = document.getElementById('modelos');
  const resultadoDiv = document.getElementById('resultado');

  // carrega fabricantes
  fetch('https://parallelum.com.br/fipe/api/v1/carros/marcas')
    .then(resp => resp.json())
    .then(fabricantes => {
      fabricantes.forEach(fab => {
        let opt = document.createElement('option');
        opt.value = fab.codigo;
        opt.textContent = fab.nome;
        fabricantesSelect.appendChild(opt);
      });
    });

  // mudanças no fabricante
  fabricantesSelect.addEventListener('change', () => {
    const fabricanteId = fabricantesSelect.value;
    fetch(`https://parallelum.com.br/fipe/api/v1/carros/marcas/${fabricanteId}/modelos`)
      .then(resp => resp.json())
      .then(data => {
        modelosSelect.innerHTML = '';
        data.modelos.forEach(mod => {
          let opt = document.createElement('option');
          opt.value = mod.codigo;
          opt.textContent = mod.nome;
          modelosSelect.appendChild(opt);
        });
        resultadoDiv.textContent = '';
      });
  });

  // detalhes do modelo selecionado
  modelosSelect.addEventListener('change', () => {
    const fabricanteId = fabricantesSelect.value;
    const modeloId = modelosSelect.value;
    fetch(`https://parallelum.com.br/fipe/api/v1/carros/marcas/${fabricanteId}/modelos/${modeloId}/anos`)
      .then(resp => resp.json())
      .then(anos => {
        resultadoDiv.innerHTML = `<strong>Anos disponíveis:</strong> ${anos.map(a => a.nome).join(', ')}`;
      });
  });
});
