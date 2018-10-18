/* affix the 2nd navbar after scroll past first navbar */
$(document).ready(function() {
  $("#nav2").affix({
    offset: {
      top: 50
    }
  });
});
