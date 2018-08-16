<?php
$name=$_POST['name'];
$email=$_POST['email'];
$subject=$_POST['subject'];
$message=$_POST['message'];
$to="subhiahsan@gmail.com";
$message="Dear, <br /> <br />".$message;
$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-type:text/html;charset=iso-8859-1" . "\r\n";
// More headers
$headers .= 'From:'.$name.' <'.$email.'>'."\r\n" . 'Reply-To: '.$name.' <'.$email.'>'."\r\n";
$headers .= 'Cc: subhiahsan@gmail.com' . "\r\n"; //untuk cc lebih dari satu tinggal kasih koma
@mail($to,$subject,$message,$headers);
if (@mail) { ?>
<script language="javascript" type="text/javascript">
alert('Terima kasih telah mengirim pesan, saya akan respon secepatnya :)');
window.location = 'index.html';
</script>
<?php
}
else { ?>
<script language="javascript" type="text/javascript">
alert('Gagal mengirim, kirim email aja ya ke subhiahsan@gmail.com');
window.location = 'index.html';
</script>
<?php
}
?>
