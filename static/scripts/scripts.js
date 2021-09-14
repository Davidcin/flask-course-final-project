$(function () {
  count = 0;
  wordsArray = ["Tech", "Phone", "Proccesor", "Videocard", "Laptop"];
  setInterval(function () {
    count++;
    $("#word").fadeOut(400, function () {
      $(this).text(wordsArray[count % wordsArray.length]).fadeIn(400);
    });
  }, 2000);
});