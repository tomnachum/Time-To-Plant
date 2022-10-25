const renderer = new Renderer();
const plants = new Plants();
plants.getPlants().then((plants) => {
    renderer.render(plants);
});

$(".plants").on("click", ".add-reminder", function () {
    userId = $(this).data().userId;
    plantId = $(this).data().plantId;
    plants.addPlantToUser(userId, plantId);
});
