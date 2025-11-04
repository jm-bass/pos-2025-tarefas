import './style.css'

// cliente-vite/main.js
import { getFabricantes, getModelos, getAnos } from './fipeApi.js';

const fabricantesSelect = document.getElementById('fabricantes');
const modelosSelect = document.getElementById('modelos');
const resultadoDiv = document.getElementById('resultado');

// Popula fabricantes no carregamento
getFabricantes().then(fabricantes => {
  fabricantes.forEach(fab => {
    let opt = document.createElement('option');
    opt.value = fab.codigo;
    opt.textContent = fab.nome;
    fabricantesSelect.appendChild(opt);
  });
});

fabricantesSelect.addEventListener('change', () => {
  const fabId = fabricantesSelect.value;
  getModelos(fabId).then(data => {
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

modelosSelect.addEventListener('change', () => {
  const fabId = fabricantesSelect.value;
  const modeloId = modelosSelect.value;
  getAnos(fabId, modeloId).then(anos => {
    resultadoDiv.innerHTML = `<strong>Anos disponíveis:</strong> ${anos.map(a => a.nome).join(', ')}`;
  });
});