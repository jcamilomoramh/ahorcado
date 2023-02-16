<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $nombre = $_POST["nombre"];
  $email = $_POST["email"];
  $mensaje = $_POST["mensaje"];

  $destinatario = "camilomoramh@hotmail.com";
  $asunto = "Nuevo mensaje del formulario de contacto";
  $cuerpo = "Nombre: $nombre\nCorreo electrónico: $email\nMensaje:\n$mensaje";

  if (mail($destinatario, $asunto, $cuerpo)) {
    echo "Gracias por contactarnos, pronto nos pondremos en contacto contigo.";
  } else {
    echo "Hubo un problema al enviar el correo, inténtalo de nuevo más tarde.";
  }
}
?>
