function validateForm() {
    let nama = document.forms["formAdd"]["nama"].value;
    if (nama == "") {
      alert("Harap Isi Nama Anda");
      alertNama = "Harap Isi Nama Anda";
      return false;
    } else if (!(nama >= "a" && nama <= "z") && !(nama >= "A" && nama <= "Z")) {
      alert("Harap Isi Nama Anda Dengan Benar");
      alertNama = "Harap Isi Nama Anda Dengan Benar";
      return false;
    }
    document.getElementById("alertNama").innerHTML = alertNama;


    let usia = document.forms["formAdd"]["usia"].value;
    if (usia == "") {
      alert("Name must be filled out");
      return false;
    }
  }