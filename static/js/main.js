$(document).ready(function(){
  var msg_id = 1;
  var love = 50;
  chatapi(msg_id);
  $("#button").click(function(){
    chatapi(msg_id);
  });
  function chatapi(message_id){
    $.ajax({
      url: '/api/chat',
      data: {message_id: message_id},
      success: function(d) {
          console.log('chat api succeeded.');
          message = $.parseJson(d);
          if(message.chater == "woman"){
            $("#message_window").text = message.text;
            love = loveapi(love,message.text);
            // 親密度の反映
            $("#love_gage").value = love;
          }else{
            $("#message_window").text = message.text;
          }
          msg_id = message.message_id;
          return;
      }
    });
  }
  function loveapi(love_value,text){
    $.ajax({
      url: '/api/love',
      data: {love_value: love_value,text: text},
      success: function(love_value) {
          console.log('love api succeeded.');
          return love_value;
      }
    });
  }
});
