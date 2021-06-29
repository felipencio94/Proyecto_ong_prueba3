      function fn_ocultarEtiquetas()
      {
        document.getElementById('lbl_usuario').style.visibility ="hidden";
        document.getElementById('lbl_contrasena').style.visibility ="hidden";

      }

      function fn_mostrarEtiquetas()
      {
          var usuario = document.getElementById('txt_usuario').value;
          var contrasena = document.getElementById("txt_contrasena").value;

          if(usuario == "")
          {
            document.getElementById('lbl_usuario').style.visibility ="visible";
            document.getElementById('txt_usuario').classList.add('is-invalid');
          }
          else
          {
            document.getElementById('lbl_usuario').style.visibility ="hidden";
            document.getElementById('txt_usuario').classList.remove('is-invalid');
            document.getElementById('txt_usuario').classList.add('is-valid');

          }

          if(contrasena == "")
          {
            document.getElementById('lbl_contrasena').style.visibility ="visible";
            document.getElementById('txt_contrasena').classList.add('is-invalid');

          }
          else
          {
            document.getElementById('lbl_contrasena').style.visibility ="hidden";
            document.getElementById('txt_contrasena').classList.remove('is-invalid');
            document.getElementById('txt_contrasena').classList.add('is-valid');


          }
      }


    $('#btn_ingresar').click(function()
    {
        fn_mostrarEtiquetas();
    })