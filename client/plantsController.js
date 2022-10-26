const renderer = new Renderer();
const plants = new Plants();
$(".profile").removeClass("active");
$(".home").addClass("active");
plants.getPlants().then(plants => {
  renderer.render(plants);
});
plants.getPlantsNames().then((plants_names) => {
    const autoCompleteJS = new autoComplete({
        placeHolder: "Search for Plant...",
        data: {
            src: plants_names,
            cache: true,
        },
        resultItem: {
            highlight: true,
        },
        events: {
            input: {
                selection: (event) => {
                    const selection = event.detail.selection.value;
                    autoCompleteJS.input.value = selection;
                    plants.getPlantByName(selection).then((plants) => {
                        renderer.render(plants);
                    });
                },
            },
        },
    });
});
$(".plants").on("click", ".add-reminder", function () {
  userId = $(this).data().userId;
  plantId = $(this).data().plantId;
  $(`#modal${plantId}`).modal("toggle");
  plants.addPlantToUser(userId, plantId);
});
