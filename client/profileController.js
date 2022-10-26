const renderer = new Renderer();
const plants = new Plants();
userId = 1;
$(".profile").addClass("active");
$(".home").removeClass("active");
plants.isPaused(userId).then((isPaused) => {
  $(".pause").html(isPaused ? "Resume notifications" : "Pause notifications");
});

plants.getUserPlants(userId).then((plants) => {
  renderer.render(plants);
  console.log(plants);
});

$(".plants").on("click", ".cancel-reminder", function () {
  userId = $(this).data().userId;
  plantId = $(this).data().plantId;
  // $(`#modal${plantId}`).modal("toggle");
  plants.deletePlantOfUser(userId, plantId).then((userPlants) => {
    renderer.render(userPlants);
  });
});
$(".pause").on("click", function () {
  plants.isPaused(userId).then((isPaused) => {
    if (isPaused) {
      plants.resumePlantsNotifications(userId).then((res) => {
        alert("Resumed all notifications. :)");
      });
      $(".pause").html("Pause notifications");
    } else {
      plants.pausePlantsNotifications(userId).then((res) => {
        alert("Paused all notifications. :(");
      });
      $(".pause").html("Reusme notifications");
    }
  });
});

$(".plants").on("click", ".note-btn", function () {
  userId = $(this)
    .closest(".modal")
    .siblings(".card-body")
    .find("button")
    .data().userId;

  plantId = $(this)
    .closest(".modal")
    .siblings(".card-body")
    .find("button")
    .data().plantId;

  note = $(this)
    .closest(".modal-footer")
    .siblings(".modal-body")
    .find(".note")
    .val();

  plants.updateNote(userId, plantId, note);
});
