$(function(){

  function upload(){
    $('#btn-upload').on('click', function(){
      //console.log("data uploaded");
      get_ajax();
    })
  }

  upload();

  function get_ajax(){
    console.log("ajax fn");
    var user="Ruth";
    $.ajax({
      type: "post",
      url: "/upload",
      data: {'data': user}
      //data: { name: $('#dat').val() }
    });
  }

$('form').on('submit', function(e){
  $.ajax({
    data: { dat: $('#dat2').val() },
    type: 'POST',
    url: "/process"
  }).done(function(data){
  //  if(data)
    console.log(data.dat);
    $('#out').text(data.dat);
  })



  e.preventDefault()
})


})
