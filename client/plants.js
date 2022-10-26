class Plants {
  constructor() {}
  getPlants() {
    return $.get("/plants");
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
}
