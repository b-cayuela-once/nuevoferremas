document.getElementById('signup-form').addEventListener('submit', async function(event) {
  event.preventDefault();

  const form = event.target;

  const data = {
    rut: form.rut.value,
    email: form.email.value,
    password: form.password.value,
    nombre: form.nombre.value,
    apellido: form.apellido.value,
    direccion: form.direccion.value,
  };

  try {
    const res = await fetch('/api/signup/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    const result = await res.json();

    const messageDiv = document.getElementById('message');

    if (res.ok) {
      messageDiv.textContent = 'Usuario creado correctamente!';
      form.reset();
    } else {
      messageDiv.textContent = 'Error: ' + JSON.stringify(result);
    }
  } catch (error) {
    document.getElementById('message').textContent = 'Error de conexión';
  }
});
