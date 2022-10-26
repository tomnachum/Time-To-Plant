class Plants {
  constructor() {}
  getPlants() {
    return $.get("/plants");
  }
  getPlantsNames() {
    return $.get("/plants").then(plants => {
      return plants.map(plant => plant["name"]);
    });
  }
  getPlantByName(plantName) {
    return $.get(`/search?plant_name=${plantName}`);
  }
  getUserPlants(userId) {
    return $.get(`/plants/${userId}`);
  }
  addPlantToUser(userId, plantId) {
    return $.post(`/users/${userId}/plants/${plantId}`);
  }
  deletePlantOfUser(userId, plantId) {
    return $.ajax({
      url: `/users/${userId}/plants/${plantId}`,
      type: "DELETE",
    });
  }
  pausePlantsNotifications(userId) {
    return $.ajax({
      url: `/users/${userId}/notification`,
      type: "DELETE",
    });
  }
  isPaused(userId) {
    return $.get(`/isPaused/${userId}`);
  }
  resumePlantsNotifications(userId) {
    return $.ajax({
      url: `/users/${userId}/notification`,
      type: "POST",
    });
  }
}
