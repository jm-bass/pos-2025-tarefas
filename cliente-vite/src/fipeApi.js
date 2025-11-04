export async function getFabricantes() {
  const resp = await fetch('https://parallelum.com.br/fipe/api/v1/carros/marcas');
  return await resp.json();
}

export async function getModelos(fabId) {
  const resp = await fetch(`https://parallelum.com.br/fipe/api/v1/carros/marcas/${fabId}/modelos`);
  return await resp.json();
}

export async function getAnos(fabId, modeloId) {
  const resp = await fetch(`https://parallelum.com.br/fipe/api/v1/carros/marcas/${fabId}/modelos/${modeloId}/anos`);
  return await resp.json();
}
