const renderer = new Renderer();
const plants = new Plants();
userId = 1;
$(".profile").addClass("active");
$(".home").removeClass("active");
plants.getUserPlants(userId).then(plants => {
  renderer.render(plants);
});
$(".plants").on("click", ".cancel-reminder", function () {
  userId = $(this).data().userId;
  plantId = $(this).data().plantId;
  $(`#modal${plantId}`).modal("toggle");
  plants.deletePlantOfUser(userId, plantId).then(userPlants => {
    renderer.render(userPlants);
  });
});
$(".pause").on("click", function () {
  plants.pausePlantsNotifications(userId).then(res => {
    alert("Paused all notifications. :(");
  });
});
