const renderer = new Renderer();
const plants = new Plants();
plants.getPlants().then((plants) => {
    renderer.render(plants);
});
