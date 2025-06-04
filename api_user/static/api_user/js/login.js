document.getElementById('login-form').addEventListener('submit', async function (e) {
  e.preventDefault();

  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const errorMsg = document.getElementById('error-msg');

  const response = await fetch('/api/login/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })  // aquí enviamos email y password
  });

  const data = await response.json();

  if (response.ok) {
    localStorage.setItem('access', data.access);
    localStorage.setItem('refresh', data.refresh);
    alert('Login exitoso');
    window.location.href = '/dashboard/'; // ruta a tu dashboard o página post-login
  } else {
    errorMsg.textContent = data.detail || 'Credenciales inválidas';
  }
});
