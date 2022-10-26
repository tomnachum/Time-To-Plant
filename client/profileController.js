const renderer = new Renderer();
const plants = new Plants();
userId = 1;

plants.getUserPlants(userId).then((plants) => {
  renderer.render(plants);
});

$(".plants").on("click", ".cancel-reminder", function () {
  userId = $(this).data().userId;
  plantId = $(this).data().plantId;
  plants.deletePlantOfUser(userId, plantId).then((userPlants) => {
    renderer.render(userPlants);
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
