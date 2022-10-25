class Plants {
    constructor() {}
    getPlants() {
        return $.get("/plants");
    }
    addPlantToUser(userId, plantId) {
        return $.post(`/users/${userId}/plants/${plantId}`);
    }
}
