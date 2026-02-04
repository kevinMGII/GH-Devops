// Calculadora web simple
const display = document.getElementById('display');
let current = '';

document.querySelectorAll('[data-value]').forEach(btn =>
  btn.addEventListener('click', () => {
    current += btn.dataset.value;
    display.value = current;
  })
);

document.querySelectorAll('[data-op]').forEach(btn =>
  btn.addEventListener('click', () => {
    current += ' ' + btn.dataset.op + ' ';
    display.value = current;
  })
);

document.getElementById('clear').addEventListener('click', () => {
  current = '';
  display.value = '';
});

document.getElementById('equals').addEventListener('click', () => {
  try {
    // Evaluación simple usando Function — no para uso en producción con entradas no confiables
    const result = Function('"use strict"; return (' + current + ')')();
    display.value = result;
    current = String(result);
  } catch (e) {
    display.value = 'Error';
  }
});
