$(document).ready(function(){
  var msg_id = 0;
  var love = 40;
  chatapi(msg_id);
  $(".next-button").click(function(){
    chatapi(msg_id);
  });
  function chatapi(message_id){
    $.ajax({
      url: '/api/chat',
      data: {message_id: message_id},
      dataType: 'json',
      success: function(message) {
          if(message.chater == "woman"){
            loveapi(love,message.text);
            // 親密度の反映
            $("p").html(message.text);
          }else{
            $("p").html('(俺) '+message.text);
          }
          msg_id += 1;
      }
    });
  }
  function loveapi(love_value,text){
    $.ajax({
      url: '/api/love',
      data: {love_value: love_value,text: text},
      success: function(love_value) {
          love =  Number(love_value);
          console.log(love);
          $("#love-gage").html(love);
      }
    });
  }
});
