const renderer = new Renderer();
const plants = new Plants();
$(".profile").removeClass("active");
$(".home").addClass("active");
plants.getPlants().then(plants => {
  renderer.render(plants);
});
$(".plants").on("click", ".add-reminder", function () {
  userId = $(this).data().userId;
  plantId = $(this).data().plantId;
  $(`#modal${plantId}`).modal("toggle");
  plants.addPlantToUser(userId, plantId);
});
